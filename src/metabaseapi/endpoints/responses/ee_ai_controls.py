from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class EeAiControlsPermission(BaseModel):
    group_id: int | str | None = None
    perm_type: str | None = None
    perm_value: str | None = None
    model_config = ConfigDict(extra="allow")


class EeAiControlsPermissionsResponse(BaseModel):
    permissions: list[EeAiControlsPermission] = PydanticField(default_factory=list)
    advanced: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeAiControlsUsageLimit(BaseModel):
    tenant_id: int | str | None = None
    group_id: int | str | None = None
    max_usage: int | None = None
    model_config = ConfigDict(extra="allow")


class EeAiControlsUsageLimitResponse(EeAiControlsUsageLimit):
    result: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeAiControlsTenantUsageLimitsResponse(BaseModel):
    limits: list[EeAiControlsUsageLimit] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "limits")


class EeAiControlsGroupUsageLimitsResponse(BaseModel):
    limits: list[EeAiControlsUsageLimit] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "limits")
