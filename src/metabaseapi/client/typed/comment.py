from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.comment import DeleteCommentRequest
from metabaseapi.endpoints.requests.comment import GetCommentMentionsRequest
from metabaseapi.endpoints.requests.comment import GetCommentRequest
from metabaseapi.endpoints.requests.comment import PostCommentReactionRequest
from metabaseapi.endpoints.requests.comment import PostCommentRequest
from metabaseapi.endpoints.requests.comment import UpdateCommentRequest
from metabaseapi.endpoints.responses import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def delete_comment_typed(client: MetabaseClient, comment_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteCommentRequest(comment_id=comment_id))


async def get_comment_mentions_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCommentMentionsRequest())


async def update_comment_typed(
    client: MetabaseClient, comment_id: int | str, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(UpdateCommentRequest(comment_id=comment_id, body=dict(body)))


async def post_comment_reaction_typed(
    client: MetabaseClient,
    comment_id: int | str,
    body: dict[str, object],
) -> GenericOperationResponse:
    return await client.run(PostCommentReactionRequest(comment_id=comment_id, body=dict(body)))


async def get_comment_typed(
    client: MetabaseClient,
    *,
    model: str | None = None,
    model_id: int | str | None = None,
) -> GenericOperationResponse:
    return await client.run(GetCommentRequest(model=model, model_id=model_id))


async def create_comment_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(PostCommentRequest(body=dict(body)))


__all__ = [
    "create_comment_typed",
    "delete_comment_typed",
    "get_comment_mentions_typed",
    "get_comment_typed",
    "post_comment_reaction_typed",
    "update_comment_typed",
]
