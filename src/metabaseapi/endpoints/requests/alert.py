from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.entities import Alert
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.alert import ListAlertsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import QueryParamValue


class ListAlertsRequest(EndpointRequest[ListAlertsResponse]):
    user_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/alert"
    response_model = ListAlertsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.user_id is None:
            return {}
        return {"user_id": self.user_id}


class GetAlertRequest(EndpointRequest[Alert]):
    alert_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/alert/{alert_id}"
    response_model = Alert


class DeleteAlertSubscriptionRequest(EndpointRequest[GenericOperationResponse]):
    alert_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/alert/{alert_id}/subscription"
    response_model = GenericOperationResponse
