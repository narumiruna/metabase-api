from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import cast

from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for action endpoints."""

    async def list_actions(self: MetabaseClient, *, model_id: int | str | None = None) -> JSONValue | None:
        params = {"model-id": model_id} if model_id is not None else None
        return await self.get("/api/action", params=params)

    async def create_action(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/action", body=dict(body))

    async def list_public_actions(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/action/public")

    async def get_action(self: MetabaseClient, action_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/action/{action_id}")

    async def delete_action(self: MetabaseClient, action_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/action/{action_id}")

    async def get_action_execute(
        self: MetabaseClient,
        action_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        query_params = cast(Mapping[str, QueryParamValue] | None, parameters)
        return await self.get(f"/api/action/{action_id}/execute", params=query_params)

    async def update_action(self: MetabaseClient, action_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put(f"/api/action/{action_id}", body=dict(body))

    async def execute_action(
        self: MetabaseClient,
        action_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(
            f"/api/action/{action_id}/execute",
            body={"parameters": dict(parameters or {})},
        )

    async def create_action_public_link(self: MetabaseClient, action_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/action/{action_id}/public_link")

    async def delete_action_public_link(self: MetabaseClient, action_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/action/{action_id}/public_link")


__all__ = ["_MetabaseClientRawMixin"]
