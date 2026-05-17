from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import Alert
from metabaseapi.metabase import DeleteAlertSubscriptionRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetAlertRequest
from metabaseapi.metabase import ListAlertsRequest
from metabaseapi.metabase import ListAlertsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed alert helpers."""

    async def list_alerts_typed(self: MetabaseClient, *, user_id: int | str | None = None) -> ListAlertsResponse:
        return await self.run(ListAlertsRequest(user_id=user_id))

    async def get_alert_typed(self: MetabaseClient, alert_id: int | str) -> Alert:
        return await self.run(GetAlertRequest(alert_id=alert_id))

    async def delete_alert_subscription_typed(self: MetabaseClient, alert_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteAlertSubscriptionRequest(alert_id=alert_id))


__all__ = ["_MetabaseClientTypedMixin"]
