from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import DataStudioTableDiscardValuesRequest
from metabaseapi.metabase import DataStudioTableEditRequest
from metabaseapi.metabase import DataStudioTableRescanValuesRequest
from metabaseapi.metabase import DataStudioTableSelectionRequest
from metabaseapi.metabase import DataStudioTableSyncSchemaRequest
from metabaseapi.metabase import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for miscellaneous endpoints."""

    async def data_studio_table_discard_values_typed(
        self: MetabaseClient, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(DataStudioTableDiscardValuesRequest(body=body))

    async def data_studio_table_edit_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(DataStudioTableEditRequest(body=body))

    async def data_studio_table_rescan_values_typed(
        self: MetabaseClient, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(DataStudioTableRescanValuesRequest(body=body))

    async def data_studio_table_selection_typed(
        self: MetabaseClient, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(DataStudioTableSelectionRequest(body=body))

    async def data_studio_table_sync_schema_typed(
        self: MetabaseClient, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(DataStudioTableSyncSchemaRequest(body=body))


__all__ = ["_MetabaseClientTypedMixin"]
