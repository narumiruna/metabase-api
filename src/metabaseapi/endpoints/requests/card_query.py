from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.card import CardsDashboardsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class PostCardPivotQueryRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/pivot/{card-id}/query"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/pivot/{self.card_id}/query"

    def request_body(self) -> JSONValue:
        return self.body or None


class CardParamsSearchRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str
    query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/search/{query}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/search/{self.query}"


class CardParamsValuesRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/values"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/values"


class CardQueryRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query"

    def request_body(self) -> JSONValue:
        return self.body or None


class CardQueryExportRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    export_format: str
    body: dict[str, Any] = PydanticField(default_factory=dict)
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query/{export_format}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query/{self.export_format}"

    def request_body(self) -> JSONValue:
        return self.body or None

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class GetCardDashboardsRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/dashboards"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/dashboards"


class CardRemappingRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/remapping"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/remapping"


class GetCardQueryMetadataRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query_metadata"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query_metadata"


class GetCardSeriesRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/series"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/series"


class CardsDashboardsRequest(EndpointRequest[CardsDashboardsResponse]):
    card_ids: list[int | str]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/dashboards"
    response_model: ClassVar[object] = CardsDashboardsResponse

    def request_body(self) -> JSONValue:
        return {"card_ids": self.card_ids}
