from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.wire import JSONValue


class TileResponse(BaseModel):
    result: JSONValue | None = None
    value: JSONValue | None = None
    content_type: str | None = None
    text: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class SavedCardTileResponse(TileResponse):
    pass


class DashboardCardTileResponse(TileResponse):
    pass


class AdHocQueryTileResponse(TileResponse):
    pass
