from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class MtGtap(BaseModel):
    id: int | str | None = None
    group_id: int | str | None = None
    table_id: int | str | None = None
    card_id: int | str | None = None
    parameter_mappings: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")


class MtGtapResponse(MtGtap):
    result: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class MtGtapsResponse(BaseModel):
    gtaps: list[MtGtap] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "gtaps")


class MtGtapValidationResponse(BaseModel):
    valid: bool | None = None
    errors: list[JSONValue] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class MtGtapDeleteResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
