from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload


class ListChannelsResponse(BaseModel):
    channels: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "channels")


class _ChannelOperationResponse(BaseModel):
    id: int | str | None = None
    name: str | None = None
    ok: bool | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class CreateChannelResponse(_ChannelOperationResponse):
    pass


class ChannelTestResponse(_ChannelOperationResponse):
    pass


class ChannelResponse(_ChannelOperationResponse):
    pass


class UpdateChannelResponse(_ChannelOperationResponse):
    pass
