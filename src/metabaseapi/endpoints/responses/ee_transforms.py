from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.wire import JSONValue


class EeTransformInspectorLens(BaseModel):
    id: int | str | None = None
    name: str | None = None
    type: str | None = None
    model_config = ConfigDict(extra="allow")


class EeTransformInspectResponse(BaseModel):
    lenses: list[EeTransformInspectorLens] = PydanticField(default_factory=list)
    sections: list[JSONValue] = PydanticField(default_factory=list)
    cards: list[JSONValue] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeTransformInspectQueryResponse(BaseModel):
    data: JSONValue | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
