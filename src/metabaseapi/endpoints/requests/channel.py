from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.channel import ChannelResponse
from metabaseapi.endpoints.responses.channel import ChannelTestResponse
from metabaseapi.endpoints.responses.channel import CreateChannelResponse
from metabaseapi.endpoints.responses.channel import ListChannelsResponse
from metabaseapi.endpoints.responses.channel import UpdateChannelResponse


class ListChannelsRequest(EndpointRequest[ListChannelsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel"
    response_model = ListChannelsResponse


class CreateChannelRequest(EndpointRequest[CreateChannelResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel"
    response_model = CreateChannelResponse


class TestChannelRequest(EndpointRequest[ChannelTestResponse]):
    __test__ = False
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel/test"
    response_model = ChannelTestResponse


class GetChannelRequest(EndpointRequest[ChannelResponse]):
    channel_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel/{channel_id}"
    response_model = ChannelResponse


class UpdateChannelRequest(EndpointRequest[UpdateChannelResponse]):
    channel_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/channel/{channel_id}"
    response_model = UpdateChannelResponse
