from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.cloud_migration import CancelCloudMigrationRequest
from metabaseapi.endpoints.requests.cloud_migration import CreateCloudMigrationRequest
from metabaseapi.endpoints.requests.cloud_migration import GetCloudMigrationRequest
from metabaseapi.endpoints.responses import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def create_cloud_migration_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(CreateCloudMigrationRequest(body=body))


async def get_cloud_migration_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCloudMigrationRequest())


async def cancel_cloud_migration_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(CancelCloudMigrationRequest())


__all__ = [
    "cancel_cloud_migration_typed",
    "create_cloud_migration_typed",
    "get_cloud_migration_typed",
]
