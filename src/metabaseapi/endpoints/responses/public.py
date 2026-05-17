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


class _PublicOperationResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class PublicActionResponse(BaseModel):
    action: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "action")


class PublicActionExecutionResponse(_PublicOperationResponse):
    ok: bool | None = None
    data: JSONValue | None = None
    status: str | None = None


class PublicCardResponse(_PublicOperationResponse):
    card: dict[str, Any] | None = None
    data: JSONValue | None = None
    status: str | None = None


class PublicCardQueryResponse(PublicCardResponse):
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None


class PublicExportResponse(_PublicOperationResponse):
    value: JSONValue | None = None
    content_type: str | None = None
    text: str | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class PublicParameterValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class PublicRemappingResponse(_PublicOperationResponse):
    data: JSONValue | None = None


class PublicDashboardResponse(_PublicOperationResponse):
    dashboard: dict[str, Any] | None = None
    dashcards: list[JSONValue] | None = None
    parameters: list[JSONValue] | None = None


class PublicDashboardCardResponse(PublicCardQueryResponse):
    pass


class PublicDashboardExecuteResponse(PublicActionExecutionResponse):
    pass


class PublicDocumentResponse(BaseModel):
    document: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "document")


class PublicDocumentCardResponse(PublicCardQueryResponse):
    pass


class PublicOEmbedResponse(_PublicOperationResponse):
    type: str | None = None
    version: str | None = None
    provider_name: str | None = None
    provider_url: str | None = None
    title: str | None = None
    html: str | None = None
    width: int | None = None
    height: int | None = None


class PublicTileResponse(PublicExportResponse):
    pass
