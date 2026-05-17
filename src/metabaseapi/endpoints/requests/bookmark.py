from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import Bookmark
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.bookmark import BookmarkOrderingUpdateResponse
from metabaseapi.endpoints.responses.bookmark import DeleteBookmarkResponse
from metabaseapi.endpoints.responses.bookmark import ListBookmarksResponse


class ListBookmarksRequest(EndpointRequest[ListBookmarksResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bookmark"
    response_model = ListBookmarksResponse


class UpdateBookmarkOrderingRequest(EndpointRequest[BookmarkOrderingUpdateResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/bookmark/ordering"
    response_model = BookmarkOrderingUpdateResponse


class CreateBookmarkRequest(EndpointRequest[Bookmark]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{item_id}"
    response_model = Bookmark


class DeleteBookmarkRequest(EndpointRequest[DeleteBookmarkResponse]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{item_id}"
    response_model = DeleteBookmarkResponse
