from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def most_recently_viewed_dashboard(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/activity/most_recently_viewed_dashboard")


async def list_popular_items(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/activity/popular_items")


async def list_recent_views(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/activity/recent_views")


async def list_recents(client: MetabaseClient, *, context: str | None = None) -> JSONValue | None:
    params = {"context": context} if context is not None else None
    return await client.get("/api/activity/recents", params=params)


async def create_recent(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/activity/recents", body=dict(body))


__all__ = [
    "create_recent",
    "list_popular_items",
    "list_recent_views",
    "list_recents",
    "most_recently_viewed_dashboard",
]
