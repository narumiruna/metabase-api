from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.execution import _BaseMetabaseRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListChannelsResponse
from metabaseapi.wire import JSONValue


class ListChannelsRequest(_BaseMetabaseRequest[ListChannelsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel"

    async def do(self, client: MetabaseRequestClient) -> ListChannelsResponse:
        return await self.execute(client, ListChannelsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListChannelsResponse:
        return self.execute_sync(client, ListChannelsResponse)


class CreateChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class TestChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    __test__ = False
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel/test"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    channel_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/channel/{self.channel_id}"


class UpdateChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    channel_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/channel/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/channel/{self.channel_id}"

    def request_body(self) -> JSONValue:
        return self.body
