from __future__ import annotations

from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedCardParamRemappingResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedCardParamValuesResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedCardQueryResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedCardResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedDashboardDashcardCardResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedDashboardParamRemappingResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedDashboardParamSearchResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedDashboardParamValuesResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedDashboardResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedPivotCardQueryResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedPivotDashboardDashcardCardResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedTilesCardResponse
from metabaseapi.endpoints.responses.preview_embed import GetPreviewEmbedTilesDashboardDashcardCardResponse
from metabaseapi.wire import QueryParamValue


class _PreviewEmbedParamsMixin:
    parameters: dict[str, QueryParamValue]

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class GetPreviewEmbedCardRequest(EndpointRequest[GetPreviewEmbedCardResponse]):
    token: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/card/{token}"
    response_model = GetPreviewEmbedCardResponse


class GetPreviewEmbedCardParamRemappingRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedCardParamRemappingResponse],
):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/card/{token}/params/{param_key}/remapping"
    response_model = GetPreviewEmbedCardParamRemappingResponse


class GetPreviewEmbedCardParamValuesRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedCardParamValuesResponse],
):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/card/{token}/params/{param_key}/values"
    response_model = GetPreviewEmbedCardParamValuesResponse


class GetPreviewEmbedCardQueryRequest(_PreviewEmbedParamsMixin, EndpointRequest[GetPreviewEmbedCardQueryResponse]):
    token: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/card/{token}/query"
    response_model = GetPreviewEmbedCardQueryResponse


class GetPreviewEmbedDashboardRequest(EndpointRequest[GetPreviewEmbedDashboardResponse]):
    token: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/dashboard/{token}"
    response_model = GetPreviewEmbedDashboardResponse


class GetPreviewEmbedDashboardDashcardCardRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedDashboardDashcardCardResponse],
):
    token: str
    dashcard_id: int | str
    card_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}"
    response_model = GetPreviewEmbedDashboardDashcardCardResponse


class GetPreviewEmbedDashboardParamRemappingRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedDashboardParamRemappingResponse],
):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/dashboard/{token}/params/{param_key}/remapping"
    response_model = GetPreviewEmbedDashboardParamRemappingResponse


class GetPreviewEmbedDashboardParamSearchRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedDashboardParamSearchResponse],
):
    token: str
    param_key: str
    prefix: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/dashboard/{token}/params/{param_key}/search/{prefix}"
    response_model = GetPreviewEmbedDashboardParamSearchResponse


class GetPreviewEmbedDashboardParamValuesRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedDashboardParamValuesResponse],
):
    token: str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/dashboard/{token}/params/{param_key}/values"
    response_model = GetPreviewEmbedDashboardParamValuesResponse


class GetPreviewEmbedPivotCardQueryRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedPivotCardQueryResponse],
):
    token: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/pivot/card/{token}/query"
    response_model = GetPreviewEmbedPivotCardQueryResponse


class GetPreviewEmbedPivotDashboardDashcardCardRequest(
    _PreviewEmbedParamsMixin,
    EndpointRequest[GetPreviewEmbedPivotDashboardDashcardCardResponse],
):
    token: str
    dashcard_id: int | str
    card_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/pivot/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}"
    response_model = GetPreviewEmbedPivotDashboardDashcardCardResponse


class GetPreviewEmbedTilesCardRequest(EndpointRequest[GetPreviewEmbedTilesCardResponse]):
    token: str
    zoom: int
    x: int
    y: int

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/preview_embed/tiles/card/{token}/{zoom}/{x}/{y}"
    response_model = GetPreviewEmbedTilesCardResponse


class GetPreviewEmbedTilesDashboardDashcardCardRequest(
    EndpointRequest[GetPreviewEmbedTilesDashboardDashcardCardResponse],
):
    token: str
    dashcard_id: int | str
    card_id: int | str
    zoom: int
    x: int
    y: int

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/preview_embed/tiles/dashboard/{token}/dashcard/{dashcard_id}/card/{card_id}/{zoom}/{x}/{y}"
    )
    response_model = GetPreviewEmbedTilesDashboardDashcardCardResponse
