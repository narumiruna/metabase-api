from __future__ import annotations

import ast
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SUPPORTED_METHODS = {"DELETE", "GET", "POST", "PUT", "PATCH"}


@dataclass(frozen=True)
class EndpointCoverage:
    method: str
    path: str
    operation_id: str | None
    has_body: bool
    has_params: bool
    expected_convenience: str | None
    is_convenience_covered: bool


def resolve_openapi_fixture() -> Path:
    cwd = Path.cwd()
    candidates = [
        cwd / "tests" / "fixtures" / "api.json",
        cwd / "api.json",
        Path(__file__).resolve().parents[2] / "tests" / "fixtures" / "api.json",
        Path(__file__).resolve().parents[2] / "api.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    msg = "Unable to locate tests/fixtures/api.json"
    raise FileNotFoundError(msg)


def load_endpoints(spec_path: Path) -> list[EndpointCoverage]:
    raw = json.loads(spec_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return []

    operations = raw.get("paths", {})
    if not isinstance(operations, dict):
        return []

    client_methods = discover_convenience_methods(Path("src/metabaseapi/client.py"))
    cli_commands = discover_cli_commands(Path("src/metabaseapi/cli.py"))
    covered_methods = set(client_methods) | set(cli_commands)

    rows: list[EndpointCoverage] = []
    for path, method_definitions in operations.items():
        if not isinstance(method_definitions, dict):
            continue
        for method, spec in method_definitions.items():
            method_upper = str(method).upper()
            if method_upper not in SUPPORTED_METHODS:
                continue

            operation_id = None
            has_body = False
            has_params = False
            if isinstance(spec, dict):
                raw_operation_id = spec.get("operationId")
                operation_id = str(raw_operation_id) if isinstance(raw_operation_id, str) else None
                has_body = isinstance(spec.get("requestBody"), dict)
                has_params = isinstance(spec.get("parameters"), list)

            if not isinstance(path, str):
                continue

            candidate = infer_convenience(method_upper, path)
            is_covered = candidate in covered_methods if candidate else True

            rows.append(
                EndpointCoverage(
                    method=method_upper,
                    path=path,
                    operation_id=operation_id,
                    has_body=has_body,
                    has_params=has_params,
                    expected_convenience=candidate,
                    is_convenience_covered=is_covered,
                ),
            )

    return rows


def infer_convenience(method: str, path: str) -> str | None:
    normalized = path.strip("/")
    if not normalized:
        return None

    parts = [segment for segment in normalized.split("/") if segment]
    if not (len(parts) >= 2 and parts[0] == "api"):
        return None

    resource = parts[1]
    resource_singular = resource[:-1] if resource.endswith("s") and len(resource) > 1 else resource

    if len(parts) == 2:
        return _infer_collection_convenience(resource, method)

    if len(parts) == 3 and is_template(parts[2]):
        return _infer_item_convenience(resource_singular, method)

    return None


def _infer_collection_convenience(resource: str, method: str) -> str | None:
    if method == "GET":
        return f"list_{resource}"
    if method in {"POST", "PUT"}:
        return f"create_{resource}"
    return None


def _infer_item_convenience(resource: str, method: str) -> str | None:
    if method == "GET":
        return f"get_{resource}"
    if method == "PUT":
        return f"update_{resource}"
    if method == "DELETE":
        return f"delete_{resource}"
    return None


def is_template(segment: str) -> bool:
    return segment.startswith("{") and segment.endswith("}") and len(segment) > 2


def discover_convenience_methods(file_path: Path) -> set[str]:
    tree = ast.parse(file_path.read_text(encoding="utf-8"))
    methods: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "MetabaseClient":
            for method in node.body:
                if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)) and method.name not in {
                    "__aenter__",
                    "__aexit__",
                    "close",
                    "request",
                    "get",
                    "post",
                    "put",
                    "patch",
                    "delete",
                    "_request_url",
                    "_decode_response_payload",
                    "from_settings",
                }:
                    methods.add(method.name)
            break
    return methods


def discover_cli_commands(file_path: Path) -> set[str]:
    tree = ast.parse(file_path.read_text(encoding="utf-8"))
    commands: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if not isinstance(decorator, ast.Call):
                    continue
                func = decorator.func
                if isinstance(func, ast.Attribute) and func.attr == "command":
                    if (
                        decorator.args
                        and isinstance(decorator.args[0], ast.Constant)
                        and isinstance(
                            decorator.args[0].value,
                            str,
                        )
                    ):
                        commands.add(decorator.args[0].value)
                    elif isinstance(decorator.keywords, list):
                        commands.add(node.name.replace("_", "-"))
    return commands


def coverage_summary(endpoints: list[EndpointCoverage]) -> dict[str, Any]:
    method_counts: dict[str, int] = {}
    missing_by_resource: dict[str, int] = {}
    for item in endpoints:
        method_counts[item.method] = method_counts.get(item.method, 0) + 1
        if not item.is_convenience_covered:
            path_parts = item.path.split("/")
            prefix = path_parts[2] if item.path.startswith("/api/") and len(path_parts) > 2 else "(root)"
            missing_by_resource[prefix] = missing_by_resource.get(prefix, 0) + 1
    return {
        "total": len(endpoints),
        "method_counts": dict(sorted(method_counts.items())),
        "missing": len([item for item in endpoints if not item.is_convenience_covered]),
        "missing_by_resource": dict(sorted(missing_by_resource.items(), key=lambda item: item[1], reverse=True)),
    }


def to_markdown(endpoints: list[EndpointCoverage]) -> str:
    summary = coverage_summary(endpoints)
    lines = [
        "# OpenAPI Coverage Snapshot",
        "",
        f"- total endpoints: {summary['total']}",
        f"- convenience coverage: {summary['total'] - summary['missing']}/{summary['total']}",
        "",
        "## Method Counts",
        "",
        "| method | count |",
        "|---|---:|",
    ]
    for method, count in summary["method_counts"].items():
        lines.append(f"| {method} | {count} |")

    lines.extend(
        [
            "",
            "## Missing Convenience Candidates",
            "",
            "| method | path | operationId | hasBody | hasParams | expectedConvenience |",
            "|---|---|---|---:|---:|---|",
        ]
    )
    for item in endpoints:
        if item.is_convenience_covered:
            continue
        has_body = "Y" if item.has_body else "N"
        has_params = "Y" if item.has_params else "N"
        operation_id = item.operation_id or ""
        expected = item.expected_convenience or ""
        lines.append(f"| {item.method} | `{item.path}` | {operation_id} | {has_body} | {has_params} | `{expected}` |")

    return "\n".join(lines) + "\n"


def generate_report(spec_path: Path | None = None) -> tuple[dict[str, Any], list[EndpointCoverage]]:
    path = spec_path or resolve_openapi_fixture()
    endpoints = load_endpoints(path)
    return coverage_summary(endpoints), endpoints
