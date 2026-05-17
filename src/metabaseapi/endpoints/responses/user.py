from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import User
from metabaseapi.wire import JSONValue


class ListUsersResponse(BaseModel):
    users: list[User] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "users")


class UserRecipientsResponse(ListUsersResponse):
    pass


class DeleteUserResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class UserModalResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class UserPasswordUpdateResponse(UserModalResponse):
    pass


class UserPasswordResetUrlResponse(BaseModel):
    url: str | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
