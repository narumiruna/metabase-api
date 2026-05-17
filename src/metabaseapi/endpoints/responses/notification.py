from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class ListNotificationsResponse(BaseModel):
    notifications: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "notifications")


class _NotificationPayloadResponse(BaseModel):
    payload: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return cast(dict[str, Any], values)
        return {"payload": values}


class NotificationResponse(_NotificationPayloadResponse):
    id: int | str | None = None
    name: str | None = None
    creator_id: int | str | None = None
    subscriptions: list[dict[str, Any]] | None = None
    handlers: list[dict[str, Any]] | None = None


class NotificationSendResponse(_NotificationPayloadResponse):
    ok: bool | None = None
    status: str | None = None


class NotificationUnsubscribeResponse(_NotificationPayloadResponse):
    ok: bool | None = None
    status: str | None = None


class NotificationUnsubscribeUndoResponse(_NotificationPayloadResponse):
    ok: bool | None = None
    status: str | None = None
