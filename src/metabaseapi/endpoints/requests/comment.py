from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class GetCommentMentionsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/comment/mentions"
    response_model: ClassVar[object] = GenericOperationResponse


class UpdateCommentRequest(EndpointRequest[GenericOperationResponse]):
    comment_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/comment/{comment_id}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return self.endpoint_path.format(comment_id=self.comment_id)

    def request_body(self) -> JSONValue:
        return self.body


class GetCommentRequest(EndpointRequest[GenericOperationResponse]):
    model: str | None = None
    model_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/comment"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.model is not None:
            params["model"] = self.model
        if self.model_id is not None:
            params["model-id"] = self.model_id
        return params


class PostCommentRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/comment"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCommentRequest(EndpointRequest[GenericOperationResponse]):
    comment_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/comment/{comment_id}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/comment/{self.comment_id}"


class PostCommentReactionRequest(EndpointRequest[GenericOperationResponse]):
    comment_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/comment/{comment_id}/reaction"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return self.endpoint_path.format(comment_id=self.comment_id)

    def request_body(self) -> JSONValue:
        return self.body
