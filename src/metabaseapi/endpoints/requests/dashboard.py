from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.dashboard import CreateDashboardPublicLinkResponse
from metabaseapi.endpoints.responses.dashboard import DashboardEmbeddableResponse
from metabaseapi.endpoints.responses.dashboard import DashboardItemsResponse
from metabaseapi.endpoints.responses.dashboard import DashboardPublicResponse
from metabaseapi.endpoints.responses.dashboard import DeleteDashboardPublicLinkResponse
from metabaseapi.endpoints.responses.dashboard import DeleteDashboardResponse
from metabaseapi.endpoints.responses.dashboard import ListDashboardsResponse
from metabaseapi.endpoints.responses.dashboard import SaveDashboardResponse
from metabaseapi.endpoints.responses.dashboard import SaveDashboardToCollectionResponse
from metabaseapi.endpoints.responses.dashboard import UpdateDashboardCardsResponse


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


class GetDashboardEmbeddableRequest(EndpointRequest[DashboardEmbeddableResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/embeddable"
    response_model = DashboardEmbeddableResponse


class GetDashboardPublicRequest(EndpointRequest[DashboardPublicResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/public"
    response_model = DashboardPublicResponse


class SaveDashboardRequest(EndpointRequest[SaveDashboardResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save"
    response_model = SaveDashboardResponse


class SaveDashboardToCollectionRequest(EndpointRequest[SaveDashboardToCollectionResponse]):
    parent_collection_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save/collection/{parent_collection_id}"
    response_model = SaveDashboardToCollectionResponse


class CreateDashboardPublicLinkRequest(EndpointRequest[CreateDashboardPublicLinkResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/public_link"
    response_model = CreateDashboardPublicLinkResponse


class DeleteDashboardPublicLinkRequest(EndpointRequest[DeleteDashboardPublicLinkResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/public_link"
    response_model = DeleteDashboardPublicLinkResponse


class CopyDashboardRequest(EndpointRequest[Dashboard]):
    from_dashboard_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{from_dashboard_id}/copy"
    response_model = Dashboard


class DeleteDashboardRequest(EndpointRequest[DeleteDashboardResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}"
    response_model = DeleteDashboardResponse


class UpdateDashboardRequest(EndpointRequest[Dashboard]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}"
    response_model = Dashboard


class UpdateDashboardCardsRequest(EndpointRequest[UpdateDashboardCardsResponse]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/cards"
    response_model = UpdateDashboardCardsResponse


class GetDashboardItemsRequest(EndpointRequest[DashboardItemsResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard_id}/items"
    response_model = DashboardItemsResponse
