from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload


class ListCommentsResponse(BaseModel):
    comments: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "comments")


class CommentMentionsResponse(BaseModel):
    mentions: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "mentions")


class _CommentOperationResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    text: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class CreateCommentResponse(_CommentOperationResponse):
    pass


class UpdateCommentResponse(_CommentOperationResponse):
    pass


class DeleteCommentResponse(_CommentOperationResponse):
    pass


class CommentReactionResponse(_CommentOperationResponse):
    pass
