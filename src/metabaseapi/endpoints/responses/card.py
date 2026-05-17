from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.wire import JSONValue


class ListCardsResponse(BaseModel):
    cards: list[Card] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "cards")


class CardsDashboardsResponse(BaseModel):
    cards: list[dict[str, Any]] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @classmethod
    @model_validator(mode="before")
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if values is None:
            return {"cards": []}

        if isinstance(values, list):
            return {"cards": values}

        if isinstance(values, dict):
            dict_values = cast(dict[str, object], values)
            if isinstance(dict_values.get("cards"), list):
                return cast(dict[str, Any], dict_values)
            if "data" in dict_values and isinstance(dict_values["data"], list):
                remainder = dict(dict_values)
                del remainder["data"]
                return {"cards": dict_values["data"], **remainder}
            return {"cards": [], "raw": dict_values}

        return {"cards": [], "raw": values}


class _CardOperationResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class CardCollectionsResponse(_CardOperationResponse):
    pass


class CardEmbeddableResponse(BaseModel):
    cards: list[Card] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "cards")


class CardPublicResponse(CardEmbeddableResponse):
    pass


class CreateCardPublicLinkResponse(_CardOperationResponse):
    uuid: str | None = None


class DeleteCardPublicLinkResponse(_CardOperationResponse):
    ok: bool | None = None


class DeleteCardResponse(_CardOperationResponse):
    ok: bool | None = None


class MoveCardsResponse(_CardOperationResponse):
    ok: bool | None = None


class CardQueryResponse(_CardOperationResponse):
    pass


class CardQueryExportResponse(_CardOperationResponse):
    pass


class CardParameterValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "values")


class CardRemappingResponse(_CardOperationResponse):
    pass


class CardQueryMetadataResponse(_CardOperationResponse):
    pass


class CardDashboardsResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "dashboards")


class CardSeriesResponse(BaseModel):
    series: list[Card] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "series")
