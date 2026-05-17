from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_fields_payload
from metabaseapi.endpoints._response_payload import normalize_named_payload
from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.wire import JSONValue


class DocumentResponse(BaseModel):
    document: dict[str, Any] = PydanticField(default_factory=dict)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_named_payload(values, "document")


class ListDocumentsResponse(BaseModel):
    documents: list[dict[str, Any]] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "documents")


class ListPublicDocumentsResponse(ListDocumentsResponse):
    pass


class _DocumentStatusResponse(BaseModel):
    id: int | str | None = None
    ok: bool | None = None
    uuid: str | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_fields_payload(values, cls.model_fields)


class DeleteDocumentResponse(_DocumentStatusResponse):
    ok: bool | None = None


class CreateDocumentPublicLinkResponse(_DocumentStatusResponse):
    uuid: str | None = None


class DeleteDocumentPublicLinkResponse(_DocumentStatusResponse):
    ok: bool | None = None


class DocumentQueryExportResponse(BaseModel):
    value: JSONValue | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        if not isinstance(values, dict):
            return {"value": values}
        return normalize_known_payload(values, cls.model_fields, "result")
