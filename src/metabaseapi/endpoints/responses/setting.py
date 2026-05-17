from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.wire import JSONValue


class SettingsResponse(BaseModel):
    settings: dict[str, Any] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return {"settings": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class UpdateSettingsResponse(SettingsResponse):
    pass


class SettingResponse(BaseModel):
    key: str | None = None
    value: JSONValue | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "value")


class UpdateSettingResponse(SettingResponse):
    pass
