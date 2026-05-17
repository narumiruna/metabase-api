from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.email import DeleteEmailSettingsResponse
from metabaseapi.endpoints.responses.email import EmailSettingsResponse
from metabaseapi.endpoints.responses.email import TestEmailResponse


class UpdateEmailSettingsRequest(EndpointRequest[EmailSettingsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/email"
    response_model = EmailSettingsResponse


class DeleteEmailSettingsRequest(EndpointRequest[DeleteEmailSettingsResponse]):
    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/email"
    response_model = DeleteEmailSettingsResponse


class TestEmailRequest(EndpointRequest[TestEmailResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/email/test"
    response_model = TestEmailResponse
