from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_databases(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/database")


async def create_database(
    client: MetabaseClient,
    *,
    name: str,
    engine: str,
    details: Mapping[str, object] | None = None,
) -> JSONValue | None:
    body: dict[str, object] = {"name": name, "engine": engine}
    if details is not None:
        body["details"] = dict(details)
    return await client.post("/api/database", body=body)


async def get_database(client: MetabaseClient, database_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/database/{database_id}")


__all__ = [
    "create_database",
    "get_database",
    "list_databases",
]
