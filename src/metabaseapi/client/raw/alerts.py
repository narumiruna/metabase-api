from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin façade."""

    async def list_alerts(self: MetabaseClient, *, user_id: int | str | None = None) -> JSONValue | None:
        params = {"user_id": user_id} if user_id is not None else None
        return await self.get("/api/alert", params=params)

    async def get_alert(self: MetabaseClient, alert_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/alert/{alert_id}")

    async def delete_alert_subscription(self: MetabaseClient, alert_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/alert/{alert_id}/subscription")


__all__ = ["_MetabaseClientRawMixin"]
