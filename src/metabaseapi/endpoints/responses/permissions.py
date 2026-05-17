from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class PermissionsGraphResponse(BaseModel):
    revision: int | None = None
    groups: dict[str, Any] = PydanticField(default_factory=dict)
    databases: dict[str, Any] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"result": values}

        dict_values = cast(dict[str, Any], values)
        payload: dict[str, Any] = {}
        if isinstance(dict_values.get("revision"), int):
            payload["revision"] = dict_values["revision"]
        if isinstance(dict_values.get("groups"), dict):
            payload["groups"] = dict_values["groups"]
        if isinstance(dict_values.get("databases"), dict):
            payload["databases"] = dict_values["databases"]

        remainder = {key: value for key, value in dict_values.items() if key not in payload}
        if remainder:
            payload["result"] = remainder
        return payload


class PermissionsGroupMember(BaseModel):
    membership_id: int | str | None = None
    id: int | str | None = None
    user_id: int | str | None = None
    group_id: int | str | None = None
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_group_manager: bool | None = None
    model_config = ConfigDict(extra="allow")


class PermissionsGroup(BaseModel):
    id: int | str | None = None
    name: str | None = None
    member_count: int | None = None
    members: list[PermissionsGroupMember] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")


class PermissionsGroupsResponse(BaseModel):
    groups: list[PermissionsGroup] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "groups")


class PermissionsGroupResponse(PermissionsGroup):
    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            dict_values = cast(dict[str, Any], values)
            if "group" in dict_values and isinstance(dict_values["group"], dict):
                return cast(dict[str, Any], dict_values["group"])
            return dict_values
        return {}


class DeletePermissionsGroupResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class PermissionsMembership(BaseModel):
    id: int | str | None = None
    membership_id: int | str | None = None
    user_id: int | str | None = None
    group_id: int | str | None = None
    is_group_manager: bool | None = None
    model_config = ConfigDict(extra="allow")


class PermissionsMembershipsResponse(BaseModel):
    memberships: dict[str, list[PermissionsMembership]] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"result": values}

        dict_values = cast(dict[str, Any], values)
        if "memberships" in dict_values and isinstance(dict_values["memberships"], dict):
            return dict_values
        if "data" in dict_values and isinstance(dict_values["data"], dict):
            return {"memberships": dict_values["data"]}

        memberships: dict[str, object] = {}
        remainder: dict[str, object] = {}
        for key, value in dict_values.items():
            if isinstance(value, list):
                memberships[key] = value
            else:
                remainder[key] = value

        payload: dict[str, Any] = {"memberships": memberships}
        if remainder:
            payload["result"] = remainder
        return payload


class PermissionsMembershipListResponse(BaseModel):
    members: list[PermissionsMembership] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "members")


class PermissionsMembershipResponse(PermissionsMembership):
    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            dict_values = cast(dict[str, Any], values)
            if "membership" in dict_values and isinstance(dict_values["membership"], dict):
                return cast(dict[str, Any], dict_values["membership"])
            return dict_values
        return {}


class DeletePermissionsMembershipResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
