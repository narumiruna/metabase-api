from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_billing import EeBillingResponse


class GetEeBillingRequest(EndpointRequest[EeBillingResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/billing"
    response_model = EeBillingResponse
