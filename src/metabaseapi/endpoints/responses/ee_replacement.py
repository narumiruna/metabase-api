from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class EeReplacementCompatibilityError(BaseModel):
    field: str | None = None
    message: str | None = None
    type: str | None = None
    source: JSONValue | None = None
    target: JSONValue | None = None
    model_config = ConfigDict(extra="allow")


class EeReplacementCheckReplaceSourceResponse(BaseModel):
    compatible: bool | None = None
    errors: list[EeReplacementCompatibilityError] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeReplacementRun(BaseModel):
    id: int | str | None = None
    run_id: int | str | None = None
    status: str | None = None
    is_active: bool | None = None
    error: str | None = None
    model_config = ConfigDict(extra="allow")


class EeReplacementRunResponse(BaseModel):
    id: int | str | None = None
    run_id: int | str | None = None
    status: str | None = None
    is_active: bool | None = None
    run: EeReplacementRun | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeReplacementRunsResponse(BaseModel):
    runs: list[EeReplacementRun] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "runs")


class EeReplacementOperationResponse(BaseModel):
    id: int | str | None = None
    run_id: int | str | None = None
    status: str | None = None
    ok: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
