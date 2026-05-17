from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_database_replication import EeDatabaseReplicationConnectionResponse


class PostEeDatabaseReplicationConnectionDatabaseIdRequest(EndpointRequest[EeDatabaseReplicationConnectionResponse]):
    database_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/database-replication/connection/{database_id}"
    response_model = EeDatabaseReplicationConnectionResponse


class DeleteEeDatabaseReplicationConnectionDatabaseIdRequest(EndpointRequest[EeDatabaseReplicationConnectionResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/database-replication/connection/{database_id}"
    response_model = EeDatabaseReplicationConnectionResponse


class PostEeDatabaseReplicationConnectionDatabaseIdPreviewRequest(
    EndpointRequest[EeDatabaseReplicationConnectionResponse]
):
    database_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/database-replication/connection/{database_id}/preview"
    response_model = EeDatabaseReplicationConnectionResponse
