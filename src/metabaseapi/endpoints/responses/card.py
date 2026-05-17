from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.wire import JSONValue


class ListCardsResponse(BaseModel):
    cards: list[Card] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "cards")


class CardsDashboardsResponse(BaseModel):
    cards: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "cards")


class _CardOperationResponse(BaseModel):
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")


class _CardStatusResponse(BaseModel):
    ok: bool | None = None
    uuid: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class CardCollectionsResponse(_CardOperationResponse):
    collections: list[JSONValue] = PydanticField(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, list):
            return {"collections": values}
        if isinstance(values, dict):
            dict_values = cast(dict[str, object], values)
            if "collections" in dict_values and isinstance(dict_values["collections"], list):
                return {"collections": dict_values["collections"]}
            if "data" in dict_values and isinstance(dict_values["data"], list):
                return {"collections": dict_values["data"]}
        return normalize_known_payload(values, cls.model_fields, "result")


class CardEmbeddableResponse(BaseModel):
    cards: list[Card] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "cards")


class CardPublicResponse(CardEmbeddableResponse):
    pass


class CreateCardPublicLinkResponse(_CardStatusResponse):
    uuid: str | None = None


class DeleteCardPublicLinkResponse(_CardStatusResponse):
    ok: bool | None = None


class DeleteCardResponse(_CardStatusResponse):
    ok: bool | None = None


class MoveCardsResponse(_CardStatusResponse):
    ok: bool | None = None


class CardQueryResponse(_CardOperationResponse):
    data: JSONValue | None = None
    status: str | None = None
    row_count: int | None = None
    running_time: int | float | None = None
    average_execution_time: int | float | None = None
    database_id: int | str | None = None
    started_at: str | None = None
    json_query: dict[str, Any] | None = None


class CardQueryExportResponse(_CardOperationResponse):
    value: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")


class CardParameterValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class CardRemappingResponse(_CardOperationResponse):
    data: JSONValue | None = None


class CardQueryMetadataResponse(_CardOperationResponse):
    metadata: JSONValue | None = None

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        payload = normalize_known_payload(values, cls.model_fields, "result")
        if set(payload) == {"result"}:
            return {"metadata": payload["result"]}
        return payload


class CardDashboardsResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "dashboards")


class CardSeriesResponse(BaseModel):
    series: list[Card] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "series")
