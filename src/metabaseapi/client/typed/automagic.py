from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.automagic import AutomagicDashboardRequest
from metabaseapi.endpoints.requests.automagic import AutomagicDatabaseCandidatesRequest
from metabaseapi.endpoints.requests.automagic import AutomagicModelIndexPrimaryKeyRequest
from metabaseapi.endpoints.responses import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def automagic_database_candidates_typed(
    client: MetabaseClient, database_id: int | str
) -> GenericOperationResponse:
    return await client.run(AutomagicDatabaseCandidatesRequest(database_id=database_id))


async def automagic_model_index_primary_key_typed(
    client: MetabaseClient,
    model_index_id: int | str,
    primary_key_id: int | str,
) -> GenericOperationResponse:
    return await client.run(
        AutomagicModelIndexPrimaryKeyRequest(model_index_id=model_index_id, primary_key_id=primary_key_id),
    )


async def automagic_dashboard_path_typed(client: MetabaseClient, path: str) -> GenericOperationResponse:
    return await client.run(AutomagicDashboardRequest(path=path))


__all__ = [
    "automagic_dashboard_path_typed",
    "automagic_database_candidates_typed",
    "automagic_model_index_primary_key_typed",
]
