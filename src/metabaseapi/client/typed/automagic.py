from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import AutomagicDashboardRequest
from metabaseapi.metabase import AutomagicDatabaseCandidatesRequest
from metabaseapi.metabase import AutomagicModelIndexPrimaryKeyRequest
from metabaseapi.metabase import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for automagic endpoints."""

    async def automagic_database_candidates_typed(
        self: MetabaseClient, database_id: int | str
    ) -> GenericOperationResponse:
        return await self.run(AutomagicDatabaseCandidatesRequest(database_id=database_id))

    async def automagic_model_index_primary_key_typed(
        self: MetabaseClient,
        model_index_id: int | str,
        primary_key_id: int | str,
    ) -> GenericOperationResponse:
        return await self.run(
            AutomagicModelIndexPrimaryKeyRequest(model_index_id=model_index_id, primary_key_id=primary_key_id),
        )

    async def automagic_dashboard_path_typed(self: MetabaseClient, path: str) -> GenericOperationResponse:
        return await self.run(AutomagicDashboardRequest(path=path))


__all__ = ["_MetabaseClientTypedMixin"]
