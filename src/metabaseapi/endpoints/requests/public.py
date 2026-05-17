from __future__ import annotations

from typing import Any
from typing import ClassVar
from typing import cast

from pydantic import BaseModel
from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.public import PublicActionExecutionResponse
from metabaseapi.endpoints.responses.public import PublicActionResponse
from metabaseapi.endpoints.responses.public import PublicCardQueryResponse
from metabaseapi.endpoints.responses.public import PublicCardResponse
from metabaseapi.endpoints.responses.public import PublicDashboardCardResponse
from metabaseapi.endpoints.responses.public import PublicDashboardExecuteResponse
from metabaseapi.endpoints.responses.public import PublicDashboardResponse
from metabaseapi.endpoints.responses.public import PublicDocumentCardResponse
from metabaseapi.endpoints.responses.public import PublicDocumentResponse
from metabaseapi.endpoints.responses.public import PublicExportResponse
from metabaseapi.endpoints.responses.public import PublicOEmbedResponse
from metabaseapi.endpoints.responses.public import PublicParameterValuesResponse
from metabaseapi.endpoints.responses.public import PublicRemappingResponse
from metabaseapi.endpoints.responses.public import PublicTileResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class _PublicQueryParamsEndpoint[ResponseT: BaseModel](EndpointRequest[ResponseT]):
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    def request_params(self) -> dict[str, QueryParamValue]:
        return cast("dict[str, QueryParamValue]", self.parameters)


class GetPublicActionRequest(EndpointRequest[PublicActionResponse]):
    uuid: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/action/{uuid}"
    response_model = PublicActionResponse


class ExecutePublicActionRequest(EndpointRequest[PublicActionExecutionResponse]):
    uuid: str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/public/action/{uuid}/execute"
    response_model = PublicActionExecutionResponse

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class GetPublicCardRequest(_PublicQueryParamsEndpoint[PublicCardResponse]):
    uuid: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/card/{uuid}"
    response_model = PublicCardResponse


class GetPublicCardParamRemappingRequest(_PublicQueryParamsEndpoint[PublicRemappingResponse]):
    uuid: str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/card/{uuid}/params/{param_key}/remapping"
    response_model = PublicRemappingResponse


class GetPublicCardParamSearchRequest(_PublicQueryParamsEndpoint[PublicParameterValuesResponse]):
    uuid: str
    param_key: str
    query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/card/{uuid}/params/{param_key}/search/{query}"
    response_model = PublicParameterValuesResponse


class GetPublicCardParamValuesRequest(_PublicQueryParamsEndpoint[PublicParameterValuesResponse]):
    uuid: str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/card/{uuid}/params/{param_key}/values"
    response_model = PublicParameterValuesResponse


class GetPublicCardQueryRequest(_PublicQueryParamsEndpoint[PublicCardQueryResponse]):
    uuid: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/card/{uuid}/query"
    response_model = PublicCardQueryResponse


class GetPublicCardQueryExportRequest(_PublicQueryParamsEndpoint[PublicExportResponse]):
    uuid: str
    export_format: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/card/{uuid}/query/{export_format}"
    response_model = PublicExportResponse


class GetPublicDashboardRequest(_PublicQueryParamsEndpoint[PublicDashboardResponse]):
    uuid: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}"
    response_model = PublicDashboardResponse


class GetPublicDashboardCardRequest(_PublicQueryParamsEndpoint[PublicDashboardCardResponse]):
    uuid: str
    dashcard_id: int | str
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/dashcard/{dashcard_id}/card/{card_id}"
    response_model = PublicDashboardCardResponse


class ExportPublicDashboardCardRequest(EndpointRequest[PublicExportResponse]):
    uuid: str
    dashcard_id: int | str
    card_id: int | str
    export_format: str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/dashcard/{dashcard_id}/card/{card_id}/{export_format}"
    response_model = PublicExportResponse


class GetPublicDashboardDashcardExecuteRequest(
    _PublicQueryParamsEndpoint[PublicDashboardExecuteResponse],
):
    uuid: str
    dashcard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/dashcard/{dashcard_id}/execute"
    response_model = PublicDashboardExecuteResponse


class ExecutePublicDashboardDashcardRequest(EndpointRequest[PublicDashboardExecuteResponse]):
    uuid: str
    dashcard_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/dashcard/{dashcard_id}/execute"
    response_model = PublicDashboardExecuteResponse

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class GetPublicDashboardParamRemappingRequest(_PublicQueryParamsEndpoint[PublicRemappingResponse]):
    uuid: str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/params/{param_key}/remapping"
    response_model = PublicRemappingResponse


class GetPublicDashboardParamSearchRequest(_PublicQueryParamsEndpoint[PublicParameterValuesResponse]):
    uuid: str
    param_key: str
    query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/params/{param_key}/search/{query}"
    response_model = PublicParameterValuesResponse


class GetPublicDashboardParamValuesRequest(_PublicQueryParamsEndpoint[PublicParameterValuesResponse]):
    uuid: str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/dashboard/{uuid}/params/{param_key}/values"
    response_model = PublicParameterValuesResponse


class GetPublicDocumentRequest(EndpointRequest[PublicDocumentResponse]):
    uuid: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/document/{uuid}"
    response_model = PublicDocumentResponse


class GetPublicDocumentCardRequest(_PublicQueryParamsEndpoint[PublicDocumentCardResponse]):
    uuid: str
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/document/{uuid}/card/{card_id}"
    response_model = PublicDocumentCardResponse


class ExportPublicDocumentCardRequest(EndpointRequest[PublicExportResponse]):
    uuid: str
    card_id: int | str
    export_format: str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/public/document/{uuid}/card/{card_id}/{export_format}"
    response_model = PublicExportResponse


class GetPublicOEmbedRequest(_PublicQueryParamsEndpoint[PublicOEmbedResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/oembed"
    response_model = PublicOEmbedResponse


class GetPublicPivotCardQueryRequest(_PublicQueryParamsEndpoint[PublicCardQueryResponse]):
    uuid: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/pivot/card/{uuid}/query"
    response_model = PublicCardQueryResponse


class GetPublicPivotDashboardCardRequest(_PublicQueryParamsEndpoint[PublicDashboardCardResponse]):
    uuid: str
    dashcard_id: int | str
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/pivot/dashboard/{uuid}/dashcard/{dashcard_id}/card/{card_id}"
    response_model = PublicDashboardCardResponse


class GetPublicCardTileRequest(_PublicQueryParamsEndpoint[PublicTileResponse]):
    uuid: str
    zoom: int | str
    x: int | str
    y: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/public/tiles/card/{uuid}/{zoom}/{x}/{y}"
    response_model = PublicTileResponse


class GetPublicDashboardCardTileRequest(_PublicQueryParamsEndpoint[PublicTileResponse]):
    uuid: str
    dashcard_id: int | str
    card_id: int | str
    zoom: int | str
    x: int | str
    y: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/public/tiles/dashboard/{uuid}/dashcard/{dashcard_id}/card/{card_id}/{zoom}/{x}/{y}"
    )
    response_model = PublicTileResponse
