from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Collection
from metabaseapi.wire import JSONValue


class ListCollectionsResponse(BaseModel):
    collections: list[Collection] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "collections")


class CollectionDashboardQuestionCandidatesResponse(BaseModel):
    cards: list[Card] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "cards")


class CollectionMoveDashboardQuestionCandidatesResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class CollectionGraphResponse(BaseModel):
    revision: int | None = None
    groups: JSONValue | None = None
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class CollectionTreeResponse(BaseModel):
    id: int | str | None = None
    name: str | None = None
    children: list[CollectionTreeResponse] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class CollectionItemsResponse(BaseModel):
    items: list[JSONValue] = PydanticField(default_factory=list)
    total: int | None = None
    limit: int | None = None
    offset: int | None = None
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_list_payload(values, "items")


class DeleteCollectionResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    success: bool | None = None
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)
