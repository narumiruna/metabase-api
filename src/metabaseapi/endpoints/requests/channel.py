from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.channel import ListChannelsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class ListChannelsRequest(EndpointRequest[ListChannelsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel"
    response_model: ClassVar[_ResponseModel] = ListChannelsResponse


class CreateChannelRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body


class TestChannelRequest(EndpointRequest[GenericOperationResponse]):
    __test__ = False
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel/test"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body


class GetChannelRequest(EndpointRequest[GenericOperationResponse]):
    channel_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel/{id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/channel/{self.channel_id}"


class UpdateChannelRequest(EndpointRequest[GenericOperationResponse]):
    channel_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/channel/{id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/channel/{self.channel_id}"

    def request_body(self) -> JSONValue:
        return self.body
