from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.entities import ActivityItem
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.activity import ActivityMutationResponse
from metabaseapi.endpoints.responses.activity import ListActivityItemsResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class GetMostRecentlyViewedDashboardRequest(EndpointRequest[ActivityItem]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/most_recently_viewed_dashboard"
    response_model: ClassVar[_ResponseModel] = ActivityItem


class ListPopularItemsRequest(EndpointRequest[ListActivityItemsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/popular_items"
    response_model: ClassVar[_ResponseModel] = ListActivityItemsResponse


class ListRecentViewsRequest(EndpointRequest[ListActivityItemsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/recent_views"
    response_model: ClassVar[_ResponseModel] = ListActivityItemsResponse


class ListRecentsRequest(EndpointRequest[ListActivityItemsResponse]):
    context: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/recents"
    response_model: ClassVar[_ResponseModel] = ListActivityItemsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.context is None:
            return {}
        return {"context": self.context}


class CreateRecentRequest(EndpointRequest[ActivityMutationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/activity/recents"
    response_model: ClassVar[_ResponseModel] = ActivityMutationResponse

    def request_body(self) -> JSONValue:
        return self.body
