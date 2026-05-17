from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class _EmbedOperationResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class GetEmbedCardResponse(BaseModel):
    card: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "card")


class GetEmbedCardParamRemappingResponse(_EmbedOperationResponse):
    data: JSONValue | None = None


class GetEmbedCardParamSearchResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class GetEmbedCardParamValuesResponse(GetEmbedCardParamSearchResponse):
    pass


class GetEmbedCardQueryResponse(_EmbedOperationResponse):
    data: JSONValue | None = None
    status: str | None = None
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None


class GetEmbedCardQueryExportResponse(_EmbedOperationResponse):
    value: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class GetEmbedDashboardResponse(BaseModel):
    dashboard: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "dashboard")


class GetEmbedDashboardDashcardCardResponse(GetEmbedCardQueryResponse):
    pass


class GetEmbedDashboardDashcardCardExportResponse(GetEmbedCardQueryExportResponse):
    pass


class GetEmbedDashboardParamRemappingResponse(_EmbedOperationResponse):
    data: JSONValue | None = None


class GetEmbedDashboardParamSearchResponse(GetEmbedCardParamSearchResponse):
    pass


class GetEmbedDashboardParamValuesResponse(GetEmbedCardParamSearchResponse):
    pass


class GetEmbedPivotCardQueryResponse(GetEmbedCardQueryResponse):
    pass


class GetEmbedPivotDashboardDashcardCardResponse(GetEmbedCardQueryResponse):
    pass


class GetEmbedTilesCardResponse(_EmbedOperationResponse):
    content_type: str | None = None
    text: str | None = None
    value: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class GetEmbedTilesDashboardDashcardCardResponse(GetEmbedTilesCardResponse):
    pass
