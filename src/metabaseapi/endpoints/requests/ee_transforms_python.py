from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_transforms_python import EeTransformsPythonLibraryResponse
from metabaseapi.endpoints.responses.ee_transforms_python import EeTransformsPythonTestRunResponse


class GetEeTransformsPythonLibraryPathRequest(EndpointRequest[EeTransformsPythonLibraryResponse]):
    path: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/transforms-python/library/{path}"
    response_model = EeTransformsPythonLibraryResponse


class PutEeTransformsPythonLibraryPathRequest(EndpointRequest[EeTransformsPythonLibraryResponse]):
    path: str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/transforms-python/library/{path}"
    response_model = EeTransformsPythonLibraryResponse


class PostEeTransformsPythonTestRunRequest(EndpointRequest[EeTransformsPythonTestRunResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/transforms-python/test-run"
    response_model = EeTransformsPythonTestRunResponse
