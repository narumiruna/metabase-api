from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_logs import EeQueryExecutionLogsResponse


class GetEeLogsQueryExecutionRequest(EndpointRequest[EeQueryExecutionLogsResponse]):
    year_month: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/logs/query_execution/{year_month}"
    response_model = EeQueryExecutionLogsResponse
