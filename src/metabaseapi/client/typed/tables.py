from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import GetFieldRequest
from metabaseapi.metabase import GetTableRequest
from metabaseapi.metabase import ListTablesRequest
from metabaseapi.metabase import ListTablesResponse
from metabaseapi.metabase import MetabaseField
from metabaseapi.metabase import Table

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for table endpoints."""

    async def list_tables_typed(self: MetabaseClient) -> ListTablesResponse:
        return await self.run(ListTablesRequest())

    async def get_table_typed(self: MetabaseClient, table_id: int | str) -> Table:
        return await self.run(GetTableRequest(table_id=table_id))

    async def get_field_typed(self: MetabaseClient, field_id: int | str) -> MetabaseField:
        return await self.run(GetFieldRequest(field_id=field_id))


__all__ = ["_MetabaseClientTypedMixin"]
