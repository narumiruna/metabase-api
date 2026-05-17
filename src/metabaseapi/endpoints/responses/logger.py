from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.wire import JSONValue


class _LoggerResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "result")


class LoggerAdjustmentResponse(_LoggerResponse):
    pass


class LoggerAdjustmentDeleteResponse(_LoggerResponse):
    pass


class LoggerLogsResponse(_LoggerResponse):
    pass


class LoggerPresetsResponse(_LoggerResponse):
    pass
