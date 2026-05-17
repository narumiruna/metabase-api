from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

JSONValue = str | int | float | bool | None | list[object] | dict[str, object]
QueryParamPrimitive = str | int | float | bool | None
QueryParamValue = QueryParamPrimitive | list[QueryParamPrimitive]
SUPPORTED_HTTP_METHODS = frozenset({"DELETE", "GET", "PATCH", "POST", "PUT"})


class APIRequestModel(BaseModel):
    method: str
    path: str
    params: dict[str, QueryParamValue] = Field(default_factory=dict)
    body: JSONValue | None = None

    @field_validator("method", mode="before")
    @classmethod
    def normalize_method(cls, value: object) -> str:
        if not isinstance(value, str):
            msg = "method must be DELETE, GET, PATCH, POST, or PUT"
            raise TypeError(msg)

        method = value.upper()
        if method not in SUPPORTED_HTTP_METHODS:
            msg = "method must be DELETE, GET, PATCH, POST, or PUT"
            raise ValueError(msg)
        return method


class APIResponseModel(BaseModel):
    status_code: int
    payload: JSONValue | None = None
    content_type: str | None = None
