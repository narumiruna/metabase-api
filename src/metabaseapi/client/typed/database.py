from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.requests.database import CreateDatabaseRequest
from metabaseapi.endpoints.requests.database import GetDatabaseRequest
from metabaseapi.endpoints.requests.database import ListDatabasesRequest
from metabaseapi.endpoints.responses import ListDatabasesResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_databases_typed(client: MetabaseClient) -> ListDatabasesResponse:
    return await client.run(ListDatabasesRequest())


async def create_database_typed(
    client: MetabaseClient,
    *,
    name: str,
    engine: str,
    details: dict[str, object] | None = None,
) -> Database:
    request = CreateDatabaseRequest(name=name, engine=engine, details=details or {})
    return await client.run(request)


async def get_database_typed(client: MetabaseClient, database_id: int | str) -> Database:
    return await client.run(GetDatabaseRequest(database_id=database_id))


__all__ = [
    "create_database_typed",
    "get_database_typed",
    "list_databases_typed",
]
