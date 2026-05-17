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


class EeRemoteSyncBranchesResponse(BaseModel):
    items: list[str] = PydanticField(default_factory=list)
    current_branch: str | None = None
    branch: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, list):
            return {"items": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class EeRemoteSyncTaskResponse(BaseModel):
    id: int | str | None = None
    task_id: int | str | None = None
    status: str | None = None
    state: str | None = None
    task: dict[str, Any] | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeRemoteSyncDirtyResponse(BaseModel):
    items: list[dict[str, Any]] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "items")


class EeRemoteSyncHasRemoteChangesResponse(BaseModel):
    has_remote_changes: bool | None = None
    has_changes: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, bool):
            return {"has_remote_changes": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class EeRemoteSyncIsDirtyResponse(BaseModel):
    is_dirty: bool | None = None
    dirty: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, bool):
            return {"is_dirty": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class EeRemoteSyncSettingsResponse(BaseModel):
    settings: dict[str, Any] = PydanticField(default_factory=dict)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            dict_values = cast(dict[str, Any], values)
            if "settings" not in dict_values and not any(key in cls.model_fields for key in dict_values):
                return {"settings": dict_values}
        return normalize_known_payload(values, cls.model_fields, "result")


class EeRemoteSyncOperationResponse(BaseModel):
    id: int | str | None = None
    task_id: int | str | None = None
    branch: str | None = None
    status: str | None = None
    ok: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
