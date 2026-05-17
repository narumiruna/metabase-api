from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class NativeQuerySnippet(BaseModel):
    id: int | str | None = None
    name: str | None = None
    description: str | None = None
    content: str | None = None
    database_id: int | str | None = None
    collection_id: int | str | None = None
    creator_id: int | str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    archived: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class ListNativeQuerySnippetsResponse(BaseModel):
    snippets: list[NativeQuerySnippet] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "snippets")
