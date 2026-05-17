from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import CancelCloudMigrationRequest
from metabaseapi.metabase import CreateCloudMigrationRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetCloudMigrationRequest

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for cloud migration endpoints."""

    async def create_cloud_migration_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(CreateCloudMigrationRequest(body=body))

    async def get_cloud_migration_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCloudMigrationRequest())

    async def cancel_cloud_migration_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(CancelCloudMigrationRequest())


__all__ = ["_MetabaseClientTypedMixin"]
