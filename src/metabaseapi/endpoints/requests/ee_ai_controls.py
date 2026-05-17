from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_ai_controls import EeAiControlsGroupUsageLimitsResponse
from metabaseapi.endpoints.responses.ee_ai_controls import EeAiControlsPermissionsResponse
from metabaseapi.endpoints.responses.ee_ai_controls import EeAiControlsTenantUsageLimitsResponse
from metabaseapi.endpoints.responses.ee_ai_controls import EeAiControlsUsageLimitResponse


class GetEeAiControlsPermissionsRequest(EndpointRequest[EeAiControlsPermissionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/permissions"
    response_model = EeAiControlsPermissionsResponse


class PutEeAiControlsPermissionsRequest(EndpointRequest[EeAiControlsPermissionsResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/permissions"
    response_model = EeAiControlsPermissionsResponse


class EnableEeAiControlsAdvancedPermissionsRequest(EndpointRequest[EeAiControlsPermissionsResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/permissions/advanced"
    response_model = EeAiControlsPermissionsResponse


class DisableEeAiControlsAdvancedPermissionsRequest(EndpointRequest[EeAiControlsPermissionsResponse]):
    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/permissions/advanced"
    response_model = EeAiControlsPermissionsResponse


class GetEeAiControlsUsageInstanceRequest(EndpointRequest[EeAiControlsUsageLimitResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/instance"
    response_model = EeAiControlsUsageLimitResponse


class PutEeAiControlsUsageInstanceRequest(EndpointRequest[EeAiControlsUsageLimitResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/instance"
    response_model = EeAiControlsUsageLimitResponse


class GetEeAiControlsUsageTenantRequest(EndpointRequest[EeAiControlsTenantUsageLimitsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/tenant"
    response_model = EeAiControlsTenantUsageLimitsResponse


class GetEeAiControlsUsageTenantIdRequest(EndpointRequest[EeAiControlsUsageLimitResponse]):
    tenant_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/tenant/{tenant_id}"
    response_model = EeAiControlsUsageLimitResponse


class PutEeAiControlsUsageTenantIdRequest(EndpointRequest[EeAiControlsUsageLimitResponse]):
    tenant_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/tenant/{tenant_id}"
    response_model = EeAiControlsUsageLimitResponse


class GetEeAiControlsUsageGroupRequest(EndpointRequest[EeAiControlsGroupUsageLimitsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/group"
    response_model = EeAiControlsGroupUsageLimitsResponse


class GetEeAiControlsUsageGroupIdRequest(EndpointRequest[EeAiControlsUsageLimitResponse]):
    group_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/group/{group_id}"
    response_model = EeAiControlsUsageLimitResponse


class PutEeAiControlsUsageGroupIdRequest(EndpointRequest[EeAiControlsUsageLimitResponse]):
    group_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/ai-controls/usage/group/{group_id}"
    response_model = EeAiControlsUsageLimitResponse
