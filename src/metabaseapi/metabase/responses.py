from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.metabase.entities import Card
from metabaseapi.metabase.entities import Collection
from metabaseapi.metabase.entities import Dashboard
from metabaseapi.metabase.entities import Database
from metabaseapi.metabase.entities import Table
from metabaseapi.metabase.entities import User
from metabaseapi.models import JSONValue


class ListDatabasesResponse(BaseModel):
    databases: list[Database] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "databases")


class ListCardsResponse(BaseModel):
    cards: list[Card] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "cards")


class ListDashboardsResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "dashboards")


class ListUsersResponse(BaseModel):
    users: list[User] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "users")


class ListCollectionsResponse(BaseModel):
    collections: list[Collection] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "collections")


class ListTablesResponse(BaseModel):
    tables: list[Table] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "tables")


def _normalize_list_payload(values: object, list_key: str) -> dict[str, Any]:
    if values is None:
        return {list_key: []}

    if isinstance(values, list):
        return {list_key: values}

    if isinstance(values, dict):
        dict_values = cast(dict[str, object], values)
        if list_key in dict_values and isinstance(dict_values[list_key], list):
            return dict_values
        if "data" in dict_values and isinstance(dict_values["data"], list):
            remainder = dict(dict_values)
            del remainder["data"]
            return {list_key: dict_values["data"], **remainder}
        if "items" in dict_values and isinstance(dict_values["items"], list):
            remainder = dict(dict_values)
            del remainder["items"]
            return {list_key: dict_values["items"], **remainder}
        return {list_key: [], "raw": dict_values}

    return {list_key: [], "raw": values}


__all__ = [
    "ListCardsResponse",
    "ListCollectionsResponse",
    "ListDashboardsResponse",
    "ListDatabasesResponse",
    "ListTablesResponse",
    "ListUsersResponse",
]
