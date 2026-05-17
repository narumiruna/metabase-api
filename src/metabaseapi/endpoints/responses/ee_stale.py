from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class EeStaleItem(BaseModel):
    id: int | str | None = None
    name: str | None = None
    model: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")


class EeStaleResponse(BaseModel):
    items: list[EeStaleItem] = PydanticField(default_factory=list)
    total: int | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "items")
