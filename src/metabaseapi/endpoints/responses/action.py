from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import Action


class ActionExecutionResponse(BaseModel):
    ok: bool | None = None
    uuid: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {}

        dict_values = cast(dict[str, object], values)
        payload: dict[str, object] = {}
        ok = dict_values.get("ok")
        uuid = dict_values.get("uuid")
        if isinstance(ok, bool):
            payload["ok"] = ok
        if isinstance(uuid, str):
            payload["uuid"] = uuid
        return payload


class ListActionsResponse(BaseModel):
    actions: list[Action] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "actions")
