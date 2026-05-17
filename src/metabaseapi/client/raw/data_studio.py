from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def data_studio_table_discard_values(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/data-studio/table/discard-values", body=dict(body))


async def data_studio_table_edit(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/data-studio/table/edit", body=dict(body))


async def data_studio_table_rescan_values(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/data-studio/table/rescan-values", body=dict(body))


async def data_studio_table_selection(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/data-studio/table/selection", body=dict(body))


async def data_studio_table_sync_schema(client: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
    return await client.post("/api/data-studio/table/sync-schema", body=dict(body))


__all__ = [
    "data_studio_table_discard_values",
    "data_studio_table_edit",
    "data_studio_table_rescan_values",
    "data_studio_table_selection",
    "data_studio_table_sync_schema",
]
