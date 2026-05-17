from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.endpoints.responses.dashboard import ListDashboardsResponse


class ListDashboardsRequest(EndpointRequest[ListDashboardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard"
    response_model = ListDashboardsResponse


class PostDashboardRequest(EndpointRequest[Dashboard]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard"
    response_model = Dashboard


class GetDashboardRequest(EndpointRequest[Dashboard]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}"
    response_model = Dashboard


class GetDashboardEmbeddableRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/embeddable"
    response_model = GenericOperationResponse


class GetDashboardPublicRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/public"
    response_model = GenericOperationResponse


class SaveDashboardRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save"
    response_model = GenericOperationResponse


class SaveDashboardToCollectionRequest(EndpointRequest[GenericOperationResponse]):
    parent_collection_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save/collection/{parent_collection_id}"
    response_model = GenericOperationResponse


class CreateDashboardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/public_link"
    response_model = GenericOperationResponse


class DeleteDashboardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/public_link"
    response_model = GenericOperationResponse


class CopyDashboardRequest(EndpointRequest[Dashboard]):
    from_dashboard_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{from_dashboard_id}/copy"
    response_model = Dashboard


class DeleteDashboardRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}"
    response_model = GenericOperationResponse


class UpdateDashboardRequest(EndpointRequest[Dashboard]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}"
    response_model = Dashboard


class UpdateDashboardCardsRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/cards"
    response_model = GenericOperationResponse


class GetDashboardItemsRequest(EndpointRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/items"
    response_model = GenericOperationResponse
