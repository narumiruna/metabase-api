from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.entities import Table
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.table import ListTablesResponse


class ListTablesRequest(EndpointRequest[ListTablesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table"
    response_model: ClassVar[object] = ListTablesResponse


class GetTableRequest(EndpointRequest[Table]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}"
    response_model: ClassVar[object] = Table

    def resolve_path(self) -> str:
        return f"/api/table/{self.table_id}"
