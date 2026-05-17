from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.slack import SlackAppInfoResponse
from metabaseapi.endpoints.responses.slack import SlackBugReportResponse
from metabaseapi.endpoints.responses.slack import SlackManifestResponse
from metabaseapi.endpoints.responses.slack import SlackSettingsResponse


class GetSlackAppInfoRequest(EndpointRequest[SlackAppInfoResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/slack/app-info"
    response_model = SlackAppInfoResponse


class CreateSlackBugReportRequest(EndpointRequest[SlackBugReportResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/slack/bug-report"
    response_model = SlackBugReportResponse


class GetSlackManifestRequest(EndpointRequest[SlackManifestResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/slack/manifest"
    response_model = SlackManifestResponse


class UpdateSlackSettingsRequest(EndpointRequest[SlackSettingsResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/slack/settings"
    response_model = SlackSettingsResponse
