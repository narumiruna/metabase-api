from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.login_history import CurrentLoginHistoryResponse


class GetCurrentLoginHistoryRequest(EndpointRequest[CurrentLoginHistoryResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/login-history/current"
    response_model = CurrentLoginHistoryResponse
