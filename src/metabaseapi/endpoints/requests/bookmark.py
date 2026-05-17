from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import Bookmark
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.bookmark import ListBookmarksResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class ListBookmarksRequest(EndpointRequest[ListBookmarksResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bookmark"
    response_model: ClassVar[object] = ListBookmarksResponse


class UpdateBookmarkOrderingRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/bookmark/ordering"
    response_model: ClassVar[object] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body


class CreateBookmarkRequest(EndpointRequest[Bookmark]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{id}"
    response_model: ClassVar[object] = Bookmark

    def resolve_path(self) -> str:
        return f"/api/bookmark/{self.model}/{self.item_id}"


class DeleteBookmarkRequest(EndpointRequest[GenericOperationResponse]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{id}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/bookmark/{self.model}/{self.item_id}"
