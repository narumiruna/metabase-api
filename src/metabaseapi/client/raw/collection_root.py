from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_collection_root(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection/root")


async def get_collection_root_dashboard_question_candidates(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection/root/dashboard-question-candidates")


async def get_collection_root_items(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection/root/items")


async def post_collection_root_move_dashboard_question_candidates(
    client: MetabaseClient,
    body: dict[str, object],
) -> JSONValue | None:
    return await client.post("/api/collection/root/move-dashboard-question-candidates", body=dict(body))


__all__ = [
    "get_collection_root",
    "get_collection_root_dashboard_question_candidates",
    "get_collection_root_items",
    "post_collection_root_move_dashboard_question_candidates",
]
