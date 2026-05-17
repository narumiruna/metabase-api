from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import DeleteCacheRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetCacheRequest
from metabaseapi.metabase import InvalidateCacheRequest
from metabaseapi.metabase import PutCacheRequest
from metabaseapi.models import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for cache endpoints."""

    async def get_cache_typed(
        self: MetabaseClient,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sort_column: str | None = None,
        sort_direction: str | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            GetCacheRequest(
                limit=limit,
                offset=offset,
                sort_column=sort_column,
                sort_direction=sort_direction,
            ),
        )

    async def put_cache_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(PutCacheRequest(body=body))

    async def delete_cache_typed(
        self: MetabaseClient,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(DeleteCacheRequest(body=body or {}))

    async def invalidate_cache_typed(
        self: MetabaseClient, params: dict[str, QueryParamValue]
    ) -> GenericOperationResponse:
        return await self.run(InvalidateCacheRequest(params=dict(params)))


__all__ = ["_MetabaseClientTypedMixin"]
