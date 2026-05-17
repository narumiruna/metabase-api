from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.metabase.entities import Action
from metabaseapi.metabase.request_base import MetabaseRequestClient
from metabaseapi.metabase.request_base import _BaseMetabaseRequest
from metabaseapi.metabase.responses import ActionExecutionResponse
from metabaseapi.metabase.responses import ListActionsResponse
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue


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
