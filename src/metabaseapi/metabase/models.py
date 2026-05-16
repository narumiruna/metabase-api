from __future__ import annotations

import asyncio
from datetime import UTC
from datetime import datetime
from typing import Any
from typing import ClassVar
from typing import Protocol
from typing import TypeVar
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator
from pydantic import model_validator

from metabaseapi.models import JSONValue


class MetabaseRequestClient(Protocol):
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, str | int | bool | float | None] | None = ...,
        json_data: JSONValue | None = ...,
    ) -> object: ...


class _MetabaseResponseBase(BaseModel):
    model_config = ConfigDict(extra="allow")

    @field_validator("created_at", "updated_at", mode="before", check_fields=False)
    @classmethod
    def parse_epoch_datetime(cls, value: object) -> datetime | None:
        if value is None:
            return None
        if isinstance(value, datetime):
            return value
        if isinstance(value, (int, float)):
            seconds = value / 1000 if value > 10_000_000_000 else value
            return datetime.fromtimestamp(seconds, tz=UTC)
        if isinstance(value, str):
            try:
                normalized = value.replace("Z", "+00:00")
                return datetime.fromisoformat(normalized)
            except ValueError as exc:
                msg = f"invalid timestamp: {value}"
                raise TypeError(msg) from exc

        msg = f"invalid timestamp: {value!r}"
        raise TypeError(msg)


class _MetabaseEntity(_MetabaseResponseBase):
    id: int | str | None = None
    name: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class CurrentUserResponse(_MetabaseEntity):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    common_name: str | None = None
    is_superuser: bool | None = None
    locale: str | None = None


class Database(_MetabaseEntity):
    engine: str | None = None
    details: dict[str, Any] = Field(default_factory=dict)


class Card(_MetabaseEntity):
    display: str | None = None
    description: str | None = None
    dataset_query: dict[str, Any] | None = None


class Dashboard(_MetabaseEntity):
    description: str | None = None
    collection_id: int | str | None = None


ResponseT = TypeVar("ResponseT", bound=BaseModel)


class ListDatabasesResponse(BaseModel):
    databases: list[Database] = Field(default_factory=list)
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if values is None:
            return {"databases": []}

        if isinstance(values, list):
            return {"databases": values}

        if isinstance(values, dict):
            dict_values = cast(dict[str, object], values)
            if "databases" in dict_values and isinstance(dict_values["databases"], list):
                return dict_values
            if "data" in dict_values and isinstance(dict_values["data"], list):
                remainder = dict(dict_values)
                del remainder["data"]
                return {"databases": dict_values["data"], **remainder}
            if "items" in dict_values and isinstance(dict_values["items"], list):
                remainder = dict(dict_values)
                del remainder["items"]
                return {"databases": dict_values["items"], **remainder}
            return {"databases": [], "raw": dict_values}

        return {"databases": [], "raw": values}


class _BaseMetabaseRequest[ResponseT](BaseModel):
    model_config = ConfigDict(extra="allow")

    endpoint_method: ClassVar[str]
    endpoint_path: ClassVar[str]

    def resolve_path(self) -> str:
        return self.endpoint_path

    def request_params(self) -> dict[str, str | int | bool | float | None]:
        return {}

    def request_body(self) -> JSONValue | None:
        return None

    async def execute(self, client: MetabaseRequestClient, response_model: type[BaseModel]) -> ResponseT:
        payload = await client.request(
            self.endpoint_method,
            self.resolve_path(),
            params=self.request_params(),
            json_data=self.request_body(),
        )
        return cast(ResponseT, response_model.model_validate(payload or {}))

    def execute_sync(self, client: MetabaseRequestClient, response_model: type[BaseModel]) -> ResponseT:
        return asyncio.run(self.execute(client, response_model))


class CurrentUserRequest(_BaseMetabaseRequest[CurrentUserResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/current"

    async def do(self, client: MetabaseRequestClient) -> CurrentUserResponse:
        return await self.execute(client, CurrentUserResponse)

    def do_sync(self, client: MetabaseRequestClient) -> CurrentUserResponse:
        return self.execute_sync(client, CurrentUserResponse)


class ListDatabasesRequest(_BaseMetabaseRequest[ListDatabasesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> ListDatabasesResponse:
        return await self.execute(client, ListDatabasesResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListDatabasesResponse:
        return self.execute_sync(client, ListDatabasesResponse)


class CreateDatabaseRequest(_BaseMetabaseRequest[Database]):
    name: str
    engine: str
    details: dict[str, Any] = Field(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetCardRequest(_BaseMetabaseRequest[Card]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class GetDashboardRequest(_BaseMetabaseRequest[Dashboard]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}"

    async def do(self, client: MetabaseRequestClient) -> Dashboard:
        return await self.execute(client, Dashboard)

    def do_sync(self, client: MetabaseRequestClient) -> Dashboard:
        return self.execute_sync(client, Dashboard)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"
