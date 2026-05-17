from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.database import ListDatabasesResponse
from metabaseapi.wire import JSONValue


class ListDatabasesRequest(EndpointRequest[ListDatabasesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database"
    response_model = ListDatabasesResponse


class CreateDatabaseRequest(EndpointRequest[Database]):
    name: str
    engine: str
    details: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database"
    response_model = Database

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetDatabaseRequest(EndpointRequest[Database]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{database_id}"
    response_model = Database
