from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_collections(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection")


async def create_collection(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/collection", body=dict(body))


async def get_collection(client: MetabaseClient, collection_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/collection/{collection_id}")


async def update_collection(
    client: MetabaseClient, collection_id: int | str, body: dict[str, object]
) -> JSONValue | None:
    return await client.put(f"/api/collection/{collection_id}", body=dict(body))


async def delete_collection(client: MetabaseClient, collection_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/collection/{collection_id}")


async def get_collection_dashboard_question_candidates(
    client: MetabaseClient,
    collection_id: int | str,
) -> JSONValue | None:
    return await client.get(f"/api/collection/{collection_id}/dashboard-question-candidates")


async def get_collection_items(client: MetabaseClient, collection_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/collection/{collection_id}/items")


async def post_collection_move_dashboard_question_candidates(
    client: MetabaseClient,
    collection_id: int | str,
    body: dict[str, object],
) -> JSONValue | None:
    return await client.post(f"/api/collection/{collection_id}/move-dashboard-question-candidates", body=dict(body))


async def get_collection_trash(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection/trash")


async def get_collection_tree(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection/tree")


__all__ = [
    "create_collection",
    "delete_collection",
    "get_collection",
    "get_collection_dashboard_question_candidates",
    "get_collection_items",
    "get_collection_trash",
    "get_collection_tree",
    "list_collections",
    "post_collection_move_dashboard_question_candidates",
    "update_collection",
]
