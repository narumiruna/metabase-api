from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class ListPulsesResponse(BaseModel):
    pulses: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "pulses")


class _PulsePayloadResponse(BaseModel):
    payload: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return cast(dict[str, Any], values)
        return {"payload": values}


class PulseResponse(_PulsePayloadResponse):
    id: int | str | None = None
    name: str | None = None
    archived: bool | None = None
    dashboard_id: int | str | None = None
    collection_id: int | str | None = None
    creator_id: int | str | None = None
    cards: list[dict[str, Any]] | None = None
    channels: list[dict[str, Any]] | None = None
    parameters: list[dict[str, Any]] | None = None


class PulseFormInputResponse(_PulsePayloadResponse):
    channels: JSONValue | None = None


class PulseTestResponse(_PulsePayloadResponse):
    ok: bool | None = None


class PulseSubscriptionDeleteResponse(_PulsePayloadResponse):
    ok: bool | None = None


class PulseUnsubscribeResponse(_PulsePayloadResponse):
    ok: bool | None = None


class PulseUnsubscribeUndoResponse(_PulsePayloadResponse):
    ok: bool | None = None
