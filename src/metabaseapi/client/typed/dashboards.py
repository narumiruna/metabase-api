from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import CopyDashboardRequest
from metabaseapi.metabase import CreateDashboardPublicLinkRequest
from metabaseapi.metabase import Dashboard
from metabaseapi.metabase import DashboardParamRemappingRequest
from metabaseapi.metabase import DashboardParamSearchRequest
from metabaseapi.metabase import DashboardParamValuesRequest
from metabaseapi.metabase import DeleteDashboardPublicLinkRequest
from metabaseapi.metabase import DeleteDashboardRequest
from metabaseapi.metabase import ExecuteDashboardDashcardRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetDashboardDashcardExecuteRequest
from metabaseapi.metabase import GetDashboardEmbeddableRequest
from metabaseapi.metabase import GetDashboardItemsRequest
from metabaseapi.metabase import GetDashboardPublicRequest
from metabaseapi.metabase import GetDashboardQueryMetadataRequest
from metabaseapi.metabase import GetDashboardRelatedRequest
from metabaseapi.metabase import GetDashboardRequest
from metabaseapi.metabase import ListDashboardsRequest
from metabaseapi.metabase import ListDashboardsResponse
from metabaseapi.metabase import PostDashboardPivotQueryRequest
from metabaseapi.metabase import PostDashboardRequest
from metabaseapi.metabase import SaveDashboardRequest
from metabaseapi.metabase import SaveDashboardToCollectionRequest
from metabaseapi.metabase import UpdateDashboardCardsRequest
from metabaseapi.metabase import UpdateDashboardRequest
from metabaseapi.models import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for dashboard endpoints."""

    async def create_dashboard_typed(self: MetabaseClient, body: dict[str, object]) -> Dashboard:
        return await self.run(PostDashboardRequest(body=dict(body)))

    async def list_dashboards_typed(self: MetabaseClient) -> ListDashboardsResponse:
        return await self.run(ListDashboardsRequest())

    async def get_dashboard_typed(self: MetabaseClient, dashboard_id: int | str) -> Dashboard:
        return await self.run(GetDashboardRequest(dashboard_id=dashboard_id))

    async def get_dashboard_embeddable_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetDashboardEmbeddableRequest())

    async def get_dashboard_public_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetDashboardPublicRequest())

    async def query_dashboard_card_pivot_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            PostDashboardPivotQueryRequest(
                dashboard_id=dashboard_id,
                dashcard_id=dashcard_id,
                card_id=card_id,
                body=body,
            )
        )

    async def save_dashboard_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(SaveDashboardRequest(body=body))

    async def save_dashboard_to_collection_typed(
        self: MetabaseClient,
        parent_collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(SaveDashboardToCollectionRequest(parent_collection_id=parent_collection_id, body=body))

    async def get_dashboard_dashcard_execute_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            GetDashboardDashcardExecuteRequest(
                dashboard_id=dashboard_id,
                dashcard_id=dashcard_id,
                parameters=parameters or {},
            )
        )

    async def execute_dashboard_dashcard_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            ExecuteDashboardDashcardRequest(
                dashboard_id=dashboard_id,
                dashcard_id=dashcard_id,
                parameters=parameters or {},
            )
        )

    async def create_dashboard_public_link_typed(
        self: MetabaseClient, dashboard_id: int | str
    ) -> GenericOperationResponse:
        return await self.run(CreateDashboardPublicLinkRequest(dashboard_id=dashboard_id))

    async def delete_dashboard_public_link_typed(
        self: MetabaseClient, dashboard_id: int | str
    ) -> GenericOperationResponse:
        return await self.run(DeleteDashboardPublicLinkRequest(dashboard_id=dashboard_id))

    async def copy_dashboard_typed(
        self: MetabaseClient,
        from_dashboard_id: int | str,
        body: dict[str, object] | None = None,
    ) -> Dashboard:
        return await self.run(CopyDashboardRequest(from_dashboard_id=from_dashboard_id, body=body))

    async def delete_dashboard_typed(self: MetabaseClient, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteDashboardRequest(dashboard_id=dashboard_id))

    async def update_dashboard_typed(
        self: MetabaseClient, dashboard_id: int | str, body: dict[str, object]
    ) -> Dashboard:
        return await self.run(UpdateDashboardRequest(dashboard_id=dashboard_id, body=body))

    async def update_dashboard_cards_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(UpdateDashboardCardsRequest(dashboard_id=dashboard_id, body=body))

    async def get_dashboard_items_typed(self: MetabaseClient, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(GetDashboardItemsRequest(dashboard_id=dashboard_id))

    async def get_dashboard_param_remapping_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            DashboardParamRemappingRequest(
                dashboard_id=dashboard_id,
                param_key=param_key,
                parameters=parameters or {},
            )
        )

    async def get_dashboard_param_search_values_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        param_key: str,
        query: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            DashboardParamSearchRequest(
                dashboard_id=dashboard_id,
                param_key=param_key,
                query=query,
                parameters=parameters or {},
            )
        )

    async def get_dashboard_param_values_typed(
        self: MetabaseClient,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            DashboardParamValuesRequest(
                dashboard_id=dashboard_id,
                param_key=param_key,
                parameters=parameters or {},
            )
        )

    async def get_dashboard_query_metadata_typed(
        self: MetabaseClient, dashboard_id: int | str
    ) -> GenericOperationResponse:
        return await self.run(GetDashboardQueryMetadataRequest(dashboard_id=dashboard_id))

    async def get_dashboard_related_typed(self: MetabaseClient, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(GetDashboardRelatedRequest(dashboard_id=dashboard_id))


__all__ = ["_MetabaseClientTypedMixin"]
