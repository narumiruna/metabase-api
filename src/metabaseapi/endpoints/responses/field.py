from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.entities import Table
from metabaseapi.wire import JSONValue


class FieldOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class FieldTableIdsResponse(BaseModel):
    table_ids: list[int] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "table_ids")


class FieldDimensionResponse(BaseModel):
    id: int | str | None = None
    field_id: int | str | None = None
    human_readable_field_id: int | str | None = None
    name: str | None = None
    type: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DeleteFieldDimensionResponse(FieldOperationResponse):
    pass


class FieldRelatedResponse(BaseModel):
    fields: list[MetabaseField] = PydanticField(default_factory=list)
    tables: list[Table] = PydanticField(default_factory=list)
    cards: list[Card] = PydanticField(default_factory=list)
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    databases: list[Database] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class FieldRemappingResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    remappings: list[JSONValue] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "values")


class FieldSearchResponse(FieldRemappingResponse):
    pass


class FieldValuesResponse(FieldRemappingResponse):
    human_readable_values: list[JSONValue] = PydanticField(default_factory=list)


class FieldSummaryResponse(BaseModel):
    count: int | None = None
    distinct_count: int | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class UpdateFieldValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    human_readable_values: list[JSONValue] = PydanticField(default_factory=list)
    ok: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)
