from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.wire import JSONValue


class EmailSettingsResponse(BaseModel):
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DeleteEmailSettingsResponse(EmailSettingsResponse):
    pass


class TestEmailResponse(EmailSettingsResponse):
    pass
