from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.channel import CreateChannelRequest
from metabaseapi.endpoints.requests.channel import GetChannelRequest
from metabaseapi.endpoints.requests.channel import ListChannelsRequest
from metabaseapi.endpoints.requests.channel import TestChannelRequest
from metabaseapi.endpoints.requests.channel import UpdateChannelRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListChannelsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_channels_typed(client: MetabaseClient) -> ListChannelsResponse:
    return await client.run(ListChannelsRequest())


async def create_channel_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(CreateChannelRequest(body=body))


async def test_channel_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(TestChannelRequest(body=body))


async def get_channel_typed(client: MetabaseClient, channel_id: int | str) -> GenericOperationResponse:
    return await client.run(GetChannelRequest(channel_id=channel_id))


async def update_channel_typed(
    client: MetabaseClient, channel_id: int | str, body: dict[str, object]
) -> GenericOperationResponse:
    return await client.run(UpdateChannelRequest(channel_id=channel_id, body=body))


__all__ = [
    "create_channel_typed",
    "get_channel_typed",
    "list_channels_typed",
    "test_channel_typed",
    "update_channel_typed",
]
