from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.data_studio import DataStudioTableDiscardValuesRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableEditRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableRescanValuesRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableSelectionRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableSyncSchemaRequest
from metabaseapi.endpoints.responses import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def data_studio_table_discard_values_typed(
    client: MetabaseClient, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(DataStudioTableDiscardValuesRequest(body=body))


async def data_studio_table_edit_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(DataStudioTableEditRequest(body=body))


async def data_studio_table_rescan_values_typed(
    client: MetabaseClient, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(DataStudioTableRescanValuesRequest(body=body))


async def data_studio_table_selection_typed(
    client: MetabaseClient, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(DataStudioTableSelectionRequest(body=body))


async def data_studio_table_sync_schema_typed(
    client: MetabaseClient, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(DataStudioTableSyncSchemaRequest(body=body))


__all__ = [
    "data_studio_table_discard_values_typed",
    "data_studio_table_edit_typed",
    "data_studio_table_rescan_values_typed",
    "data_studio_table_selection_typed",
    "data_studio_table_sync_schema_typed",
]
