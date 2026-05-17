from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_bookmarks(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/bookmark")


async def update_bookmark_ordering(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.put("/api/bookmark/ordering", body=dict(body))


async def create_bookmark(client: MetabaseClient, model: str, item_id: int | str) -> JSONValue | None:
    return await client.post(f"/api/bookmark/{model}/{item_id}")


async def delete_bookmark(client: MetabaseClient, model: str, item_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/bookmark/{model}/{item_id}")


__all__ = [
    "create_bookmark",
    "delete_bookmark",
    "list_bookmarks",
    "update_bookmark_ordering",
]
