from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Action
from metabaseapi.endpoints.requests.action import CreateActionPublicLinkRequest
from metabaseapi.endpoints.requests.action import CreateActionRequest
from metabaseapi.endpoints.requests.action import DeleteActionPublicLinkRequest
from metabaseapi.endpoints.requests.action import DeleteActionRequest
from metabaseapi.endpoints.requests.action import ExecuteActionRequest
from metabaseapi.endpoints.requests.action import GetActionExecuteRequest
from metabaseapi.endpoints.requests.action import GetActionRequest
from metabaseapi.endpoints.requests.action import ListActionsRequest
from metabaseapi.endpoints.requests.action import ListPublicActionsRequest
from metabaseapi.endpoints.requests.action import UpdateActionRequest
from metabaseapi.endpoints.responses import ActionExecutionResponse
from metabaseapi.endpoints.responses import ListActionsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_actions_typed(client: MetabaseClient, *, model_id: int | str | None = None) -> ListActionsResponse:
    return await client.run(ListActionsRequest(model_id=model_id))


async def create_action_typed(client: MetabaseClient, body: dict[str, object]) -> Action:
    return await client.run(CreateActionRequest(body=body))


async def list_public_actions_typed(client: MetabaseClient) -> ListActionsResponse:
    return await client.run(ListPublicActionsRequest())


async def get_action_typed(client: MetabaseClient, action_id: int | str) -> Action:
    return await client.run(GetActionRequest(action_id=action_id))


async def delete_action_typed(client: MetabaseClient, action_id: int | str) -> ActionExecutionResponse:
    return await client.run(DeleteActionRequest(action_id=action_id))


async def get_action_execute_typed(
    client: MetabaseClient,
    action_id: int | str,
    *,
    parameters: dict[str, object] | None = None,
) -> ActionExecutionResponse:
    return await client.run(GetActionExecuteRequest(action_id=action_id, parameters=parameters or {}))


async def update_action_typed(client: MetabaseClient, action_id: int | str, body: dict[str, object]) -> Action:
    return await client.run(UpdateActionRequest(action_id=action_id, body=body))


async def execute_action_typed(
    client: MetabaseClient,
    action_id: int | str,
    *,
    parameters: dict[str, object] | None = None,
) -> ActionExecutionResponse:
    return await client.run(ExecuteActionRequest(action_id=action_id, parameters=parameters or {}))


async def create_action_public_link_typed(client: MetabaseClient, action_id: int | str) -> ActionExecutionResponse:
    return await client.run(CreateActionPublicLinkRequest(action_id=action_id))


async def delete_action_public_link_typed(client: MetabaseClient, action_id: int | str) -> ActionExecutionResponse:
    return await client.run(DeleteActionPublicLinkRequest(action_id=action_id))


__all__ = [
    "create_action_public_link_typed",
    "create_action_typed",
    "delete_action_public_link_typed",
    "delete_action_typed",
    "execute_action_typed",
    "get_action_execute_typed",
    "get_action_typed",
    "list_actions_typed",
    "list_public_actions_typed",
    "update_action_typed",
]
