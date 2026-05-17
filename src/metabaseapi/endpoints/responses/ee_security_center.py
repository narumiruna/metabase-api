from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class EeSecurityCenterAdvisory(BaseModel):
    id: int | str | None = None
    advisory_id: int | str | None = None
    title: str | None = None
    status: str | None = None
    severity: str | None = None
    matched: bool | None = None
    acknowledged: bool | None = None
    acknowledged_at: str | None = None
    created_at: str | None = None
    updated_at: str | None = None
    model_config = ConfigDict(extra="allow")


class EeSecurityCenterAdvisoriesResponse(BaseModel):
    advisories: list[EeSecurityCenterAdvisory] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        payload = normalize_model_list_payload(values, cls.model_fields, "advisories")
        if not payload["advisories"] and isinstance(values, dict):
            payload = normalize_known_payload(values, cls.model_fields, "result")
            payload.setdefault("advisories", [])
        return payload


class EeSecurityCenterOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    status: str | None = None
    message: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
