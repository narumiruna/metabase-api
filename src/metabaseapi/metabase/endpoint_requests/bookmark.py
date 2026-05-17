from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.metabase.entities import Bookmark
from metabaseapi.metabase.request_base import MetabaseRequestClient
from metabaseapi.metabase.request_base import _BaseMetabaseRequest
from metabaseapi.metabase.responses import GenericOperationResponse
from metabaseapi.metabase.responses import ListBookmarksResponse
from metabaseapi.models import JSONValue


class ListBookmarksRequest(_BaseMetabaseRequest[ListBookmarksResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bookmark"

    async def do(self, client: MetabaseRequestClient) -> ListBookmarksResponse:
        return await self.execute(client, ListBookmarksResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListBookmarksResponse:
        return self.execute_sync(client, ListBookmarksResponse)


class UpdateBookmarkOrderingRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/bookmark/ordering"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class CreateBookmarkRequest(_BaseMetabaseRequest[Bookmark]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{id}"

    async def do(self, client: MetabaseRequestClient) -> Bookmark:
        return await self.execute(client, Bookmark)

    def do_sync(self, client: MetabaseRequestClient) -> Bookmark:
        return self.execute_sync(client, Bookmark)

    def resolve_path(self) -> str:
        return f"/api/bookmark/{self.model}/{self.item_id}"


class DeleteBookmarkRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/bookmark/{self.model}/{self.item_id}"
