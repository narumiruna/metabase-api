from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.database import ListDatabasesResponse
from metabaseapi.wire import JSONValue


class ListDatabasesRequest(EndpointRequest[ListDatabasesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> ListDatabasesResponse:
        return await self.execute(client, ListDatabasesResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListDatabasesResponse:
        return self.execute_sync(client, ListDatabasesResponse)


class CreateDatabaseRequest(EndpointRequest[Database]):
    name: str
    engine: str
    details: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetDatabaseRequest(EndpointRequest[Database]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{id}"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def resolve_path(self) -> str:
        return f"/api/database/{self.database_id}"
