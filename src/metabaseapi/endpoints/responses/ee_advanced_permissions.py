from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.wire import JSONValue


class EeApplicationPermissionsGraphResponse(BaseModel):
    revision: int | None = None
    groups: dict[str, Any] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeImpersonationPolicy(BaseModel):
    id: int | str | None = None
    group_id: int | str | None = None
    db_id: int | str | None = None
    attribute: str | None = None
    model_config = ConfigDict(extra="allow")


class EeImpersonationResponse(BaseModel):
    policies: list[EeImpersonationPolicy] = PydanticField(default_factory=list)
    policy: EeImpersonationPolicy | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, list):
            return {"policies": values}
        if isinstance(values, dict):
            dict_values = cast(dict[str, Any], values)
            if any(key in dict_values for key in ("id", "group_id", "db_id")):
                return {"policy": dict_values}
            return normalize_known_payload(dict_values, cls.model_fields, "result")
        return {"result": values}


class DeleteEeImpersonationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
