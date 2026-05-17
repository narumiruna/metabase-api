from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import Bookmark
from metabaseapi.metabase import CreateBookmarkRequest
from metabaseapi.metabase import DeleteBookmarkRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import ListBookmarksRequest
from metabaseapi.metabase import ListBookmarksResponse
from metabaseapi.metabase import UpdateBookmarkOrderingRequest

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for bookmark endpoints."""

    async def list_bookmarks_typed(self: MetabaseClient) -> ListBookmarksResponse:
        return await self.run(ListBookmarksRequest())

    async def update_bookmark_ordering_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(UpdateBookmarkOrderingRequest(body=body))

    async def create_bookmark_typed(self: MetabaseClient, model: str, item_id: int | str) -> Bookmark:
        return await self.run(CreateBookmarkRequest(model=model, item_id=item_id))

    async def delete_bookmark_typed(self: MetabaseClient, model: str, item_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteBookmarkRequest(model=model, item_id=item_id))


__all__ = ["_MetabaseClientTypedMixin"]
