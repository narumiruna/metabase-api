from __future__ import annotations

from typing import Any
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints.entities import Action
from metabaseapi.endpoints.entities import ActivityItem
from metabaseapi.endpoints.entities import Alert
from metabaseapi.endpoints.entities import ApiKey
from metabaseapi.endpoints.entities import Bookmark
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.entities import Table
from metabaseapi.endpoints.entities import User
from metabaseapi.wire import JSONValue


class ActionExecutionResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return cast(dict[str, Any], values)
        return {"raw": values}


class ListActionsResponse(BaseModel):
    actions: list[Action] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "actions")


class ListActivityItemsResponse(BaseModel):
    items: list[ActivityItem] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "items")


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
                return dict_values
            if "data" in dict_values and isinstance(dict_values["data"], list):
                remainder = dict(dict_values)
                del remainder["data"]
                return {"cards": dict_values["data"], **remainder}
            return {"cards": [], "raw": dict_values}

        return {"cards": [], "raw": values}


class ListChannelsResponse(BaseModel):
    channels: list[dict[str, Any]] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "channels")


class GenericOperationResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return cast(dict[str, Any], values)
        return {"raw": values}


class ListAlertsResponse(BaseModel):
    alerts: list[Alert] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "alerts")


class ListBookmarksResponse(BaseModel):
    bookmarks: list[Bookmark] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "bookmarks")


class ListApiKeysResponse(BaseModel):
    api_keys: list[ApiKey] = PydanticField(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return _normalize_list_payload(values, "api_keys")


class AgentResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return cast(dict[str, Any], values)
        return {"raw": values}


class ActivityMutationResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if isinstance(values, dict):
            return cast(dict[str, Any], values)
        return {"raw": values}


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
    "ActionExecutionResponse",
    "ActivityMutationResponse",
    "AgentResponse",
    "CardsDashboardsResponse",
    "GenericOperationResponse",
    "ListActionsResponse",
    "ListActivityItemsResponse",
    "ListAlertsResponse",
    "ListApiKeysResponse",
    "ListBookmarksResponse",
    "ListCardsResponse",
    "ListChannelsResponse",
    "ListCollectionsResponse",
    "ListDashboardsResponse",
    "ListDatabasesResponse",
    "ListTablesResponse",
    "ListUsersResponse",
]
