from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_database_routing import EeDatabaseRoutingDatabaseResponse


class PostEeDatabaseRoutingDestinationDatabaseRequest(EndpointRequest[EeDatabaseRoutingDatabaseResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/database-routing/destination-database"
    response_model = EeDatabaseRoutingDatabaseResponse


class PutEeDatabaseRoutingRouterDatabaseIdRequest(EndpointRequest[EeDatabaseRoutingDatabaseResponse]):
    id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/database-routing/router-database/{id}"
    response_model = EeDatabaseRoutingDatabaseResponse
