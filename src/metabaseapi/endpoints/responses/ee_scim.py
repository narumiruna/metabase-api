from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.wire import JSONValue


class EeScimApiKeyResponse(BaseModel):
    id: int | str | None = None
    api_key: str | None = None
    key: str | None = None
    masked_key: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeScimMeta(BaseModel):
    resource_type: str | None = PydanticField(default=None, alias="resourceType")
    created: str | None = None
    last_modified: str | None = PydanticField(default=None, alias="lastModified")
    location: str | None = None
    version: str | None = None
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimEmail(BaseModel):
    value: str | None = None
    type: str | None = None
    primary: bool | None = None
    model_config = ConfigDict(extra="allow")


class EeScimGroupMember(BaseModel):
    value: str | None = None
    display: str | None = None
    ref: str | None = PydanticField(default=None, alias="$ref")
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimGroup(BaseModel):
    schemas: list[str] | None = None
    id: int | str | None = None
    external_id: str | None = PydanticField(default=None, alias="externalId")
    display_name: str | None = PydanticField(default=None, alias="displayName")
    members: list[EeScimGroupMember] = PydanticField(default_factory=list)
    meta: EeScimMeta | None = None
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimUserName(BaseModel):
    formatted: str | None = None
    family_name: str | None = PydanticField(default=None, alias="familyName")
    given_name: str | None = PydanticField(default=None, alias="givenName")
    middle_name: str | None = PydanticField(default=None, alias="middleName")
    honorific_prefix: str | None = PydanticField(default=None, alias="honorificPrefix")
    honorific_suffix: str | None = PydanticField(default=None, alias="honorificSuffix")
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimUserGroup(BaseModel):
    value: str | None = None
    display: str | None = None
    type: str | None = None
    ref: str | None = PydanticField(default=None, alias="$ref")
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimUser(BaseModel):
    schemas: list[str] | None = None
    id: int | str | None = None
    external_id: str | None = PydanticField(default=None, alias="externalId")
    user_name: str | None = PydanticField(default=None, alias="userName")
    name: EeScimUserName | None = None
    display_name: str | None = PydanticField(default=None, alias="displayName")
    emails: list[EeScimEmail] = PydanticField(default_factory=list)
    groups: list[EeScimUserGroup] = PydanticField(default_factory=list)
    active: bool | None = None
    meta: EeScimMeta | None = None
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimGroupsResponse(BaseModel):
    schemas: list[str] | None = None
    resources: list[EeScimGroup] = PydanticField(default_factory=list, alias="Resources")
    total_results: int | None = PydanticField(default=None, alias="totalResults")
    start_index: int | None = PydanticField(default=None, alias="startIndex")
    items_per_page: int | None = PydanticField(default=None, alias="itemsPerPage")
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimUsersResponse(BaseModel):
    schemas: list[str] | None = None
    resources: list[EeScimUser] = PydanticField(default_factory=list, alias="Resources")
    total_results: int | None = PydanticField(default=None, alias="totalResults")
    start_index: int | None = PydanticField(default=None, alias="startIndex")
    items_per_page: int | None = PydanticField(default=None, alias="itemsPerPage")
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class EeScimDeleteResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
