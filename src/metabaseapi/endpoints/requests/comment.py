from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.comment import CommentMentionsResponse
from metabaseapi.endpoints.responses.comment import CommentReactionResponse
from metabaseapi.endpoints.responses.comment import CreateCommentResponse
from metabaseapi.endpoints.responses.comment import DeleteCommentResponse
from metabaseapi.endpoints.responses.comment import ListCommentsResponse
from metabaseapi.endpoints.responses.comment import UpdateCommentResponse
from metabaseapi.wire import QueryParamValue


class GetCommentMentionsRequest(EndpointRequest[CommentMentionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/comment/mentions"
    response_model = CommentMentionsResponse


class UpdateCommentRequest(EndpointRequest[UpdateCommentResponse]):
    comment_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/comment/{comment_id}"
    response_model = UpdateCommentResponse


class GetCommentRequest(EndpointRequest[ListCommentsResponse]):
    model: str | None = None
    model_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/comment"
    response_model = ListCommentsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.model is not None:
            params["model"] = self.model
        if self.model_id is not None:
            params["model-id"] = self.model_id
        return params


class PostCommentRequest(EndpointRequest[CreateCommentResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/comment"
    response_model = CreateCommentResponse


class DeleteCommentRequest(EndpointRequest[DeleteCommentResponse]):
    comment_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/comment/{comment_id}"
    response_model = DeleteCommentResponse


class PostCommentReactionRequest(EndpointRequest[CommentReactionResponse]):
    comment_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/comment/{comment_id}/reaction"
    response_model = CommentReactionResponse
