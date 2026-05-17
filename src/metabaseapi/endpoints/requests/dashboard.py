from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.execution import _BaseMetabaseRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListDashboardsResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class ListDashboardsRequest(_BaseMetabaseRequest[ListDashboardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard"

    async def do(self, client: MetabaseRequestClient) -> ListDashboardsResponse:
        return await self.execute(client, ListDashboardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListDashboardsResponse:
        return self.execute_sync(client, ListDashboardsResponse)


class PostDashboardRequest(_BaseMetabaseRequest[Dashboard]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard"

    async def do(self, client: MetabaseRequestClient) -> Dashboard:
        return await self.execute(client, Dashboard)

    def do_sync(self, client: MetabaseRequestClient) -> Dashboard:
        return self.execute_sync(client, Dashboard)

    def request_body(self) -> JSONValue:
        return self.body


class GetDashboardRequest(_BaseMetabaseRequest[Dashboard]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}"

    async def do(self, client: MetabaseRequestClient) -> Dashboard:
        return await self.execute(client, Dashboard)

    def do_sync(self, client: MetabaseRequestClient) -> Dashboard:
        return self.execute_sync(client, Dashboard)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"


class GetDashboardEmbeddableRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/embeddable"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetDashboardPublicRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/public"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class PostDashboardPivotQueryRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    card_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/pivot/{dashboard-id}/dashcard/{dashcard-id}/card/{card-id}/query"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/pivot/{self.dashboard_id}/dashcard/{self.dashcard_id}/card/{self.card_id}/query"

    def request_body(self) -> JSONValue | None:
        return self.body


class SaveDashboardRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class SaveDashboardToCollectionRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    parent_collection_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/save/collection/{parent-collection-id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/save/collection/{self.parent_collection_id}"

    def request_body(self) -> JSONValue:
        return self.body


class GetDashboardDashcardExecuteRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/execute"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class ExecuteDashboardDashcardRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/dashcard/{dashcard-id}/execute"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/dashcard/{self.dashcard_id}/execute"

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class CreateDashboardPublicLinkRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/public_link"


class DeleteDashboardPublicLinkRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/public_link"


class CopyDashboardRequest(_BaseMetabaseRequest[Dashboard]):
    from_dashboard_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dashboard/{from-dashboard-id}/copy"

    async def do(self, client: MetabaseRequestClient) -> Dashboard:
        return await self.execute(client, Dashboard)

    def do_sync(self, client: MetabaseRequestClient) -> Dashboard:
        return self.execute_sync(client, Dashboard)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.from_dashboard_id}/copy"

    def request_body(self) -> JSONValue | None:
        return self.body


class DeleteDashboardRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"


class UpdateDashboardRequest(_BaseMetabaseRequest[Dashboard]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}"

    async def do(self, client: MetabaseRequestClient) -> Dashboard:
        return await self.execute(client, Dashboard)

    def do_sync(self, client: MetabaseRequestClient) -> Dashboard:
        return self.execute_sync(client, Dashboard)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"

    def request_body(self) -> JSONValue:
        return self.body


class UpdateDashboardCardsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/cards"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/cards"

    def request_body(self) -> JSONValue:
        return self.body


class GetDashboardItemsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/items"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/items"


class DashboardParamRemappingRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/remapping"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/remapping"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class DashboardParamSearchRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    query: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/search/{query}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/search/{self.query}"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class DashboardParamValuesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str
    param_key: str
    parameters: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/params/{param-key}/values"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/params/{self.param_key}/values"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class GetDashboardQueryMetadataRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/query_metadata"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/query_metadata"


class GetDashboardRelatedRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{id}/related"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}/related"
