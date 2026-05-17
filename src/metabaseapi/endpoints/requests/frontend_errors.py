from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.frontend_errors import FrontendErrorReportResponse


class ReportFrontendErrorRequest(EndpointRequest[FrontendErrorReportResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/frontend-errors"
    response_model = FrontendErrorReportResponse
