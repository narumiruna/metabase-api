from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Alert
from metabaseapi.endpoints.requests.alert import DeleteAlertSubscriptionRequest
from metabaseapi.endpoints.requests.alert import GetAlertRequest
from metabaseapi.endpoints.requests.alert import ListAlertsRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListAlertsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_alerts_typed(client: MetabaseClient, *, user_id: int | str | None = None) -> ListAlertsResponse:
    return await client.run(ListAlertsRequest(user_id=user_id))


async def get_alert_typed(client: MetabaseClient, alert_id: int | str) -> Alert:
    return await client.run(GetAlertRequest(alert_id=alert_id))


async def delete_alert_subscription_typed(client: MetabaseClient, alert_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteAlertSubscriptionRequest(alert_id=alert_id))


__all__ = [
    "delete_alert_subscription_typed",
    "get_alert_typed",
    "list_alerts_typed",
]
