from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import Bookmark
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.bookmark import ListBookmarksResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class ListBookmarksRequest(EndpointRequest[ListBookmarksResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bookmark"
    response_model: ClassVar[_ResponseModel] = ListBookmarksResponse


class UpdateBookmarkOrderingRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/bookmark/ordering"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class CreateBookmarkRequest(EndpointRequest[Bookmark]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{item_id}"
    response_model: ClassVar[_ResponseModel] = Bookmark


class DeleteBookmarkRequest(EndpointRequest[GenericOperationResponse]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{item_id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse
