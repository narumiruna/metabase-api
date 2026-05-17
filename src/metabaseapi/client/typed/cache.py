from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.cache import DeleteCacheRequest
from metabaseapi.endpoints.requests.cache import GetCacheRequest
from metabaseapi.endpoints.requests.cache import InvalidateCacheRequest
from metabaseapi.endpoints.requests.cache import PutCacheRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def get_cache_typed(
    client: MetabaseClient,
    *,
    limit: int | None = None,
    offset: int | None = None,
    sort_column: str | None = None,
    sort_direction: str | None = None,
) -> GenericOperationResponse:
    return await client.run(
        GetCacheRequest(
            limit=limit,
            offset=offset,
            sort_column=sort_column,
            sort_direction=sort_direction,
        ),
    )


async def put_cache_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(PutCacheRequest(body=body))


async def delete_cache_typed(
    client: MetabaseClient,
    body: dict[str, object] | None = None,
) -> GenericOperationResponse:
    return await client.run(DeleteCacheRequest(body=body or {}))


async def invalidate_cache_typed(
    client: MetabaseClient, params: dict[str, QueryParamValue]
) -> GenericOperationResponse:
    return await client.run(InvalidateCacheRequest(params=dict(params)))


__all__ = [
    "delete_cache_typed",
    "get_cache_typed",
    "invalidate_cache_typed",
    "put_cache_typed",
]
