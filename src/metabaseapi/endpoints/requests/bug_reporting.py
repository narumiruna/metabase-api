from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.bug_reporting import BugReportingConnectionPoolDetailsResponse
from metabaseapi.endpoints.responses.bug_reporting import BugReportingDetailsResponse


class GetBugReportingConnectionPoolDetailsRequest(EndpointRequest[BugReportingConnectionPoolDetailsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/connection-pool-details"
    response_model = BugReportingConnectionPoolDetailsResponse


class GetBugReportingDetailsRequest(EndpointRequest[BugReportingDetailsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/details"
    response_model = BugReportingDetailsResponse
