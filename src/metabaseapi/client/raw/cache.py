from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_cache(
    client: MetabaseClient,
    *,
    limit: int | None = None,
    offset: int | None = None,
    sort_column: str | None = None,
    sort_direction: str | None = None,
) -> JSONValue | None:
    params = {
        "limit": limit,
        "offset": offset,
        "sort_column": sort_column,
        "sort_direction": sort_direction,
    }
    filtered_params = {key: value for key, value in params.items() if value is not None}
    return await client.get("/api/cache", params=filtered_params)


async def put_cache(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.put("/api/cache", body=dict(body))


async def delete_cache(client: MetabaseClient, body: Mapping[str, object] | None = None) -> JSONValue | None:
    if body is None:
        return await client.delete("/api/cache")
    return await client.delete("/api/cache", body=dict(body))


async def invalidate_cache(client: MetabaseClient, params: Mapping[str, QueryParamValue]) -> JSONValue | None:
    return await client.post("/api/cache/invalidate", params=dict(params))


__all__ = [
    "delete_cache",
    "get_cache",
    "invalidate_cache",
    "put_cache",
]
