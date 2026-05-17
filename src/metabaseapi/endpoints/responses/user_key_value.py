from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.wire import JSONValue


class _UserKeyValueResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {}

        dict_values = cast(dict[str, object], values)
        return {key: dict_values[key] for key in cls.model_fields if key in dict_values}


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
