from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import Card
from metabaseapi.wire import JSONValue


class ListMetricsResponse(BaseModel):
    metrics: list[Card] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "metrics")


class MetricDatasetResponse(BaseModel):
    data: JSONValue | None = None
    status: str | None = None
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class MetricBreakoutValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    data: JSONValue | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "values")


class MetricDimensionValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    human_readable_values: list[JSONValue] = PydanticField(default_factory=list)
    remappings: list[JSONValue] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "values")


class MetricDimensionRemappingResponse(MetricDimensionValuesResponse):
    pass


class MetricDimensionSearchResponse(MetricDimensionValuesResponse):
    pass
