from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_action_v2 import EeActionV2ExecuteFormResponse
from metabaseapi.endpoints.responses.ee_action_v2 import EeActionV2ExecuteResponse


class EeActionV2ExecuteRequest(EndpointRequest[EeActionV2ExecuteResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/action-v2/execute"
    response_model = EeActionV2ExecuteResponse


class EeActionV2ExecuteBulkRequest(EndpointRequest[EeActionV2ExecuteResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/action-v2/execute-bulk"
    response_model = EeActionV2ExecuteResponse


class EeActionV2ExecuteFormRequest(EndpointRequest[EeActionV2ExecuteFormResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/action-v2/execute-form"
    response_model = EeActionV2ExecuteFormResponse
