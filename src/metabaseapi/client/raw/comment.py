from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_comment(
    client: MetabaseClient,
    *,
    model: str | None = None,
    model_id: int | str | None = None,
) -> JSONValue | None:
    params: dict[str, QueryParamValue] = {}
    if model is not None:
        params["model"] = model
    if model_id is not None:
        params["model-id"] = model_id
    return await client.get("/api/comment", params=params or None)


async def get_comment_mentions(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/comment/mentions")


async def create_comment(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/comment", body=dict(body))


async def update_comment(client: MetabaseClient, comment_id: int | str, body: dict[str, object]) -> JSONValue | None:
    return await client.put(f"/api/comment/{comment_id}", body=dict(body))


async def post_comment_reaction(
    client: MetabaseClient, comment_id: int | str, body: dict[str, object]
) -> JSONValue | None:
    return await client.post(f"/api/comment/{comment_id}/reaction", body=dict(body))


async def delete_comment(client: MetabaseClient, comment_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/comment/{comment_id}")


__all__ = [
    "create_comment",
    "delete_comment",
    "get_comment",
    "get_comment_mentions",
    "post_comment_reaction",
    "update_comment",
]
