from __future__ import annotations

import asyncio
from typing import ClassVar
from typing import Protocol
from typing import TypeVar
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict

from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class MetabaseRequestClient(Protocol):
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, QueryParamValue] | None = ...,
        json_data: JSONValue | None = ...,
    ) -> object: ...


ResponseT = TypeVar("ResponseT", bound=BaseModel)


class EndpointRequest[ResponseT](BaseModel):
    model_config = ConfigDict(extra="allow")

    endpoint_method: ClassVar[str]
    endpoint_path: ClassVar[str]

    def resolve_path(self) -> str:
        return self.endpoint_path

    def request_params(self) -> dict[str, QueryParamValue]:
        return {}

    def request_body(self) -> JSONValue | None:
        return None

    async def execute(self, client: MetabaseRequestClient, response_model: type[BaseModel]) -> ResponseT:
        payload = await client.request(
            self.endpoint_method,
            self.resolve_path(),
            params=self.request_params(),
            json_data=self.request_body(),
        )
        return cast(ResponseT, response_model.model_validate(payload or {}))

    def execute_sync(self, client: MetabaseRequestClient, response_model: type[BaseModel]) -> ResponseT:
        return asyncio.run(self.execute(client, response_model))


__all__ = ["EndpointRequest", "MetabaseRequestClient"]
