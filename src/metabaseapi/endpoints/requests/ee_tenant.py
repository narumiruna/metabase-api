from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_tenant import EeTenantResponse
from metabaseapi.endpoints.responses.ee_tenant import EeTenantsResponse


class PostEeTenantRequest(EndpointRequest[EeTenantResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/tenant"
    response_model = EeTenantResponse


class GetEeTenantRequest(EndpointRequest[EeTenantsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/tenant"
    response_model = EeTenantsResponse


class PutEeTenantIdRequest(EndpointRequest[EeTenantResponse]):
    tenant_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/tenant/{tenant_id}"
    response_model = EeTenantResponse


class GetEeTenantIdRequest(EndpointRequest[EeTenantResponse]):
    tenant_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/tenant/{tenant_id}"
    response_model = EeTenantResponse
