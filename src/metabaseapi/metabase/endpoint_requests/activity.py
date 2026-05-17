from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.metabase.entities import ActivityItem
from metabaseapi.metabase.request_base import MetabaseRequestClient
from metabaseapi.metabase.request_base import _BaseMetabaseRequest
from metabaseapi.metabase.responses import ActivityMutationResponse
from metabaseapi.metabase.responses import ListActivityItemsResponse
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue


class GetMostRecentlyViewedDashboardRequest(_BaseMetabaseRequest[ActivityItem]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/most_recently_viewed_dashboard"

    async def do(self, client: MetabaseRequestClient) -> ActivityItem:
        return await self.execute(client, ActivityItem)

    def do_sync(self, client: MetabaseRequestClient) -> ActivityItem:
        return self.execute_sync(client, ActivityItem)


class ListPopularItemsRequest(_BaseMetabaseRequest[ListActivityItemsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/popular_items"

    async def do(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return await self.execute(client, ListActivityItemsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return self.execute_sync(client, ListActivityItemsResponse)


class ListRecentViewsRequest(_BaseMetabaseRequest[ListActivityItemsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/recent_views"

    async def do(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return await self.execute(client, ListActivityItemsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return self.execute_sync(client, ListActivityItemsResponse)


class ListRecentsRequest(_BaseMetabaseRequest[ListActivityItemsResponse]):
    context: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/recents"

    async def do(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return await self.execute(client, ListActivityItemsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return self.execute_sync(client, ListActivityItemsResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.context is None:
            return {}
        return {"context": self.context}


class CreateRecentRequest(_BaseMetabaseRequest[ActivityMutationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/activity/recents"

    async def do(self, client: MetabaseRequestClient) -> ActivityMutationResponse:
        return await self.execute(client, ActivityMutationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActivityMutationResponse:
        return self.execute_sync(client, ActivityMutationResponse)

    def request_body(self) -> JSONValue:
        return self.body
