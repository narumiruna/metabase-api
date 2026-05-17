from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_serialization import EeSerializationExportResponse
from metabaseapi.endpoints.responses.ee_serialization import EeSerializationImportResponse
from metabaseapi.wire import JSONValue


class PostEeSerializationExportRequest(EndpointRequest[EeSerializationExportResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/serialization/export"
    response_model = EeSerializationExportResponse

    def request_body(self) -> JSONValue | None:
        return self.body or None


class PostEeSerializationImportRequest(EndpointRequest[EeSerializationImportResponse]):
    file_path: str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/serialization/import"
    response_model = EeSerializationImportResponse

    def request_body(self) -> JSONValue:
        return {"file": self.file_path, **self.body}
