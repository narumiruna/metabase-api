from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.wire import JSONValue


class EeCloudAddOn(BaseModel):
    id: int | str | None = None
    name: str | None = None
    product_type: str | None = None
    model_config = ConfigDict(extra="allow")


class EeCloudPlan(BaseModel):
    id: int | str | None = None
    name: str | None = None
    model_config = ConfigDict(extra="allow")


class EeCloudAddOnsResponse(BaseModel):
    addons: list[EeCloudAddOn] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "addons")


class EeCloudPlansResponse(BaseModel):
    plans: list[EeCloudPlan] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "plans")


class EeCloudAddOnOperationResponse(BaseModel):
    ok: bool | None = None
    product_type: str | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class EeCloudProxyResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
