from __future__ import annotations

from typing import Any
from typing import ClassVar
from typing import cast

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_support_access_grant import EeSupportAccessGrantResponse
from metabaseapi.endpoints.responses.ee_support_access_grant import EeSupportAccessGrantsResponse
from metabaseapi.wire import QueryParamValue


class PostEeSupportAccessGrantRequest(EndpointRequest[EeSupportAccessGrantResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/support-access-grant"
    response_model = EeSupportAccessGrantResponse


class GetEeSupportAccessGrantRequest(EndpointRequest[EeSupportAccessGrantsResponse]):
    ticket_number: str | None = None
    status: str | None = None
    limit: int | None = None
    offset: int | None = None
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/support-access-grant"
    response_model = EeSupportAccessGrantsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.params)
        params.update(
            {
                key: cast("QueryParamValue", value)
                for key, value in (
                    ("ticket-number", self.ticket_number),
                    ("status", self.status),
                    ("limit", self.limit),
                    ("offset", self.offset),
                )
                if value is not None
            }
        )
        return params


class GetEeSupportAccessGrantCurrentRequest(EndpointRequest[EeSupportAccessGrantResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/support-access-grant/current"
    response_model = EeSupportAccessGrantResponse


class PutEeSupportAccessGrantIdRevokeRequest(EndpointRequest[EeSupportAccessGrantResponse]):
    grant_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/support-access-grant/{grant_id}/revoke"
    response_model = EeSupportAccessGrantResponse
