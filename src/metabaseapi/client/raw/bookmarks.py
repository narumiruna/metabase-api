from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for bookmark endpoints."""

    async def list_bookmarks(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/bookmark")

    async def update_bookmark_ordering(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.put("/api/bookmark/ordering", body=dict(body))

    async def create_bookmark(self: MetabaseClient, model: str, item_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/bookmark/{model}/{item_id}")

    async def delete_bookmark(self: MetabaseClient, model: str, item_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/bookmark/{model}/{item_id}")


__all__ = ["_MetabaseClientRawMixin"]
