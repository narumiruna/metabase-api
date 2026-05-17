from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for bug-reporting endpoints."""

    async def bug_reporting_connection_pool_details(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/bug-reporting/connection-pool-details")

    async def bug_reporting_details(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/bug-reporting/details")


__all__ = ["_MetabaseClientRawMixin"]
