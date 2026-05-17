from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_gsheets import EeGsheetsConnectionResponse
from metabaseapi.endpoints.responses.ee_gsheets import EeGsheetsDeleteConnectionResponse
from metabaseapi.endpoints.responses.ee_gsheets import EeGsheetsServiceAccountResponse


class CreateEeGsheetsConnectionRequest(EndpointRequest[EeGsheetsConnectionResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/gsheets/connection"
    response_model = EeGsheetsConnectionResponse


class GetEeGsheetsConnectionRequest(EndpointRequest[EeGsheetsConnectionResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/gsheets/connection"
    response_model = EeGsheetsConnectionResponse


class DeleteEeGsheetsConnectionRequest(EndpointRequest[EeGsheetsDeleteConnectionResponse]):
    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/gsheets/connection"
    response_model = EeGsheetsDeleteConnectionResponse


class SyncEeGsheetsConnectionRequest(EndpointRequest[EeGsheetsConnectionResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/gsheets/connection/sync"
    response_model = EeGsheetsConnectionResponse


class GetEeGsheetsServiceAccountRequest(EndpointRequest[EeGsheetsServiceAccountResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/gsheets/service-account"
    response_model = EeGsheetsServiceAccountResponse
