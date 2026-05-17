from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import CreateChannelRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetChannelRequest
from metabaseapi.metabase import ListChannelsRequest
from metabaseapi.metabase import ListChannelsResponse
from metabaseapi.metabase import TestChannelRequest
from metabaseapi.metabase import UpdateChannelRequest

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for channel endpoints."""

    async def list_channels_typed(self: MetabaseClient) -> ListChannelsResponse:
        return await self.run(ListChannelsRequest())

    async def create_channel_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(CreateChannelRequest(body=body))

    async def test_channel_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(TestChannelRequest(body=body))

    async def get_channel_typed(self: MetabaseClient, channel_id: int | str) -> GenericOperationResponse:
        return await self.run(GetChannelRequest(channel_id=channel_id))

    async def update_channel_typed(
        self: MetabaseClient, channel_id: int | str, body: dict[str, object]
    ) -> GenericOperationResponse:
        return await self.run(UpdateChannelRequest(channel_id=channel_id, body=body))


__all__ = ["_MetabaseClientTypedMixin"]
