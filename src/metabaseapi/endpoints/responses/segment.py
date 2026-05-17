from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.entities import Table
from metabaseapi.wire import JSONValue


class Segment(BaseModel):
    id: int | str | None = None
    name: str | None = None
    description: str | None = None
    table_id: int | str | None = None
    definition: dict[str, Any] | None = None
    archived: bool | None = None
    creator_id: int | str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class ListSegmentsResponse(BaseModel):
    segments: list[Segment] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "segments")


class DeleteSegmentResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class SegmentRelatedResponse(BaseModel):
    segments: list[Segment] = PydanticField(default_factory=list)
    fields: list[MetabaseField] = PydanticField(default_factory=list)
    tables: list[Table] = PydanticField(default_factory=list)
    cards: list[Card] = PydanticField(default_factory=list)
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    databases: list[Database] = PydanticField(default_factory=list)
    related: dict[str, JSONValue] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict) and not any(key in cls.model_fields for key in values):
            return {"related": values}
        return normalize_model_fields_payload(values, cls.model_fields)
