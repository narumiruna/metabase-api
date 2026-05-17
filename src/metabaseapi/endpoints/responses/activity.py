from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
from metabaseapi.endpoints.entities import ActivityItem
from metabaseapi.wire import JSONValue


class ListActivityItemsResponse(BaseModel):
    items: list[ActivityItem] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "items")


class ActivityMutationResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)

