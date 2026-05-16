from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import ClassVar
from urllib.parse import urlsplit

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator

JSONValue = str | int | float | bool | None | list[object] | dict[str, object]


class APIRequestModel(BaseModel):
    endpoint_method: ClassVar[str] = ""
    endpoint_path: ClassVar[str] = ""

    method: str
    path: str
    params: dict[str, str | int | bool | float | None] = Field(default_factory=dict)
    body: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_method(cls, values: dict[str, Any]) -> dict[str, Any]:
        method = values.get("method")
        if isinstance(method, str):
            values["method"] = method.upper()
        return values


class APIResponseModel(BaseModel):
    endpoint_method: ClassVar[str] = ""
    endpoint_path: ClassVar[str] = ""

    status_code: int
    payload: JSONValue | None = None
    content_type: str | None = None


@dataclass(frozen=True)
class EndpointModels:
    request: type[APIRequestModel]
    response: type[APIResponseModel]


_SUPPORTED_METHODS = {"delete", "get", "post", "put", "patch"}


def _find_openapi_fixture() -> Path | None:
    candidates: list[Path] = [
        Path(__file__).resolve().parents[2] / "tests" / "fixtures" / "api.json",
        Path.cwd() / "tests" / "fixtures" / "api.json",
        Path(__file__).resolve().parent / "fixtures" / "api.json",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _load_openapi_endpoints() -> dict[str, list[str]]:
    fixture = _find_openapi_fixture()
    if fixture is None:
        return {}

    try:
        raw = fixture.read_text(encoding="utf-8")
        data = json.loads(raw)
    except OSError, json.JSONDecodeError:
        return {}

    methods: dict[str, list[str]] = {}
    for path, operations in data.get("paths", {}).items():
        if not isinstance(operations, dict):
            continue
        for method in operations:
            method_lower = str(method).lower()
            if method_lower not in _SUPPORTED_METHODS:
                continue
            methods.setdefault(method_lower, []).append(str(path))
    return methods


def _sanitize_token(value: str) -> str:
    token = "".join(ch if ch.isalnum() else "_" for ch in value.strip())
    token = re.sub(r"_+", "_", token)
    token = token.strip("_")
    if not token:
        return "segment"
    if token[0].isdecimal():
        token = f"N{token}"
    return token


def _sanitize_path_identifier(path: str) -> str:
    stripped = path.strip("/")
    if not stripped:
        return "root"
    parts = (_sanitize_token(part.replace("{", "_").replace("}", "")) for part in stripped.split("/") if part)
    safe = "_".join(parts)
    return safe or "root"


def _build_model_name(method: str, path: str, suffix: str) -> str:
    return f"{method.upper()}_{_sanitize_path_identifier(path)}_{suffix}"


def _build_request_model(method: str, path: str) -> type[APIRequestModel]:
    name = _build_model_name(method, path, "Request")
    return type(
        name,
        (APIRequestModel,),
        {
            "__module__": __name__,
            "__annotations__": {
                "endpoint_method": ClassVar[str],
                "endpoint_path": ClassVar[str],
            },
            "endpoint_method": method,
            "endpoint_path": path,
            "__doc__": f"Request model for {method} {path}",
        },
    )


def _build_response_model(method: str, path: str) -> type[APIResponseModel]:
    name = _build_model_name(method, path, "Response")
    return type(
        name,
        (APIResponseModel,),
        {
            "__module__": __name__,
            "__annotations__": {
                "endpoint_method": ClassVar[str],
                "endpoint_path": ClassVar[str],
            },
            "endpoint_method": method,
            "endpoint_path": path,
            "__doc__": f"Response model for {method} {path}",
        },
    )


def _normalize_request_path(path: str) -> str:
    parsed = urlsplit(path)
    return parsed.path or "/"


def _path_segments(path: str) -> tuple[str, ...]:
    cleaned = path.strip("/")
    if not cleaned:
        return ()
    return tuple(segment for segment in cleaned.split("/") if segment)


def _is_template_segment(segment: str) -> bool:
    return segment.startswith("{") and segment.endswith("}")


def _template_matches(template_path: str, concrete_path: str) -> bool:
    template_segments = _path_segments(template_path)
    concrete_segments = _path_segments(concrete_path)
    if len(template_segments) != len(concrete_segments):
        return False

    for idx in range(len(template_segments)):
        template_segment = template_segments[idx]
        concrete_segment = concrete_segments[idx]
        if _is_template_segment(template_segment):
            continue
        if template_segment != concrete_segment:
            return False
    return True


def _build_endpoint_registry() -> tuple[dict[str, list[str]], dict[tuple[str, str], EndpointModels]]:
    raw_endpoints = _load_openapi_endpoints()
    method_paths: dict[str, list[str]] = {}
    registry: dict[tuple[str, str], EndpointModels] = {}

    for method, paths in raw_endpoints.items():
        method_upper = method.upper()
        unique_paths = sorted(set(paths))
        method_paths[method_upper] = unique_paths
        for path in unique_paths:
            normalized_path = _normalize_request_path(path)
            registry[(method_upper, normalized_path)] = EndpointModels(
                request=_build_request_model(method_upper, normalized_path),
                response=_build_response_model(method_upper, normalized_path),
            )

    return method_paths, registry


_ENDPOINT_PATHS_BY_METHOD, _ENDPOINT_MODELS = _build_endpoint_registry()


def iter_openapi_endpoints() -> list[tuple[str, str]]:
    return [(method, path) for method, paths in _ENDPOINT_PATHS_BY_METHOD.items() for path in paths]


def resolve_endpoint_path(method: str, path: str) -> str | None:
    method_upper = method.upper()
    normalized_path = _normalize_request_path(path)

    direct_key = (method_upper, normalized_path)
    if direct_key in _ENDPOINT_MODELS:
        return normalized_path

    for candidate in _ENDPOINT_PATHS_BY_METHOD.get(method_upper, []):
        if _template_matches(candidate, normalized_path):
            return candidate
    return None


def get_request_model(method: str, path: str) -> type[APIRequestModel]:
    template_path = resolve_endpoint_path(method, path)
    if template_path is None:
        return APIRequestModel
    return _ENDPOINT_MODELS[(method.upper(), template_path)].request


def get_response_model(method: str, path: str) -> type[APIResponseModel]:
    template_path = resolve_endpoint_path(method, path)
    if template_path is None:
        return APIResponseModel
    return _ENDPOINT_MODELS[(method.upper(), template_path)].response
