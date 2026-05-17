from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_collection_graph(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/collection/graph")


async def put_collection_graph(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.put("/api/collection/graph", body=dict(body))


__all__ = [
    "get_collection_graph",
    "put_collection_graph",
]
