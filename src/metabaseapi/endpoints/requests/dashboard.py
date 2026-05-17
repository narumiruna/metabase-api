from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import ResponseModel
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.endpoints.responses.dashboard import ListDashboardsResponse
from metabaseapi.wire import JSONValue


class ListDashboardsRequest(EndpointRequest[ListDashboardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard"
    response_model: ClassVar[ResponseModel] = ListDashboardsResponse


class PostDashboardRequest(EndpointRequest[Dashboard]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard"
    response_model: ClassVar[ResponseModel] = Dashboard

    def request_body(self) -> JSONValue:
        return self.body


class GetDashboardRequest(EndpointRequest[Dashboard]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}"
    response_model: ClassVar[ResponseModel] = Dashboard

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"


class GetDashboardEmbeddableRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/embeddable"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse


class GetDashboardPublicRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/public"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse


class SaveDashboardRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body


class SaveDashboardToCollectionRequest(EndpointRequest[GenericOperationResponse]):
    parent_collection_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save/collection/{parent-collection-id}"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/save/collection/{self.parent_collection_id}"

    def request_body(self) -> JSONValue:
        return self.body


class CreateDashboardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/public_link"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/public_link"


class DeleteDashboardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/public_link"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/public_link"


class CopyDashboardRequest(EndpointRequest[Dashboard]):
    from_dashboard_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{from-dashboard-id}/copy"
    response_model: ClassVar[ResponseModel] = Dashboard

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.from_dashboard_id}/copy"

    def request_body(self) -> JSONValue | None:
        return self.body


class DeleteDashboardRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"


class UpdateDashboardRequest(EndpointRequest[Dashboard]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}"
    response_model: ClassVar[ResponseModel] = Dashboard

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"

    def request_body(self) -> JSONValue:
        return self.body


class UpdateDashboardCardsRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/cards"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/cards"

    def request_body(self) -> JSONValue:
        return self.body


class GetDashboardItemsRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/items"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/items"
