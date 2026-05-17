from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import CreateDatabaseRequest
from metabaseapi.metabase import Database
from metabaseapi.metabase import GetDatabaseRequest
from metabaseapi.metabase import ListDatabasesRequest
from metabaseapi.metabase import ListDatabasesResponse

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for database endpoints."""

    async def list_databases_typed(self: MetabaseClient) -> ListDatabasesResponse:
        return await self.run(ListDatabasesRequest())

    async def create_database_typed(
        self: MetabaseClient,
        *,
        name: str,
        engine: str,
        details: dict[str, object] | None = None,
    ) -> Database:
        request = CreateDatabaseRequest(name=name, engine=engine, details=details or {})
        return await self.run(request)

    async def get_database_typed(self: MetabaseClient, database_id: int | str) -> Database:
        return await self.run(GetDatabaseRequest(database_id=database_id))


__all__ = ["_MetabaseClientTypedMixin"]
