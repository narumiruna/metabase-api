from __future__ import annotations

from typing import ClassVar
from typing import Protocol
from typing import TypeVar
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class _MetabaseRequestClient(Protocol):
    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, QueryParamValue] | None = ...,
        json_data: JSONValue | None = ...,
    ) -> object: ...


ResponseT = TypeVar("ResponseT", bound=BaseModel)
_ResponseModel = type[BaseModel]


class EndpointRequest[ResponseT](BaseModel):
    model_config = ConfigDict(extra="forbid")

    endpoint_method: ClassVar[str]
    endpoint_path: ClassVar[str]
    response_model: ClassVar[_ResponseModel]

    def resolve_path(self) -> str:
        if "{" not in self.endpoint_path:
            return self.endpoint_path
        values = self.model_dump(mode="python", exclude_none=False)
        format_values = values | {key.replace("_", "-"): value for key, value in values.items()}
        try:
            return self.endpoint_path.format_map(format_values)
        except KeyError:
            return self.endpoint_path

    def request_params(self) -> dict[str, QueryParamValue]:
        return {}

    def request_body(self) -> JSONValue | None:
        if hasattr(self, "body"):
            return cast("JSONValue | None", self.body)
        return None

    async def do(self, client: _MetabaseRequestClient) -> ResponseT:
        payload = await client._request(
            self.endpoint_method,
            self.resolve_path(),
            params=self.request_params(),
            json_data=self.request_body(),
        )
        return cast(ResponseT, self.response_model.model_validate(payload or {}))


__all__ = ["EndpointRequest"]
