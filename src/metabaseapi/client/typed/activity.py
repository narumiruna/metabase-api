from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import ActivityItem
from metabaseapi.endpoints.requests.activity import CreateRecentRequest
from metabaseapi.endpoints.requests.activity import GetMostRecentlyViewedDashboardRequest
from metabaseapi.endpoints.requests.activity import ListPopularItemsRequest
from metabaseapi.endpoints.requests.activity import ListRecentsRequest
from metabaseapi.endpoints.requests.activity import ListRecentViewsRequest
from metabaseapi.endpoints.responses import ActivityMutationResponse
from metabaseapi.endpoints.responses import ListActivityItemsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def most_recently_viewed_dashboard_typed(client: MetabaseClient) -> ActivityItem:
    return await client.run(GetMostRecentlyViewedDashboardRequest())


async def list_popular_items_typed(client: MetabaseClient) -> ListActivityItemsResponse:
    return await client.run(ListPopularItemsRequest())


async def list_recent_views_typed(client: MetabaseClient) -> ListActivityItemsResponse:
    return await client.run(ListRecentViewsRequest())


async def list_recents_typed(client: MetabaseClient, *, context: str | None = None) -> ListActivityItemsResponse:
    return await client.run(ListRecentsRequest(context=context))


async def create_recent_typed(client: MetabaseClient, body: dict[str, object]) -> ActivityMutationResponse:
    return await client.run(CreateRecentRequest(body=body))


__all__ = [
    "create_recent_typed",
    "list_popular_items_typed",
    "list_recent_views_typed",
    "list_recents_typed",
    "most_recently_viewed_dashboard_typed",
]
