from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for Data Studio endpoints."""

    async def data_studio_table_discard_values(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/discard-values", body=dict(body))

    async def data_studio_table_edit(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/edit", body=dict(body))

    async def data_studio_table_rescan_values(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/rescan-values", body=dict(body))

    async def data_studio_table_selection(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/selection", body=dict(body))

    async def data_studio_table_sync_schema(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/sync-schema", body=dict(body))


__all__ = ["_MetabaseClientRawMixin"]
