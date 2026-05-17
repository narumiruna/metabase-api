from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.database import DatabaseAutocompleteSuggestionsResponse
from metabaseapi.endpoints.responses.database import DatabaseCardAutocompleteSuggestionsResponse
from metabaseapi.endpoints.responses.database import DatabaseFieldsResponse
from metabaseapi.endpoints.responses.database import DatabaseFieldValuesResponse
from metabaseapi.endpoints.responses.database import DatabaseHealthcheckResponse
from metabaseapi.endpoints.responses.database import DatabaseMetadataResponse
from metabaseapi.endpoints.responses.database import DatabaseOperationResponse
from metabaseapi.endpoints.responses.database import DatabaseSchemasResponse
from metabaseapi.endpoints.responses.database import DatabaseSchemaTablesResponse
from metabaseapi.endpoints.responses.database import DatabaseSettingsAvailableResponse
from metabaseapi.endpoints.responses.database import DatabaseUsageInfoResponse
from metabaseapi.endpoints.responses.database import DeleteDatabaseResponse
from metabaseapi.endpoints.responses.database import ImportDatabaseMetadataResponse
from metabaseapi.endpoints.responses.database import ListDatabasesResponse
from metabaseapi.endpoints.responses.database import ValidateDatabaseResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class ListDatabasesRequest(EndpointRequest[ListDatabasesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database"
    response_model = ListDatabasesResponse


class CreateDatabaseRequest(EndpointRequest[Database]):
    name: str
    engine: str
    details: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database"
    response_model = Database

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetDatabaseRequest(EndpointRequest[Database]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}"
    response_model = Database


class UpdateDatabaseRequest(EndpointRequest[Database]):
    database_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}"
    response_model = Database


class DeleteDatabaseRequest(EndpointRequest[DeleteDatabaseResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}"
    response_model = DeleteDatabaseResponse


class CreateSampleDatabaseRequest(EndpointRequest[Database]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/sample_database"
    response_model = Database


class ValidateDatabaseRequest(EndpointRequest[ValidateDatabaseResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/validate"
    response_model = ValidateDatabaseResponse


class GetDatabaseFieldValuesRequest(EndpointRequest[DatabaseFieldValuesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/field-values"
    response_model = DatabaseFieldValuesResponse


class GetDatabaseMetadataRequest(EndpointRequest[DatabaseMetadataResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/metadata"
    response_model = DatabaseMetadataResponse


class PostDatabaseMetadataRequest(EndpointRequest[ImportDatabaseMetadataResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/metadata"
    response_model = ImportDatabaseMetadataResponse


class GetDatabaseAutocompleteSuggestionsRequest(EndpointRequest[DatabaseAutocompleteSuggestionsResponse]):
    database_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/autocomplete_suggestions"
    response_model = DatabaseAutocompleteSuggestionsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetDatabaseCardAutocompleteSuggestionsRequest(EndpointRequest[DatabaseCardAutocompleteSuggestionsResponse]):
    database_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/card_autocomplete_suggestions"
    response_model = DatabaseCardAutocompleteSuggestionsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class DiscardDatabaseValuesRequest(EndpointRequest[DatabaseOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/discard_values"
    response_model = DatabaseOperationResponse


class DismissDatabaseSpinnerRequest(EndpointRequest[DatabaseOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/dismiss_spinner"
    response_model = DatabaseOperationResponse


class GetDatabaseFieldsRequest(EndpointRequest[DatabaseFieldsResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/fields"
    response_model = DatabaseFieldsResponse


class GetDatabaseHealthcheckRequest(EndpointRequest[DatabaseHealthcheckResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/healthcheck"
    response_model = DatabaseHealthcheckResponse


class GetDatabaseIdFieldsRequest(EndpointRequest[DatabaseFieldsResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/idfields"
    response_model = DatabaseFieldsResponse


class GetDatabaseDetailMetadataRequest(EndpointRequest[DatabaseMetadataResponse]):
    database_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/metadata"
    response_model = DatabaseMetadataResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class RescanDatabaseValuesRequest(EndpointRequest[DatabaseOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/rescan_values"
    response_model = DatabaseOperationResponse


class GetDatabaseSchemaRequest(EndpointRequest[DatabaseSchemaTablesResponse]):
    database_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/schema"
    response_model = DatabaseSchemaTablesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetDatabaseSchemaTablesRequest(EndpointRequest[DatabaseSchemaTablesResponse]):
    database_id: int | str
    schema_name: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/schema/{schema_name}"
    response_model = DatabaseSchemaTablesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetDatabaseSchemasRequest(EndpointRequest[DatabaseSchemasResponse]):
    database_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/schemas"
    response_model = DatabaseSchemasResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetDatabaseSettingsAvailableRequest(EndpointRequest[DatabaseSettingsAvailableResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/settings-available"
    response_model = DatabaseSettingsAvailableResponse


class SyncDatabaseSchemaRequest(EndpointRequest[DatabaseOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/sync_schema"
    response_model = DatabaseOperationResponse


class GetDatabaseSyncableSchemasRequest(EndpointRequest[DatabaseSchemasResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/syncable_schemas"
    response_model = DatabaseSchemasResponse


class GetDatabaseUsageInfoRequest(EndpointRequest[DatabaseUsageInfoResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}/usage_info"
    response_model = DatabaseUsageInfoResponse


class GetVirtualDatabaseDatasetsRequest(EndpointRequest[DatabaseSchemaTablesResponse]):
    virtual_database: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{virtual_database}/datasets"
    response_model = DatabaseSchemaTablesResponse


class GetVirtualDatabaseSchemaDatasetsRequest(EndpointRequest[DatabaseSchemaTablesResponse]):
    virtual_database: int | str
    schema_name: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{virtual_database}/datasets/{schema_name}"
    response_model = DatabaseSchemaTablesResponse


class GetVirtualDatabaseMetadataRequest(EndpointRequest[DatabaseMetadataResponse]):
    virtual_database: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{virtual_database}/metadata"
    response_model = DatabaseMetadataResponse


class GetVirtualDatabaseSchemaRequest(EndpointRequest[DatabaseSchemaTablesResponse]):
    virtual_database: int | str
    schema_name: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{virtual_database}/schema/{schema_name}"
    response_model = DatabaseSchemaTablesResponse


class GetVirtualDatabaseSchemasRequest(EndpointRequest[DatabaseSchemasResponse]):
    virtual_database: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{virtual_database}/schemas"
    response_model = DatabaseSchemasResponse
