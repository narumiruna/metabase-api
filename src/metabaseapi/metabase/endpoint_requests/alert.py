from __future__ import annotations

from typing import ClassVar

from metabaseapi.metabase.entities import Alert
from metabaseapi.metabase.request_base import MetabaseRequestClient
from metabaseapi.metabase.request_base import _BaseMetabaseRequest
from metabaseapi.metabase.responses import GenericOperationResponse
from metabaseapi.metabase.responses import ListAlertsResponse
from metabaseapi.models import QueryParamValue


class ListAlertsRequest(_BaseMetabaseRequest[ListAlertsResponse]):
    user_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/alert"

    async def do(self, client: MetabaseRequestClient) -> ListAlertsResponse:
        return await self.execute(client, ListAlertsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListAlertsResponse:
        return self.execute_sync(client, ListAlertsResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.user_id is None:
            return {}
        return {"user_id": self.user_id}


class GetAlertRequest(_BaseMetabaseRequest[Alert]):
    alert_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/alert/{id}"

    async def do(self, client: MetabaseRequestClient) -> Alert:
        return await self.execute(client, Alert)

    def do_sync(self, client: MetabaseRequestClient) -> Alert:
        return self.execute_sync(client, Alert)

    def resolve_path(self) -> str:
        return f"/api/alert/{self.alert_id}"


class DeleteAlertSubscriptionRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    alert_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/alert/{id}/subscription"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/alert/{self.alert_id}/subscription"
