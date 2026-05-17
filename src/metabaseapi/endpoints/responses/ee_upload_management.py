from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_known_payload
from metabaseapi.endpoints._response_payload import normalize_model_list_payload
from metabaseapi.endpoints.entities import Table
from metabaseapi.wire import JSONValue


class EeUploadManagementTablesResponse(BaseModel):
    tables: list[Table] = PydanticField(default_factory=list)
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_model_list_payload(values, cls.model_fields, "tables")


class EeUploadManagementDeleteTableResponse(BaseModel):
    id: int | str | None = None
    archived_cards: list[JSONValue] = PydanticField(default_factory=list)
    ok: bool | None = None
    result: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_known_payload(values, cls.model_fields, "result")
