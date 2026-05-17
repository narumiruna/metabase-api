from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for channel endpoints."""

    async def list_channels(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/channel")

    async def create_channel(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/channel", body=dict(body))

    async def test_channel(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/channel/test", body=dict(body))

    async def get_channel(self: MetabaseClient, channel_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/channel/{channel_id}")

    async def update_channel(self: MetabaseClient, channel_id: int | str, body: dict[str, object]) -> JSONValue | None:
        return await self.put(f"/api/channel/{channel_id}", body=dict(body))


__all__ = ["_MetabaseClientRawMixin"]
