from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for cloud migration endpoints."""

    async def create_cloud_migration(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/cloud-migration", body=dict(body))

    async def get_cloud_migration(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/cloud-migration")

    async def cancel_cloud_migration(self: MetabaseClient) -> JSONValue | None:
        return await self.put("/api/cloud-migration/cancel")


__all__ = ["_MetabaseClientRawMixin"]
