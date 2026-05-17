from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class _DatasetOperationResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class DatasetQueryResponse(_DatasetOperationResponse):
    data: JSONValue | None = None
    status: str | None = None
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None


class DatasetNativeResponse(_DatasetOperationResponse):
    query: str | None = None
    native: JSONValue | None = None


class DatasetParameterRemappingResponse(_DatasetOperationResponse):
    data: JSONValue | None = None


class DatasetParameterSearchResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class DatasetParameterValuesResponse(DatasetParameterSearchResponse):
    pass


class DatasetPivotResponse(DatasetQueryResponse):
    pass


class DatasetQueryMetadataResponse(_DatasetOperationResponse):
    metadata: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        payload = normalize_known_payload(values, cls.model_fields, "result")
        if set(payload) == {"result"}:
            return {"metadata": payload["result"]}
        return payload


class DatasetExportResponse(_DatasetOperationResponse):
    value: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")
