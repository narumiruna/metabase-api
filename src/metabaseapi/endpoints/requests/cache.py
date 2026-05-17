from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class GetCacheRequest(EndpointRequest[GenericOperationResponse]):
    limit: int | None = None
    offset: int | None = None
    sort_column: str | None = None
    sort_direction: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/cache"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.sort_column is not None:
            params["sort_column"] = self.sort_column
        if self.sort_direction is not None:
            params["sort_direction"] = self.sort_direction
        return params


class PutCacheRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/cache"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCacheRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/cache"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class InvalidateCacheRequest(EndpointRequest[GenericOperationResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cache/invalidate"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return dict(self.params)
