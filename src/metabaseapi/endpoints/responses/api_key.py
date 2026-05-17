from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import ApiKey


class ListApiKeysResponse(BaseModel):
    api_keys: list[ApiKey] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "api_keys")


class ApiKeyCountResponse(BaseModel):
    count: int | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, int):
            return {"count": values}
        if isinstance(values, dict):
            dict_values = cast(dict[str, object], values)
            count = dict_values.get("count")
            return {"count": count} if isinstance(count, int) else {}
        return {}


class DeleteApiKeyResponse(BaseModel):
    ok: bool | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            dict_values = cast(dict[str, object], values)
            ok = dict_values.get("ok")
            return {"ok": ok} if isinstance(ok, bool) else {}
        return {}
