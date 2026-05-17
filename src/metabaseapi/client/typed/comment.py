from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import DeleteCommentRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetCommentMentionsRequest
from metabaseapi.metabase import GetCommentRequest
from metabaseapi.metabase import PostCommentReactionRequest
from metabaseapi.metabase import PostCommentRequest
from metabaseapi.metabase import UpdateCommentRequest

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for comment endpoints."""

    async def delete_comment_typed(self: MetabaseClient, comment_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteCommentRequest(comment_id=comment_id))

    async def get_comment_mentions_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCommentMentionsRequest())

    async def update_comment_typed(
        self: MetabaseClient, comment_id: int | str, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(UpdateCommentRequest(comment_id=comment_id, body=dict(body)))

    async def post_comment_reaction_typed(
        self: MetabaseClient,
        comment_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(PostCommentReactionRequest(comment_id=comment_id, body=dict(body)))

    async def get_comment_typed(
        self: MetabaseClient,
        *,
        model: str | None = None,
        model_id: int | str | None = None,
    ) -> GenericOperationResponse:
        return await self.run(GetCommentRequest(model=model, model_id=model_id))

    async def create_comment_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(PostCommentRequest(body=dict(body)))


__all__ = ["_MetabaseClientTypedMixin"]
