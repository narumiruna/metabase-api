from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
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
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class _CardStatusResponse(BaseModel):
    ok: bool | None = None
    uuid: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {}

        dict_values = cast(dict[str, object], values)
        return {key: dict_values[key] for key in cls.model_fields if key in dict_values}


class CardCollectionsResponse(_CardOperationResponse):
    pass


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
    pass


class CardQueryExportResponse(_CardOperationResponse):
    pass


class CardParameterValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class CardRemappingResponse(_CardOperationResponse):
    pass


class CardQueryMetadataResponse(_CardOperationResponse):
    pass


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
