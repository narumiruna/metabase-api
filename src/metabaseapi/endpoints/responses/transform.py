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


class Transform(BaseModel):
    id: int | str | None = None
    name: str | None = None
    description: str | None = None
    source: JSONValue | None = None
    query: JSONValue | None = None
    table: JSONValue | None = None
    database_id: int | str | None = None
    schema_: str | None = PydanticField(default=None, alias="schema")
    job_id: int | str | None = None
    tag_ids: list[int | str] = PydanticField(default_factory=list)
    created_at: Any | None = None
    updated_at: Any | None = None
    model_config = ConfigDict(extra="allow")


class TransformRun(BaseModel):
    id: int | str | None = None
    transform_id: int | str | None = None
    job_id: int | str | None = None
    status: str | None = None
    started_at: Any | None = None
    ended_at: Any | None = None
    error: JSONValue | None = None
    model_config = ConfigDict(extra="allow")


class TransformResponse(BaseModel):
    transform: Transform = PydanticField(default_factory=Transform)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "transform")


class ListTransformsResponse(BaseModel):
    transforms: list[Transform] = PydanticField(default_factory=list)
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, set(cls.model_fields), "transforms")


class TransformRunResponse(BaseModel):
    run: TransformRun = PydanticField(default_factory=TransformRun)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "run")


class ListTransformRunsResponse(BaseModel):
    runs: list[TransformRun] = PydanticField(default_factory=list)
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, set(cls.model_fields), "runs")


class TransformDependenciesResponse(BaseModel):
    dependencies: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, set(cls.model_fields), "dependencies")


class TransformOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    success: bool | None = None
    status: str | None = None
    message: str | None = None
    model_config = ConfigDict(extra="allow")


class DeleteTransformResponse(TransformOperationResponse):
    pass
