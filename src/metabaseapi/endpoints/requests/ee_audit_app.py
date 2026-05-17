from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_audit_app import EeAuditAppExportResponse
from metabaseapi.endpoints.responses.ee_audit_app import EeAuditAppUserAuditInfoResponse
from metabaseapi.endpoints.responses.ee_audit_app import EeAuditAppUserSubscriptionsDeleteResponse


class PostEeAuditAppAnalyticsDevExportRequest(EndpointRequest[EeAuditAppExportResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/audit-app/analytics-dev/export"
    response_model = EeAuditAppExportResponse


class GetEeAuditAppUserAuditInfoRequest(EndpointRequest[EeAuditAppUserAuditInfoResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/audit-app/user/audit-info"
    response_model = EeAuditAppUserAuditInfoResponse


class DeleteEeAuditAppUserSubscriptionsRequest(EndpointRequest[EeAuditAppUserSubscriptionsDeleteResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/audit-app/user/{id}/subscriptions"
    response_model = EeAuditAppUserSubscriptionsDeleteResponse
