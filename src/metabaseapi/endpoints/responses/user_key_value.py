from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.wire import JSONValue


class _UserKeyValueResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class UserKeyValueNamespaceResponse(_UserKeyValueResponse):
    namespace: str | None = None
    data: dict[str, object] = PydanticField(default_factory=dict)


class UserKeyValueStoreResponse(_UserKeyValueResponse):
    status: str | None = None
    value: JSONValue | None = None


class UserKeyValueResponse(_UserKeyValueResponse):
    value: JSONValue | None = None


class DeleteUserKeyValueResponse(_UserKeyValueResponse):
    status: str | None = None
