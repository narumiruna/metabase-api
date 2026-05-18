from __future__ import annotations

import argparse
import importlib
import inspect
import json
import pkgutil
import re
from collections import defaultdict
from collections.abc import Sequence
from pathlib import Path
from typing import Any
from typing import cast

import metabaseapi.endpoints.requests as request_package
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.utils import download_openapi_document_from_env

HTTP_METHODS = frozenset({"DELETE", "GET", "PATCH", "POST", "PUT"})
DEFAULT_OPENAPI_PATH = Path("/tmp/metabase-api-openapi.json")

type OpenAPIOperation = tuple[str, dict[str, Any], list[dict[str, Any]]]
type OpenAPIOperations = dict[tuple[str, str], list[OpenAPIOperation]]
type ImplementedOperation = tuple[str, str, type[EndpointRequest[Any]], str]
type ImplementedOperations = dict[tuple[str, str], list[ImplementedOperation]]


def normalize_path(path: str) -> str:
    path = re.sub(r":([A-Za-z][A-Za-z0-9_-]*)", "{}", path)
    return re.sub(r"\{[^}/]+\}", "{}", path)


def path_placeholders(path: str) -> set[str]:
    return set(re.findall(r"\{([^}/]+)\}", path))


def python_field_name(name: str) -> str:
    return name.replace("-", "_")


def load_openapi_operations(document: dict[str, Any]) -> OpenAPIOperations:
    operations: OpenAPIOperations = defaultdict(list)
    paths = document.get("paths", {})
    if not isinstance(paths, dict):
        return operations

    for path, item in paths.items():
        if not isinstance(path, str) or not isinstance(item, dict):
            continue
        inherited_params = [param for param in item.get("parameters", []) if is_parameter(param, "path")]
        for method, operation in item.items():
            if not isinstance(method, str):
                continue
            upper_method = method.upper()
            if upper_method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            params = inherited_params + [param for param in operation.get("parameters", []) if isinstance(param, dict)]
            operations[(upper_method, normalize_path(path))].append((path, operation, params))
    return operations


def is_parameter(value: object, location: str) -> bool:
    if not isinstance(value, dict):
        return False
    parameter = cast("dict[str, object]", value)
    return parameter.get("in") == location


def load_implemented_operations() -> ImplementedOperations:
    operations: ImplementedOperations = defaultdict(list)
    for module_info in pkgutil.iter_modules(request_package.__path__, request_package.__name__ + "."):
        if module_info.ispkg:
            continue
        module = importlib.import_module(module_info.name)
        for class_name, request_class in inspect.getmembers(module, inspect.isclass):
            if request_class is EndpointRequest:
                continue
            if not issubclass(request_class, EndpointRequest) or request_class.__module__ != module.__name__:
                continue
            method = getattr(request_class, "endpoint_method", None)
            path = getattr(request_class, "endpoint_path", None)
            if isinstance(method, str) and isinstance(path, str):
                operations[(method, normalize_path(path))].append((module.__name__, class_name, request_class, path))
    return operations


def placeholder_gaps(implemented_operations: ImplementedOperations) -> list[tuple[str, str, str, str]]:
    gaps: list[tuple[str, str, str, str]] = []
    for implementations in implemented_operations.values():
        for module_name, class_name, request_class, path in implementations:
            fields = set(request_class.model_fields)
            gaps.extend(
                (module_name, class_name, path, value) for value in path_placeholders(path) if value not in fields
            )
    return gaps


def request_body_gaps(
    openapi_operations: OpenAPIOperations,
    implemented_operations: ImplementedOperations,
) -> list[tuple[str, str, str, str]]:
    gaps: list[tuple[str, str, str, str]] = []
    for key, operations in openapi_operations.items():
        for openapi_route, operation, _params in operations:
            for module_name, class_name, request_class, path in implemented_operations.get(key, []):
                fields = set(request_class.model_fields)
                has_default_body = request_class.request_body is EndpointRequest.request_body
                if "requestBody" in operation and "body" not in fields and has_default_body:
                    gaps.append((module_name, class_name, path, openapi_route))
    return gaps


def static_class_attr(cls: type[object], name: str) -> object:
    return inspect.getattr_static(cls, name)


def supports_generic_query_params(request_class: type[EndpointRequest[Any]]) -> bool:
    has_base_do = static_class_attr(request_class, "do") is EndpointRequest.do
    has_base_param_merge = (
        static_class_attr(
            request_class,
            "merged_request_params",
        )
        is EndpointRequest.merged_request_params
    )
    if "params" not in request_class.model_fields:
        return False
    if not has_base_do:
        return False
    return has_base_param_merge


def query_param_gaps(
    openapi_operations: OpenAPIOperations,
    implemented_operations: ImplementedOperations,
) -> list[tuple[str, str, str, str, list[str]]]:
    gaps: list[tuple[str, str, str, str, list[str]]] = []
    for key, operations in openapi_operations.items():
        for openapi_route, _operation, params in operations:
            for module_name, class_name, request_class, path in implemented_operations.get(key, []):
                fields = set(request_class.model_fields)
                missing_query = [
                    param["name"]
                    for param in params
                    if is_parameter(param, "query")
                    and isinstance(param.get("name"), str)
                    and param["name"] not in fields
                    and python_field_name(param["name"]) not in fields
                ]
                if not missing_query:
                    continue
                has_custom_query_params = request_class.request_params is not EndpointRequest.request_params
                if has_custom_query_params or supports_generic_query_params(request_class):
                    continue
                gaps.append((module_name, class_name, path, openapi_route, missing_query))
    return gaps


def print_gap_details(label: str, gaps: Sequence[object]) -> None:
    if not gaps:
        return
    print(label)
    for gap in gaps:
        print(f"  {gap}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit implemented Metabase endpoint requests against OpenAPI.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OPENAPI_PATH,
        help=f"Path for the downloaded OpenAPI JSON document. Default: {DEFAULT_OPENAPI_PATH}",
    )
    parser.add_argument("--details", action="store_true", help="Print gap details when the audit fails.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    openapi_path: Path = args.output
    download_openapi_document_from_env(openapi_path)
    document = json.loads(openapi_path.read_text(encoding="utf-8"))

    openapi_operations = load_openapi_operations(document)
    implemented_operations = load_implemented_operations()
    missing = sorted(set(openapi_operations) - set(implemented_operations))
    placeholders = placeholder_gaps(implemented_operations)
    bodies = request_body_gaps(openapi_operations, implemented_operations)
    queries = query_param_gaps(openapi_operations, implemented_operations)

    paths = document.get("paths", {})
    print("downloaded_openapi_bytes", openapi_path.stat().st_size)
    print("openapi_version", document.get("openapi"), document.get("info", {}).get("version"))
    print("openapi_paths", len(paths) if isinstance(paths, dict) else 0)
    print("openapi_operations", len(openapi_operations))
    print("implemented_unique_operations", len(implemented_operations))
    print("missing_openapi_operations", len(missing))
    print("placeholder_gaps", len(placeholders))
    print("request_body_gaps", len(bodies))
    print("query_param_gaps", len(queries))

    if args.details:
        print_gap_details("missing_openapi_operations", missing)
        print_gap_details("placeholder_gaps", placeholders)
        print_gap_details("request_body_gaps", bodies)
        print_gap_details("query_param_gaps", queries)

    if missing or placeholders or bodies or queries:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
