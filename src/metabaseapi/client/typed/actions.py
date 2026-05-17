from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import Action
from metabaseapi.metabase import ActionExecutionResponse
from metabaseapi.metabase import CreateActionPublicLinkRequest
from metabaseapi.metabase import CreateActionRequest
from metabaseapi.metabase import DeleteActionPublicLinkRequest
from metabaseapi.metabase import DeleteActionRequest
from metabaseapi.metabase import ExecuteActionRequest
from metabaseapi.metabase import GetActionExecuteRequest
from metabaseapi.metabase import GetActionRequest
from metabaseapi.metabase import ListActionsRequest
from metabaseapi.metabase import ListActionsResponse
from metabaseapi.metabase import ListPublicActionsRequest
from metabaseapi.metabase import UpdateActionRequest

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for action endpoints."""

    async def list_actions_typed(self: MetabaseClient, *, model_id: int | str | None = None) -> ListActionsResponse:
        return await self.run(ListActionsRequest(model_id=model_id))

    async def create_action_typed(self: MetabaseClient, body: dict[str, object]) -> Action:
        return await self.run(CreateActionRequest(body=body))

    async def list_public_actions_typed(self: MetabaseClient) -> ListActionsResponse:
        return await self.run(ListPublicActionsRequest())

    async def get_action_typed(self: MetabaseClient, action_id: int | str) -> Action:
        return await self.run(GetActionRequest(action_id=action_id))

    async def delete_action_typed(self: MetabaseClient, action_id: int | str) -> ActionExecutionResponse:
        return await self.run(DeleteActionRequest(action_id=action_id))

    async def get_action_execute_typed(
        self: MetabaseClient,
        action_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> ActionExecutionResponse:
        return await self.run(GetActionExecuteRequest(action_id=action_id, parameters=parameters or {}))

    async def update_action_typed(self: MetabaseClient, action_id: int | str, body: dict[str, object]) -> Action:
        return await self.run(UpdateActionRequest(action_id=action_id, body=body))

    async def execute_action_typed(
        self: MetabaseClient,
        action_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> ActionExecutionResponse:
        return await self.run(ExecuteActionRequest(action_id=action_id, parameters=parameters or {}))

    async def create_action_public_link_typed(self: MetabaseClient, action_id: int | str) -> ActionExecutionResponse:
        return await self.run(CreateActionPublicLinkRequest(action_id=action_id))

    async def delete_action_public_link_typed(self: MetabaseClient, action_id: int | str) -> ActionExecutionResponse:
        return await self.run(DeleteActionPublicLinkRequest(action_id=action_id))


__all__ = ["_MetabaseClientTypedMixin"]
