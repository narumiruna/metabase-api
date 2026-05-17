from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.cloud_migration import CancelCloudMigrationResponse
from metabaseapi.endpoints.responses.cloud_migration import CloudMigrationStatusResponse
from metabaseapi.endpoints.responses.cloud_migration import CreateCloudMigrationResponse


class CreateCloudMigrationRequest(EndpointRequest[CreateCloudMigrationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cloud-migration"
    response_model = CreateCloudMigrationResponse


class GetCloudMigrationRequest(EndpointRequest[CloudMigrationStatusResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/cloud-migration"
    response_model = CloudMigrationStatusResponse


class CancelCloudMigrationRequest(EndpointRequest[CancelCloudMigrationResponse]):
    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/cloud-migration/cancel"
    response_model = CancelCloudMigrationResponse
