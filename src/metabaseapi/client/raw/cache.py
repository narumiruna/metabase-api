from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for cache endpoints."""

    async def get_cache(
        self: MetabaseClient,
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
        return await self.get("/api/cache", params=filtered_params)

    async def put_cache(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put("/api/cache", body=dict(body))

    async def delete_cache(self: MetabaseClient, body: Mapping[str, object] | None = None) -> JSONValue | None:
        if body is None:
            return await self.delete("/api/cache")
        return await self.delete("/api/cache", body=dict(body))

    async def invalidate_cache(self: MetabaseClient, params: Mapping[str, QueryParamValue]) -> JSONValue | None:
        return await self.post("/api/cache/invalidate", params=dict(params))


__all__ = ["_MetabaseClientRawMixin"]
