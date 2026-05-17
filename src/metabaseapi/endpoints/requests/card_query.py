from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.card import CardDashboardsResponse
from metabaseapi.endpoints.responses.card import CardParameterValuesResponse
from metabaseapi.endpoints.responses.card import CardQueryExportResponse
from metabaseapi.endpoints.responses.card import CardQueryMetadataResponse
from metabaseapi.endpoints.responses.card import CardQueryResponse
from metabaseapi.endpoints.responses.card import CardRemappingResponse
from metabaseapi.endpoints.responses.card import CardsDashboardsResponse
from metabaseapi.endpoints.responses.card import CardSeriesResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class PostCardPivotQueryRequest(EndpointRequest[CardQueryResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/pivot/{card-id}/query"
    response_model = CardQueryResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class CardParamsSearchRequest(EndpointRequest[CardParameterValuesResponse]):
    card_id: int | str
    param_key: str
    query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/search/{query}"
    response_model = CardParameterValuesResponse


class CardParamsValuesRequest(EndpointRequest[CardParameterValuesResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/values"
    response_model = CardParameterValuesResponse


class CardQueryRequest(EndpointRequest[CardQueryResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query"
    response_model = CardQueryResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class CardQueryExportRequest(EndpointRequest[CardQueryExportResponse]):
    card_id: int | str
    export_format: str
    body: dict[str, Any] = PydanticField(default_factory=dict)
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query/{export_format}"
    response_model = CardQueryExportResponse

    def request_body(self) -> JSONValue:
        return self.body or None

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class GetCardDashboardsRequest(EndpointRequest[CardDashboardsResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/dashboards"
    response_model = CardDashboardsResponse


class CardRemappingRequest(EndpointRequest[CardRemappingResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/remapping"
    response_model = CardRemappingResponse


class GetCardQueryMetadataRequest(EndpointRequest[CardQueryMetadataResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query_metadata"
    response_model = CardQueryMetadataResponse


class GetCardSeriesRequest(EndpointRequest[CardSeriesResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/series"
    response_model = CardSeriesResponse


class CardsDashboardsRequest(EndpointRequest[CardsDashboardsResponse]):
    card_ids: list[int | str]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/dashboards"
    response_model = CardsDashboardsResponse

    def request_body(self) -> JSONValue:
        return {"card_ids": self.card_ids}
