from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.requests.bug_reporting import GetBugReportingConnectionPoolDetailsRequest
from metabaseapi.endpoints.requests.bug_reporting import GetBugReportingDetailsRequest
from metabaseapi.endpoints.responses import GenericOperationResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def bug_reporting_connection_pool_details_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetBugReportingConnectionPoolDetailsRequest())


async def bug_reporting_details_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetBugReportingDetailsRequest())


__all__ = [
    "bug_reporting_connection_pool_details_typed",
    "bug_reporting_details_typed",
]
