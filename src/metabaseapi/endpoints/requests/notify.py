from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.notify import NotifyAttachedDatawarehouseResponse
from metabaseapi.endpoints.responses.notify import NotifyDatabaseNewTableResponse
from metabaseapi.endpoints.responses.notify import NotifyDatabaseResponse


class NotifyAttachedDatawarehouseRequest(EndpointRequest[NotifyAttachedDatawarehouseResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notify/db/attached_datawarehouse"
    response_model = NotifyAttachedDatawarehouseResponse


class NotifyDatabaseRequest(EndpointRequest[NotifyDatabaseResponse]):
    database_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notify/db/{database_id}"
    response_model = NotifyDatabaseResponse


class NotifyDatabaseNewTableRequest(EndpointRequest[NotifyDatabaseNewTableResponse]):
    database_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/notify/db/{database_id}/new-table"
    response_model = NotifyDatabaseNewTableResponse
