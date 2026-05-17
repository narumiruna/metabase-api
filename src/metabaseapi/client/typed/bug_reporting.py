from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetBugReportingConnectionPoolDetailsRequest
from metabaseapi.metabase import GetBugReportingDetailsRequest

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for bug-reporting endpoints."""

    async def bug_reporting_connection_pool_details_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetBugReportingConnectionPoolDetailsRequest())

    async def bug_reporting_details_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetBugReportingDetailsRequest())


__all__ = ["_MetabaseClientTypedMixin"]
