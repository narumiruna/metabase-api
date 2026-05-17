from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def create_cloud_migration(client: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
    return await client.post("/api/cloud-migration", body=dict(body))


async def get_cloud_migration(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/cloud-migration")


async def cancel_cloud_migration(client: MetabaseClient) -> JSONValue | None:
    return await client.put("/api/cloud-migration/cancel")


__all__ = [
    "cancel_cloud_migration",
    "create_cloud_migration",
    "get_cloud_migration",
]
