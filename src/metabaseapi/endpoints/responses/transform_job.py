from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.wire import JSONValue


def _normalize_list_payload(values: object, field_names: set[str], list_key: str) -> dict[str, Any]:
    if values is None:
        return {list_key: []}
    if isinstance(values, list):
        return {list_key: values}
    payload = normalize_model_fields_payload(values, field_names)
    if isinstance(values, dict):
        dict_values = cast(dict[str, object], values)
        for source_key in (list_key, "data", "items"):
            source_value = dict_values.get(source_key)
            if isinstance(source_value, list):
                payload[list_key] = source_value
                break
    payload.setdefault(list_key, [])
    return payload


class TransformJob(BaseModel):
    id: int | str | None = None
    name: str | None = None
    description: str | None = None
    schedule: JSONValue | None = None
    transform_ids: list[int | str] = PydanticField(default_factory=list)
    tag_ids: list[int | str] = PydanticField(default_factory=list)
    created_at: Any | None = None
    updated_at: Any | None = None
    model_config = ConfigDict(extra="allow")


class TransformJobResponse(BaseModel):
    job: TransformJob = PydanticField(default_factory=TransformJob)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "job")


class ListTransformJobsResponse(BaseModel):
    jobs: list[TransformJob] = PydanticField(default_factory=list)
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, set(cls.model_fields), "jobs")


class TransformJobTransformsResponse(BaseModel):
    transforms: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, set(cls.model_fields), "transforms")


class TransformJobOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    success: bool | None = None
    status: str | None = None
    message: str | None = None
    model_config = ConfigDict(extra="allow")


class DeleteTransformJobResponse(TransformJobOperationResponse):
    pass
