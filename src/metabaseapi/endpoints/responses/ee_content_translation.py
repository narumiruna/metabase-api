from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class EeContentTranslationCsvResponse(BaseModel):
    content_type: str | None = None
    text: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeContentTranslationEntry(BaseModel):
    locale: str | None = None
    msgid: str | None = None
    msgstr: str | None = None
    model_config = ConfigDict(extra="allow")


class EeContentTranslationDictionaryResponse(BaseModel):
    dictionary: list[EeContentTranslationEntry] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, list):
            return normalize_model_list_payload(values, cls.model_fields, "dictionary")
        return normalize_known_payload(values, cls.model_fields, "result")


class EeContentTranslationUploadResponse(BaseModel):
    ok: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
