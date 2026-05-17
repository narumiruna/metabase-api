from __future__ import annotations

from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.embed import GetEmbedCardParamRemappingResponse
from metabaseapi.endpoints.responses.embed import GetEmbedCardParamSearchResponse
from metabaseapi.endpoints.responses.embed import GetEmbedCardParamValuesResponse
from metabaseapi.endpoints.responses.embed import GetEmbedCardQueryExportResponse
from metabaseapi.endpoints.responses.embed import GetEmbedCardQueryResponse
from metabaseapi.endpoints.responses.embed import GetEmbedCardResponse
from metabaseapi.endpoints.responses.embed import GetEmbedDashboardDashcardCardExportResponse
from metabaseapi.endpoints.responses.embed import GetEmbedDashboardDashcardCardResponse
from metabaseapi.endpoints.responses.embed import GetEmbedDashboardParamRemappingResponse
from metabaseapi.endpoints.responses.embed import GetEmbedDashboardParamSearchResponse
from metabaseapi.endpoints.responses.embed import GetEmbedDashboardParamValuesResponse
from metabaseapi.endpoints.responses.embed import GetEmbedDashboardResponse
from metabaseapi.endpoints.responses.embed import GetEmbedPivotCardQueryResponse
from metabaseapi.endpoints.responses.embed import GetEmbedPivotDashboardDashcardCardResponse
from metabaseapi.endpoints.responses.embed import GetEmbedTilesCardResponse
from metabaseapi.endpoints.responses.embed import GetEmbedTilesDashboardDashcardCardResponse
from metabaseapi.wire import QueryParamValue


class _EmbedParamsMixin:
    parameters: dict[str, QueryParamValue]

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class GetEmbedCardRequest(EndpointRequest[GetEmbedCardResponse]):
    token: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/card/{token}"
    response_model = GetEmbedCardResponse


class GetEmbedCardParamRemappingRequest(
    _EmbedParamsMixin,
    EndpointRequest[GetEmbedCardParamRemappingResponse],
):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/card/{token}/params/{param_key}/remapping"
    response_model = GetEmbedCardParamRemappingResponse


class GetEmbedCardParamSearchRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedCardParamSearchResponse]):
    token: str
    param_key: str
    prefix: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/card/{token}/params/{param_key}/search/{prefix}"
    response_model = GetEmbedCardParamSearchResponse


class GetEmbedCardParamValuesRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedCardParamValuesResponse]):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/card/{token}/params/{param_key}/values"
    response_model = GetEmbedCardParamValuesResponse


class GetEmbedCardQueryRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedCardQueryResponse]):
    token: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/card/{token}/query"
    response_model = GetEmbedCardQueryResponse


class GetEmbedCardQueryExportRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedCardQueryExportResponse]):
    token: str
    export_format: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/card/{token}/query/{export_format}"
    response_model = GetEmbedCardQueryExportResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.parameters)
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class GetEmbedDashboardRequest(EndpointRequest[GetEmbedDashboardResponse]):
    token: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/dashboard/{token}"
    response_model = GetEmbedDashboardResponse


class GetEmbedDashboardDashcardCardRequest(
    _EmbedParamsMixin,
    EndpointRequest[GetEmbedDashboardDashcardCardResponse],
):
    token: str
    dashcard_id: int | str
    card_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}"
    response_model = GetEmbedDashboardDashcardCardResponse


class GetEmbedDashboardDashcardCardExportRequest(
    _EmbedParamsMixin,
    EndpointRequest[GetEmbedDashboardDashcardCardExportResponse],
):
    token: str
    dashcard_id: int | str
    card_id: int | str
    export_format: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}/{export_format}"
    response_model = GetEmbedDashboardDashcardCardExportResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.parameters)
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class GetEmbedDashboardParamRemappingRequest(
    _EmbedParamsMixin,
    EndpointRequest[GetEmbedDashboardParamRemappingResponse],
):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/dashboard/{token}/params/{param_key}/remapping"
    response_model = GetEmbedDashboardParamRemappingResponse


class GetEmbedDashboardParamSearchRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedDashboardParamSearchResponse]):
    token: str
    param_key: str
    prefix: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/dashboard/{token}/params/{param_key}/search/{prefix}"
    response_model = GetEmbedDashboardParamSearchResponse


class GetEmbedDashboardParamValuesRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedDashboardParamValuesResponse]):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/dashboard/{token}/params/{param_key}/values"
    response_model = GetEmbedDashboardParamValuesResponse


class GetEmbedPivotCardQueryRequest(_EmbedParamsMixin, EndpointRequest[GetEmbedPivotCardQueryResponse]):
    token: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/pivot/card/{token}/query"
    response_model = GetEmbedPivotCardQueryResponse


class GetEmbedPivotDashboardDashcardCardRequest(
    _EmbedParamsMixin,
    EndpointRequest[GetEmbedPivotDashboardDashcardCardResponse],
):
    token: str
    dashcard_id: int | str
    card_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/pivot/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}"
    response_model = GetEmbedPivotDashboardDashcardCardResponse


class GetEmbedTilesCardRequest(EndpointRequest[GetEmbedTilesCardResponse]):
    token: str
    zoom: int
    x: int
    y: int

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed/tiles/card/{token}/{zoom}/{x}/{y}"
    response_model = GetEmbedTilesCardResponse


class GetEmbedTilesDashboardDashcardCardRequest(EndpointRequest[GetEmbedTilesDashboardDashcardCardResponse]):
    token: str
    dashcard_id: int | str
    card_id: int | str
    zoom: int
    x: int
    y: int

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/embed/tiles/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}/{zoom}/{x}/{y}"
    )
    response_model = GetEmbedTilesDashboardDashcardCardResponse
