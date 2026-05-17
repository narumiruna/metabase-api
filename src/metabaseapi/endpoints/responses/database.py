from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.entities import Table
from metabaseapi.wire import JSONValue


class ListDatabasesResponse(BaseModel):
    databases: list[Database] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "databases")


class DeleteDatabaseResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class ValidateDatabaseResponse(BaseModel):
    valid: bool | None = None
    message: str | None = None
    errors: JSONValue | None = None
    details: JSONValue | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DatabaseFieldValuesResponse(BaseModel):
    field_values: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "field_values")


class DatabaseMetadataResponse(BaseModel):
    database: Database | None = None
    databases: list[Database] = PydanticField(default_factory=list)
    tables: list[Table] = PydanticField(default_factory=list)
    fields: list[MetabaseField] = PydanticField(default_factory=list)
    field_values: list[dict[str, Any]] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class ImportDatabaseMetadataResponse(BaseModel):
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DatabaseFieldsResponse(BaseModel):
    fields: list[MetabaseField] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "fields")


class DatabaseSchemaTablesResponse(BaseModel):
    tables: list[Table] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "tables")


class DatabaseSchemasResponse(BaseModel):
    schemas: list[str] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        payload = normalize_strict_list_payload(values, "schemas")
        schemas = payload.get("schemas", [])
        if isinstance(schemas, list) and all(isinstance(schema, str) for schema in schemas):
            return {"schemas": schemas}
        return {"schemas": []}


class DatabaseAutocompleteSuggestionsResponse(BaseModel):
    suggestions: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "suggestions")


class DatabaseCardAutocompleteSuggestionsResponse(DatabaseAutocompleteSuggestionsResponse):
    pass


class DatabaseOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DatabaseHealthcheckResponse(BaseModel):
    status: str | None = None
    message: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DatabaseSettingsAvailableResponse(BaseModel):
    settings: list[dict[str, Any]] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, list):
            return {"settings": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class DatabaseUsageInfoResponse(BaseModel):
    usage: dict[str, int] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        payload = normalize_known_payload(values, cls.model_fields, "result")
        if set(payload) == {"result"} and isinstance(payload["result"], dict):
            usage = payload["result"]
            if all(isinstance(value, int) for value in usage.values()):
                return {"usage": usage}
        return payload
