from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def bug_reporting_connection_pool_details(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/bug-reporting/connection-pool-details")


async def bug_reporting_details(client: MetabaseClient) -> JSONValue | None:
    return await client.get("/api/bug-reporting/details")


__all__ = [
    "bug_reporting_connection_pool_details",
    "bug_reporting_details",
]
