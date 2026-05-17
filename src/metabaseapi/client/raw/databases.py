from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for database endpoints."""

    async def list_databases(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/database")

    async def create_database(
        self: MetabaseClient,
        *,
        name: str,
        engine: str,
        details: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {"name": name, "engine": engine}
        if details is not None:
            body["details"] = dict(details)
        return await self.post("/api/database", body=body)

    async def get_database(self: MetabaseClient, database_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/database/{database_id}")


__all__ = ["_MetabaseClientRawMixin"]
