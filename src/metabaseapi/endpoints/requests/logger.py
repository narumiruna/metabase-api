from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.logger import LoggerAdjustmentDeleteResponse
from metabaseapi.endpoints.responses.logger import LoggerAdjustmentResponse
from metabaseapi.endpoints.responses.logger import LoggerLogsResponse
from metabaseapi.endpoints.responses.logger import LoggerPresetsResponse


class CreateLoggerAdjustmentRequest(EndpointRequest[LoggerAdjustmentResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/logger/adjustment"
    response_model = LoggerAdjustmentResponse


class DeleteLoggerAdjustmentRequest(EndpointRequest[LoggerAdjustmentDeleteResponse]):
    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/logger/adjustment"
    response_model = LoggerAdjustmentDeleteResponse


class GetLoggerLogsRequest(EndpointRequest[LoggerLogsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/logger/logs"
    response_model = LoggerLogsResponse


class GetLoggerPresetsRequest(EndpointRequest[LoggerPresetsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/logger/presets"
    response_model = LoggerPresetsResponse
