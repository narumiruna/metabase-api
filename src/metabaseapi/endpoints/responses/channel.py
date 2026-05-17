from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
from metabaseapi.wire import JSONValue


class ListChannelsResponse(BaseModel):
    channels: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "channels")


class _ChannelOperationResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class CreateChannelResponse(_ChannelOperationResponse):
    pass


class ChannelTestResponse(_ChannelOperationResponse):
    pass


class ChannelResponse(_ChannelOperationResponse):
    pass


class UpdateChannelResponse(_ChannelOperationResponse):
    pass
