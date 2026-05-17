from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class EmbedTheme(BaseModel):
    id: int | str | None = None
    name: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    payload: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "payload")


class ListEmbedThemesResponse(BaseModel):
    embed_themes: list[EmbedTheme] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "embed_themes")


class SeedDefaultEmbedThemesResponse(BaseModel):
    embed_themes: list[EmbedTheme] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, list):
            return {"embed_themes": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class DeleteEmbedThemeResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    success: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, bool):
            return {"success": values}
        if isinstance(values, dict):
            dict_values = cast(dict[str, object], values)
            return normalize_known_payload(dict_values, cls.model_fields, "result")
        return {"result": values}
