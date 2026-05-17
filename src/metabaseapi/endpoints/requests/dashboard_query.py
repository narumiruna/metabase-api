from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamPrimitive
from metabaseapi.wire import QueryParamValue


class DashboardParamsValidFilterFieldsRequest(EndpointRequest[GenericOperationResponse]):
    filtered: list[QueryParamPrimitive] | None = None
    filtering: list[QueryParamPrimitive] | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/params/valid-filter-fields"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.filtered is not None:
            params["filtered"] = self.filtered
        if self.filtering is not None:
            params["filtering"] = self.filtering
        return params


class DashboardCardQueryRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    card_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/card/{self.card_id}/query"


class DashboardCardQueryExportRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    card_id: int | str
    export_format: str
    body: dict[str, Any] | None = None
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = (
        "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query/{export-format}"
    )
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return (
            f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/card/"
            f"{self.card_id}/query/{self.export_format}"
        )

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class PostDashboardPivotQueryRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    card_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/pivot/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/pivot/{self.dashboard_id}/dashcard/{self.dashcard_id}/card/{self.card_id}/query"


class GetDashboardDashcardExecuteRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/execute"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class ExecuteDashboardDashcardRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/execute"

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class DashboardParamRemappingRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/remapping"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/remapping"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class DashboardParamSearchRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    query: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/search/{query}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/search/{self.query}"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class DashboardParamValuesRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/values"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/values"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class GetDashboardQueryMetadataRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/query_metadata"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/query_metadata"


class GetDashboardRelatedRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/related"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/related"
