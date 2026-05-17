from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_library import EeLibraryResponse
from metabaseapi.endpoints.responses.ee_library import EeLibraryTreeResponse


class CreateEeLibraryRequest(EndpointRequest[EeLibraryResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/library"
    response_model = EeLibraryResponse


class GetEeLibraryRequest(EndpointRequest[EeLibraryResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/library"
    response_model = EeLibraryResponse


class GetEeLibraryTreeRequest(EndpointRequest[EeLibraryTreeResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/library/tree"
    response_model = EeLibraryTreeResponse
