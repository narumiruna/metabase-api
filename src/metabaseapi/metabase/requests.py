from __future__ import annotations

import asyncio
from typing import Any
from typing import ClassVar
from typing import Protocol
from typing import TypeVar
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField

from metabaseapi.metabase.entities import Action
from metabaseapi.metabase.entities import Card
from metabaseapi.metabase.entities import Collection
from metabaseapi.metabase.entities import CurrentUserResponse
from metabaseapi.metabase.entities import Dashboard
from metabaseapi.metabase.entities import Database
from metabaseapi.metabase.entities import MetabaseField
from metabaseapi.metabase.entities import Table
from metabaseapi.metabase.entities import User
from metabaseapi.metabase.responses import ActionExecutionResponse
from metabaseapi.metabase.responses import ListActionsResponse
from metabaseapi.metabase.responses import ListCardsResponse
from metabaseapi.metabase.responses import ListCollectionsResponse
from metabaseapi.metabase.responses import ListDashboardsResponse
from metabaseapi.metabase.responses import ListDatabasesResponse
from metabaseapi.metabase.responses import ListTablesResponse
from metabaseapi.metabase.responses import ListUsersResponse
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue


class MetabaseRequestClient(Protocol):
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, QueryParamValue] | None = ...,
        json_data: JSONValue | None = ...,
    ) -> object: ...


ResponseT = TypeVar("ResponseT", bound=BaseModel)


class _BaseMetabaseRequest[ResponseT](BaseModel):
    model_config = ConfigDict(extra="allow")

    endpoint_method: ClassVar[str]
    endpoint_path: ClassVar[str]

    def resolve_path(self) -> str:
        return self.endpoint_path

    def request_params(self) -> dict[str, QueryParamValue]:
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


class ListActionsRequest(_BaseMetabaseRequest[ListActionsResponse]):
    model_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action"

    async def do(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return await self.execute(client, ListActionsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return self.execute_sync(client, ListActionsResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.model_id is None:
            return {}
        return {"model-id": self.model_id}


class CreateActionRequest(_BaseMetabaseRequest[Action]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action"

    async def do(self, client: MetabaseRequestClient) -> Action:
        return await self.execute(client, Action)

    def do_sync(self, client: MetabaseRequestClient) -> Action:
        return self.execute_sync(client, Action)

    def request_body(self) -> JSONValue:
        return self.body


class ListPublicActionsRequest(_BaseMetabaseRequest[ListActionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/public"

    async def do(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return await self.execute(client, ListActionsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return self.execute_sync(client, ListActionsResponse)


class GetActionRequest(_BaseMetabaseRequest[Action]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/{action-id}"

    async def do(self, client: MetabaseRequestClient) -> Action:
        return await self.execute(client, Action)

    def do_sync(self, client: MetabaseRequestClient) -> Action:
        return self.execute_sync(client, Action)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}"


class DeleteActionRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/action/{action-id}"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}"


class GetActionExecuteRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/{action-id}/execute"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/execute"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class UpdateActionRequest(_BaseMetabaseRequest[Action]):
    action_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/action/{id}"

    async def do(self, client: MetabaseRequestClient) -> Action:
        return await self.execute(client, Action)

    def do_sync(self, client: MetabaseRequestClient) -> Action:
        return self.execute_sync(client, Action)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}"

    def request_body(self) -> JSONValue:
        return self.body


class ExecuteActionRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action/{id}/execute"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/execute"

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class CreateActionPublicLinkRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action/{id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/public_link"


class DeleteActionPublicLinkRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/action/{id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/public_link"


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
    details: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetDatabaseRequest(_BaseMetabaseRequest[Database]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{id}"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def resolve_path(self) -> str:
        return f"/api/database/{self.database_id}"


class ListCardsRequest(_BaseMetabaseRequest[ListCardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card"

    async def do(self, client: MetabaseRequestClient) -> ListCardsResponse:
        return await self.execute(client, ListCardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListCardsResponse:
        return self.execute_sync(client, ListCardsResponse)


class CreateCardRequest(_BaseMetabaseRequest[Card]):
    name: str
    dataset_query: dict[str, Any]
    display: str
    visualization_settings: dict[str, Any] = PydanticField(default_factory=dict)
    type: str | None = "question"
    collection_id: int | str | None = None
    description: str | None = None
    parameters: list[Any] | None = None
    result_metadata: list[Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

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


class ListDashboardsRequest(_BaseMetabaseRequest[ListDashboardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard"

    async def do(self, client: MetabaseRequestClient) -> ListDashboardsResponse:
        return await self.execute(client, ListDashboardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListDashboardsResponse:
        return self.execute_sync(client, ListDashboardsResponse)


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


class ListUsersRequest(_BaseMetabaseRequest[ListUsersResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user"

    async def do(self, client: MetabaseRequestClient) -> ListUsersResponse:
        return await self.execute(client, ListUsersResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListUsersResponse:
        return self.execute_sync(client, ListUsersResponse)


class GetUserRequest(_BaseMetabaseRequest[User]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"

    async def do(self, client: MetabaseRequestClient) -> User:
        return await self.execute(client, User)

    def do_sync(self, client: MetabaseRequestClient) -> User:
        return self.execute_sync(client, User)

    def resolve_path(self) -> str:
        return f"/api/user/{self.user_id}"


class ListCollectionsRequest(_BaseMetabaseRequest[ListCollectionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection"

    async def do(self, client: MetabaseRequestClient) -> ListCollectionsResponse:
        return await self.execute(client, ListCollectionsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListCollectionsResponse:
        return self.execute_sync(client, ListCollectionsResponse)


class GetCollectionRequest(_BaseMetabaseRequest[Collection]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"

    async def do(self, client: MetabaseRequestClient) -> Collection:
        return await self.execute(client, Collection)

    def do_sync(self, client: MetabaseRequestClient) -> Collection:
        return self.execute_sync(client, Collection)

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}"


class ListTablesRequest(_BaseMetabaseRequest[ListTablesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table"

    async def do(self, client: MetabaseRequestClient) -> ListTablesResponse:
        return await self.execute(client, ListTablesResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListTablesResponse:
        return self.execute_sync(client, ListTablesResponse)


class GetTableRequest(_BaseMetabaseRequest[Table]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}"

    async def do(self, client: MetabaseRequestClient) -> Table:
        return await self.execute(client, Table)

    def do_sync(self, client: MetabaseRequestClient) -> Table:
        return self.execute_sync(client, Table)

    def resolve_path(self) -> str:
        return f"/api/table/{self.table_id}"


class GetFieldRequest(_BaseMetabaseRequest[MetabaseField]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}"

    async def do(self, client: MetabaseRequestClient) -> MetabaseField:
        return await self.execute(client, MetabaseField)

    def do_sync(self, client: MetabaseRequestClient) -> MetabaseField:
        return self.execute_sync(client, MetabaseField)

    def resolve_path(self) -> str:
        return f"/api/field/{self.field_id}"


__all__ = [
    "CreateActionPublicLinkRequest",
    "CreateActionRequest",
    "CreateCardRequest",
    "CreateDatabaseRequest",
    "CurrentUserRequest",
    "DeleteActionPublicLinkRequest",
    "DeleteActionRequest",
    "ExecuteActionRequest",
    "GetActionExecuteRequest",
    "GetActionRequest",
    "GetCardRequest",
    "GetCollectionRequest",
    "GetDashboardRequest",
    "GetDatabaseRequest",
    "GetFieldRequest",
    "GetTableRequest",
    "GetUserRequest",
    "ListActionsRequest",
    "ListCardsRequest",
    "ListCollectionsRequest",
    "ListDashboardsRequest",
    "ListDatabasesRequest",
    "ListPublicActionsRequest",
    "ListTablesRequest",
    "ListUsersRequest",
    "MetabaseRequestClient",
    "UpdateActionRequest",
]
