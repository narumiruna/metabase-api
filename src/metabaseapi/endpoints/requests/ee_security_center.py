from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_security_center import EeSecurityCenterAdvisoriesResponse
from metabaseapi.endpoints.responses.ee_security_center import EeSecurityCenterOperationResponse


class GetEeSecurityCenterRequest(EndpointRequest[EeSecurityCenterAdvisoriesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/security-center"
    response_model = EeSecurityCenterAdvisoriesResponse


class AcknowledgeEeSecurityCenterAdvisoriesRequest(EndpointRequest[EeSecurityCenterOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/security-center/acknowledge"
    response_model = EeSecurityCenterOperationResponse


class SyncEeSecurityCenterRequest(EndpointRequest[EeSecurityCenterOperationResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/security-center/sync"
    response_model = EeSecurityCenterOperationResponse


class TestEeSecurityCenterNotificationRequest(EndpointRequest[EeSecurityCenterOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/security-center/test-notification"
    response_model = EeSecurityCenterOperationResponse


class AcknowledgeEeSecurityCenterAdvisoryRequest(EndpointRequest[EeSecurityCenterOperationResponse]):
    advisory_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/security-center/{advisory_id}/acknowledge"
    response_model = EeSecurityCenterOperationResponse
