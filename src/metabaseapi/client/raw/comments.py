from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for comment endpoints."""

    async def get_comment(
        self: MetabaseClient,
        *,
        model: str | None = None,
        model_id: int | str | None = None,
    ) -> JSONValue | None:
        params: dict[str, QueryParamValue] = {}
        if model is not None:
            params["model"] = model
        if model_id is not None:
            params["model-id"] = model_id
        return await self.get("/api/comment", params=params or None)

    async def get_comment_mentions(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/comment/mentions")

    async def create_comment(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/comment", body=dict(body))

    async def update_comment(self: MetabaseClient, comment_id: int | str, body: dict[str, object]) -> JSONValue | None:
        return await self.put(f"/api/comment/{comment_id}", body=dict(body))

    async def post_comment_reaction(
        self: MetabaseClient, comment_id: int | str, body: dict[str, object]
    ) -> JSONValue | None:
        return await self.post(f"/api/comment/{comment_id}/reaction", body=dict(body))

    async def delete_comment(self: MetabaseClient, comment_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/comment/{comment_id}")


__all__ = ["_MetabaseClientRawMixin"]
