from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.google import GoogleSettingsResponse


class UpdateGoogleSettingsRequest(EndpointRequest[GoogleSettingsResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/google/settings"
    response_model = GoogleSettingsResponse
