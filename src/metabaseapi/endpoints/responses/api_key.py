from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
from metabaseapi.endpoints.entities import ApiKey
from metabaseapi.wire import JSONValue


class ListApiKeysResponse(BaseModel):
    api_keys: list[ApiKey] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "api_keys")


class ApiKeyCountResponse(BaseModel):
    count: int | None = None
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, int):
            return {"count": values}
        if isinstance(values, dict):
            return cast("dict[str, Any]", values)
        return {"raw": values}


class DeleteApiKeyResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)
