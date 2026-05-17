from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_metabot import EeMetabotUsageResponse


class GetEeMetabotUsageRequest(EndpointRequest[EeMetabotUsageResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/metabot/usage"
    response_model = EeMetabotUsageResponse
