from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_alerts(client: MetabaseClient, *, user_id: int | str | None = None) -> JSONValue | None:
    params = {"user_id": user_id} if user_id is not None else None
    return await client.get("/api/alert", params=params)


async def get_alert(client: MetabaseClient, alert_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/alert/{alert_id}")


async def delete_alert_subscription(client: MetabaseClient, alert_id: int | str) -> JSONValue | None:
    return await client.delete(f"/api/alert/{alert_id}/subscription")


__all__ = [
    "delete_alert_subscription",
    "get_alert",
    "list_alerts",
]
