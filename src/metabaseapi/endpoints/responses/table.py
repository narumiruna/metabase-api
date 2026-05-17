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


class ListTablesResponse(BaseModel):
    tables: list[Table] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "tables")


class TableOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    tables: list[Table] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class TableForeignKeysResponse(BaseModel):
    fks: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "fks")


class TableQueryMetadataResponse(BaseModel):
    table: Table | None = None
    database: Database | None = None
    fields: list[MetabaseField] = PydanticField(default_factory=list)
    fks: list[dict[str, Any]] = PydanticField(default_factory=list)
    field_values: list[dict[str, Any]] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class TableRelatedResponse(BaseModel):
    related: dict[str, JSONValue] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict) and "related" not in values:
            return {"related": values}
        return normalize_model_fields_payload(values, cls.model_fields)


class TableDataResponse(BaseModel):
    rows: list[dict[str, Any]] = PydanticField(default_factory=list)
    cols: list[dict[str, Any]] = PydanticField(default_factory=list)
    data: JSONValue | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
