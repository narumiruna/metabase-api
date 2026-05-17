from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for activity endpoints."""

    async def most_recently_viewed_dashboard(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/activity/most_recently_viewed_dashboard")

    async def list_popular_items(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/activity/popular_items")

    async def list_recent_views(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/activity/recent_views")

    async def list_recents(self: MetabaseClient, *, context: str | None = None) -> JSONValue | None:
        params = {"context": context} if context is not None else None
        return await self.get("/api/activity/recents", params=params)

    async def create_recent(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/activity/recents", body=dict(body))


__all__ = ["_MetabaseClientRawMixin"]
