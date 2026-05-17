from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class CreateCloudMigrationRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cloud-migration"
    response_model = GenericOperationResponse


class GetCloudMigrationRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/cloud-migration"
    response_model = GenericOperationResponse


class CancelCloudMigrationRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/cloud-migration/cancel"
    response_model = GenericOperationResponse
