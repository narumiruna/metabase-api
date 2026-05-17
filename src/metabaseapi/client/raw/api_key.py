from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for API key endpoints."""

    async def create_api_key(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/api-key", body=dict(body))

    async def list_api_keys(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/api-key")

    async def count_api_keys(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/api-key/count")

    async def update_api_key(self: MetabaseClient, api_key_id: int | str, body: dict[str, object]) -> JSONValue | None:
        return await self.put(f"/api/api-key/{api_key_id}", body=dict(body))

    async def delete_api_key(self: MetabaseClient, api_key_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/api-key/{api_key_id}")

    async def regenerate_api_key(self: MetabaseClient, api_key_id: int | str) -> JSONValue | None:
        return await self.put(f"/api/api-key/{api_key_id}/regenerate")


__all__ = ["_MetabaseClientRawMixin"]
