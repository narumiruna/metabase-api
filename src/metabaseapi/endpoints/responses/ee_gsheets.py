from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.wire import JSONValue


class EeGsheetsConnectionResponse(BaseModel):
    db_id: int | str | None = None
    status: str | None = None
    state: str | None = None
    connected: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeGsheetsDeleteConnectionResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "result")


class EeGsheetsServiceAccountResponse(BaseModel):
    configured: bool | None = None
    setup: bool | None = None
    email: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
