from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_channels(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/channel")


async def create_channel(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/channel", body=dict(body))


async def test_channel(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/channel/test", body=dict(body))


async def get_channel(client: MetabaseClient, channel_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/channel/{channel_id}")


async def update_channel(client: MetabaseClient, channel_id: int | str, body: dict[str, object]) -> JSONValue | None:
    return await client.put(f"/api/channel/{channel_id}", body=dict(body))


__all__ = [
    "create_channel",
    "get_channel",
    "list_channels",
    "test_channel",
    "update_channel",
]
