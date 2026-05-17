from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Bookmark
from metabaseapi.endpoints.requests.bookmark import CreateBookmarkRequest
from metabaseapi.endpoints.requests.bookmark import DeleteBookmarkRequest
from metabaseapi.endpoints.requests.bookmark import ListBookmarksRequest
from metabaseapi.endpoints.requests.bookmark import UpdateBookmarkOrderingRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListBookmarksResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_bookmarks_typed(client: MetabaseClient) -> ListBookmarksResponse:
    return await client.run(ListBookmarksRequest())


async def update_bookmark_ordering_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(UpdateBookmarkOrderingRequest(body=body))


async def create_bookmark_typed(client: MetabaseClient, model: str, item_id: int | str) -> Bookmark:
    return await client.run(CreateBookmarkRequest(model=model, item_id=item_id))


async def delete_bookmark_typed(client: MetabaseClient, model: str, item_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteBookmarkRequest(model=model, item_id=item_id))


__all__ = [
    "create_bookmark_typed",
    "delete_bookmark_typed",
    "list_bookmarks_typed",
    "update_bookmark_ordering_typed",
]
