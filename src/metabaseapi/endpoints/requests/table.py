from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Table
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.table import ListTablesResponse
from metabaseapi.endpoints.responses.table import TableDataResponse
from metabaseapi.endpoints.responses.table import TableForeignKeysResponse
from metabaseapi.endpoints.responses.table import TableOperationResponse
from metabaseapi.endpoints.responses.table import TableQueryMetadataResponse
from metabaseapi.endpoints.responses.table import TableRelatedResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class ListTablesRequest(EndpointRequest[ListTablesResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table"
    response_model = ListTablesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class UpdateTablesRequest(EndpointRequest[TableOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/table"
    response_model = TableOperationResponse


class GetTableRequest(EndpointRequest[Table]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}"
    response_model = Table


class UpdateTableRequest(EndpointRequest[Table]):
    table_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}"
    response_model = Table


class AppendTableCsvRequest(EndpointRequest[TableOperationResponse]):
    table_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/append-csv"
    response_model = TableOperationResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DiscardTableValuesRequest(EndpointRequest[TableOperationResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/discard_values"
    response_model = TableOperationResponse


class UpdateTableFieldsOrderRequest(EndpointRequest[TableOperationResponse]):
    table_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/fields/order"
    response_model = TableOperationResponse


class GetTableForeignKeysRequest(EndpointRequest[TableForeignKeysResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/fks"
    response_model = TableForeignKeysResponse


class GetCardTableForeignKeysRequest(EndpointRequest[TableForeignKeysResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/card__{card_id}/fks"
    response_model = TableForeignKeysResponse


class GetTableQueryMetadataRequest(EndpointRequest[TableQueryMetadataResponse]):
    table_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/query_metadata"
    response_model = TableQueryMetadataResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetCardTableQueryMetadataRequest(EndpointRequest[TableQueryMetadataResponse]):
    card_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/card__{card_id}/query_metadata"
    response_model = TableQueryMetadataResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetTableRelatedRequest(EndpointRequest[TableRelatedResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/related"
    response_model = TableRelatedResponse


class ReplaceTableCsvRequest(EndpointRequest[TableOperationResponse]):
    table_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/replace-csv"
    response_model = TableOperationResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class RescanTableValuesRequest(EndpointRequest[TableOperationResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/rescan_values"
    response_model = TableOperationResponse


class SyncTableSchemaRequest(EndpointRequest[TableOperationResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/sync_schema"
    response_model = TableOperationResponse


class GetTableDataRequest(EndpointRequest[TableDataResponse]):
    table_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}/data"
    response_model = TableDataResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params
