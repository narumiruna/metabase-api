from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.wire import JSONValue


class EeEmailOverrideResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "result")


class DeleteEeEmailOverrideResponse(EeEmailOverrideResponse):
    pass
