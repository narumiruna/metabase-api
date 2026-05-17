from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_tables(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/table")


async def get_table(client: MetabaseClient, table_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/table/{table_id}")


async def get_field(client: MetabaseClient, field_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/field/{field_id}")


__all__ = [
    "get_field",
    "get_table",
    "list_tables",
]
