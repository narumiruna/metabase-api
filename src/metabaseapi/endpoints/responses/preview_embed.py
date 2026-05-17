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


class _PreviewEmbedOperationResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class GetPreviewEmbedCardResponse(BaseModel):
    card: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "card")


class GetPreviewEmbedCardParamRemappingResponse(_PreviewEmbedOperationResponse):
    data: JSONValue | None = None


class GetPreviewEmbedCardParamValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class GetPreviewEmbedCardQueryResponse(_PreviewEmbedOperationResponse):
    data: JSONValue | None = None
    status: str | None = None
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None


class GetPreviewEmbedDashboardResponse(BaseModel):
    dashboard: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "dashboard")


class GetPreviewEmbedDashboardDashcardCardResponse(GetPreviewEmbedCardQueryResponse):
    pass


class GetPreviewEmbedDashboardParamRemappingResponse(_PreviewEmbedOperationResponse):
    data: JSONValue | None = None


class GetPreviewEmbedDashboardParamSearchResponse(GetPreviewEmbedCardParamValuesResponse):
    pass


class GetPreviewEmbedDashboardParamValuesResponse(GetPreviewEmbedCardParamValuesResponse):
    pass


class GetPreviewEmbedPivotCardQueryResponse(GetPreviewEmbedCardQueryResponse):
    pass


class GetPreviewEmbedPivotDashboardDashcardCardResponse(GetPreviewEmbedCardQueryResponse):
    pass


class GetPreviewEmbedTilesCardResponse(_PreviewEmbedOperationResponse):
    content_type: str | None = None
    text: str | None = None
    value: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class GetPreviewEmbedTilesDashboardDashcardCardResponse(GetPreviewEmbedTilesCardResponse):
    pass
