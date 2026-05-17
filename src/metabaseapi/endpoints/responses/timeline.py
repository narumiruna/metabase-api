from __future__ import annotations

from datetime import UTC
from datetime import datetime
from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import field_validator
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.endpoints.responses.timeline_event import TimelineEvent
from metabaseapi.wire import JSONValue


class Timeline(BaseModel):
    id: int | str | None = None
    name: str | None = None
    default: bool | None = None
    description: str | None = None
    icon: str | None = None
    collection_id: int | str | None = None
    archived: bool | None = None
    creator_id: int | str | None = None
    creator: JSONValue | None = None
    collection: JSONValue | None = None
    events: list[TimelineEvent] = PydanticField(default_factory=list)
    created_at: datetime | None = None
    updated_at: datetime | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)

    @field_validator("created_at", "updated_at", mode="before")
    @classmethod
    def parse_datetime(cls, value: object) -> datetime | None:
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        if isinstance(value, (int, float)):
            seconds = value / 1000 if value > 10_000_000_000 else value
            return datetime.fromtimestamp(seconds, tz=UTC)
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError as exc:
                msg = f"invalid timestamp: {value}"
                raise TypeError(msg) from exc

        msg = f"invalid timestamp: {value!r}"
        raise TypeError(msg)


class TimelineResponse(BaseModel):
    timeline: Timeline = PydanticField(default_factory=Timeline)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict) and "timeline" in values:
            return normalize_model_fields_payload(values, cls.model_fields)
        return {"timeline": values}


class ListTimelinesResponse(BaseModel):
    timelines: list[Timeline] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "timelines")


class DeleteTimelineResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    success: bool | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)
