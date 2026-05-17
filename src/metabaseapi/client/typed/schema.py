from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.entities import Table
from metabaseapi.endpoints.requests.schema import GetFieldRequest
from metabaseapi.endpoints.requests.schema import GetTableRequest
from metabaseapi.endpoints.requests.schema import ListTablesRequest
from metabaseapi.endpoints.responses import ListTablesResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_tables_typed(client: MetabaseClient) -> ListTablesResponse:
    return await client.run(ListTablesRequest())


async def get_table_typed(client: MetabaseClient, table_id: int | str) -> Table:
    return await client.run(GetTableRequest(table_id=table_id))


async def get_field_typed(client: MetabaseClient, field_id: int | str) -> MetabaseField:
    return await client.run(GetFieldRequest(field_id=field_id))


__all__ = [
    "get_field_typed",
    "get_table_typed",
    "list_tables_typed",
]
