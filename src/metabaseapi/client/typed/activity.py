from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import ActivityItem
from metabaseapi.metabase import ActivityMutationResponse
from metabaseapi.metabase import CreateRecentRequest
from metabaseapi.metabase import GetMostRecentlyViewedDashboardRequest
from metabaseapi.metabase import ListActivityItemsResponse
from metabaseapi.metabase import ListPopularItemsRequest
from metabaseapi.metabase import ListRecentsRequest
from metabaseapi.metabase import ListRecentViewsRequest

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for activity endpoints."""

    async def most_recently_viewed_dashboard_typed(self: MetabaseClient) -> ActivityItem:
        return await self.run(GetMostRecentlyViewedDashboardRequest())

    async def list_popular_items_typed(self: MetabaseClient) -> ListActivityItemsResponse:
        return await self.run(ListPopularItemsRequest())

    async def list_recent_views_typed(self: MetabaseClient) -> ListActivityItemsResponse:
        return await self.run(ListRecentViewsRequest())

    async def list_recents_typed(self: MetabaseClient, *, context: str | None = None) -> ListActivityItemsResponse:
        return await self.run(ListRecentsRequest(context=context))

    async def create_recent_typed(self: MetabaseClient, body: dict[str, object]) -> ActivityMutationResponse:
        return await self.run(CreateRecentRequest(body=body))


__all__ = ["_MetabaseClientTypedMixin"]
