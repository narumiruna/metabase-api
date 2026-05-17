from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for table endpoints."""

    async def list_tables(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/table")

    async def get_table(self: MetabaseClient, table_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/table/{table_id}")

    async def get_field(self: MetabaseClient, field_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/field/{field_id}")


__all__ = ["_MetabaseClientRawMixin"]
