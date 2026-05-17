from __future__ import annotations

import asyncio
from typing import Any
from typing import ClassVar
from typing import Protocol
from typing import TypeVar
from typing import cast

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField

from metabaseapi.metabase.entities import Action
from metabaseapi.metabase.entities import ActivityItem
from metabaseapi.metabase.entities import Alert
from metabaseapi.metabase.entities import ApiKey
from metabaseapi.metabase.entities import Bookmark
from metabaseapi.metabase.entities import Card
from metabaseapi.metabase.entities import Collection
from metabaseapi.metabase.entities import CurrentUserResponse
from metabaseapi.metabase.entities import Dashboard
from metabaseapi.metabase.entities import Database
from metabaseapi.metabase.entities import MetabaseField
from metabaseapi.metabase.entities import Table
from metabaseapi.metabase.entities import User
from metabaseapi.metabase.responses import ActionExecutionResponse
from metabaseapi.metabase.responses import ActivityMutationResponse
from metabaseapi.metabase.responses import AgentResponse
from metabaseapi.metabase.responses import GenericOperationResponse
from metabaseapi.metabase.responses import ListActionsResponse
from metabaseapi.metabase.responses import ListActivityItemsResponse
from metabaseapi.metabase.responses import ListAlertsResponse
from metabaseapi.metabase.responses import ListApiKeysResponse
from metabaseapi.metabase.responses import ListBookmarksResponse
from metabaseapi.metabase.responses import ListCardsResponse
from metabaseapi.metabase.responses import ListCollectionsResponse
from metabaseapi.metabase.responses import ListDashboardsResponse
from metabaseapi.metabase.responses import ListDatabasesResponse
from metabaseapi.metabase.responses import ListTablesResponse
from metabaseapi.metabase.responses import ListUsersResponse
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue


class MetabaseRequestClient(Protocol):
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, QueryParamValue] | None = ...,
        json_data: JSONValue | None = ...,
    ) -> object: ...


ResponseT = TypeVar("ResponseT", bound=BaseModel)


class _BaseMetabaseRequest[ResponseT](BaseModel):
    model_config = ConfigDict(extra="allow")

    endpoint_method: ClassVar[str]
    endpoint_path: ClassVar[str]

    def resolve_path(self) -> str:
        return self.endpoint_path

    def request_params(self) -> dict[str, QueryParamValue]:
        return {}

    def request_body(self) -> JSONValue | None:
        return None

    async def execute(self, client: MetabaseRequestClient, response_model: type[BaseModel]) -> ResponseT:
        payload = await client.request(
            self.endpoint_method,
            self.resolve_path(),
            params=self.request_params(),
            json_data=self.request_body(),
        )
        return cast(ResponseT, response_model.model_validate(payload or {}))

    def execute_sync(self, client: MetabaseRequestClient, response_model: type[BaseModel]) -> ResponseT:
        return asyncio.run(self.execute(client, response_model))


class ListActionsRequest(_BaseMetabaseRequest[ListActionsResponse]):
    model_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action"

    async def do(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return await self.execute(client, ListActionsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return self.execute_sync(client, ListActionsResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.model_id is None:
            return {}
        return {"model-id": self.model_id}


class CreateActionRequest(_BaseMetabaseRequest[Action]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action"

    async def do(self, client: MetabaseRequestClient) -> Action:
        return await self.execute(client, Action)

    def do_sync(self, client: MetabaseRequestClient) -> Action:
        return self.execute_sync(client, Action)

    def request_body(self) -> JSONValue:
        return self.body


class ListPublicActionsRequest(_BaseMetabaseRequest[ListActionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/public"

    async def do(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return await self.execute(client, ListActionsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActionsResponse:
        return self.execute_sync(client, ListActionsResponse)


class GetActionRequest(_BaseMetabaseRequest[Action]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/{action-id}"

    async def do(self, client: MetabaseRequestClient) -> Action:
        return await self.execute(client, Action)

    def do_sync(self, client: MetabaseRequestClient) -> Action:
        return self.execute_sync(client, Action)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}"


class DeleteActionRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/action/{action-id}"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}"


class GetActionExecuteRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/action/{action-id}/execute"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/execute"

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.parameters


class UpdateActionRequest(_BaseMetabaseRequest[Action]):
    action_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/action/{id}"

    async def do(self, client: MetabaseRequestClient) -> Action:
        return await self.execute(client, Action)

    def do_sync(self, client: MetabaseRequestClient) -> Action:
        return self.execute_sync(client, Action)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}"

    def request_body(self) -> JSONValue:
        return self.body


class ExecuteActionRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str
    parameters: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action/{id}/execute"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/execute"

    def request_body(self) -> JSONValue:
        return {"parameters": self.parameters}


class CreateActionPublicLinkRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/action/{id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/public_link"


class DeleteActionPublicLinkRequest(_BaseMetabaseRequest[ActionExecutionResponse]):
    action_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/action/{id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return await self.execute(client, ActionExecutionResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActionExecutionResponse:
        return self.execute_sync(client, ActionExecutionResponse)

    def resolve_path(self) -> str:
        return f"/api/action/{self.action_id}/public_link"


class ListBookmarksRequest(_BaseMetabaseRequest[ListBookmarksResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bookmark"

    async def do(self, client: MetabaseRequestClient) -> ListBookmarksResponse:
        return await self.execute(client, ListBookmarksResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListBookmarksResponse:
        return self.execute_sync(client, ListBookmarksResponse)


class UpdateBookmarkOrderingRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/bookmark/ordering"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class CreateBookmarkRequest(_BaseMetabaseRequest[Bookmark]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{id}"

    async def do(self, client: MetabaseRequestClient) -> Bookmark:
        return await self.execute(client, Bookmark)

    def do_sync(self, client: MetabaseRequestClient) -> Bookmark:
        return self.execute_sync(client, Bookmark)

    def resolve_path(self) -> str:
        return f"/api/bookmark/{self.model}/{self.item_id}"


class DeleteBookmarkRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    model: str
    item_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/bookmark/{model}/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/bookmark/{self.model}/{self.item_id}"


class GetBugReportingConnectionPoolDetailsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/connection-pool-details"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetBugReportingDetailsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/bug-reporting/details"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class AutomagicDashboardRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    path: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{path}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/{self.path.lstrip('/')}"


class AutomagicDatabaseCandidatesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/database/{id}/candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/database/{self.database_id}/candidates"


class AutomagicModelIndexPrimaryKeyRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    model_index_id: int | str
    primary_key_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/model_index/{model-index-id}/primary_key/{pk-id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/model_index/{self.model_index_id}/primary_key/{self.primary_key_id}"


class CreateApiKeyRequest(_BaseMetabaseRequest[ApiKey]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/api-key"

    async def do(self, client: MetabaseRequestClient) -> ApiKey:
        return await self.execute(client, ApiKey)

    def do_sync(self, client: MetabaseRequestClient) -> ApiKey:
        return self.execute_sync(client, ApiKey)

    def request_body(self) -> JSONValue:
        return self.body


class ListApiKeysRequest(_BaseMetabaseRequest[ListApiKeysResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key"

    async def do(self, client: MetabaseRequestClient) -> ListApiKeysResponse:
        return await self.execute(client, ListApiKeysResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListApiKeysResponse:
        return self.execute_sync(client, ListApiKeysResponse)


class CountApiKeysRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/api-key/count"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class UpdateApiKeyRequest(_BaseMetabaseRequest[ApiKey]):
    api_key_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}"

    async def do(self, client: MetabaseRequestClient) -> ApiKey:
        return await self.execute(client, ApiKey)

    def do_sync(self, client: MetabaseRequestClient) -> ApiKey:
        return self.execute_sync(client, ApiKey)

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteApiKeyRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}"


class RegenerateApiKeyRequest(_BaseMetabaseRequest[ApiKey]):
    api_key_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/api-key/{id}/regenerate"

    async def do(self, client: MetabaseRequestClient) -> ApiKey:
        return await self.execute(client, ApiKey)

    def do_sync(self, client: MetabaseRequestClient) -> ApiKey:
        return self.execute_sync(client, ApiKey)

    def resolve_path(self) -> str:
        return f"/api/api-key/{self.api_key_id}/regenerate"


class AnalyzeChartRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ai-entity-analysis/analyze-chart"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


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


class GetAnonymousStatsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/analytics/anonymous-stats"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class CreateAnalyticsEventBatchRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/analytics/internal"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class AgentExecuteRequest(_BaseMetabaseRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/execute"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetAgentMetricRequest(_BaseMetabaseRequest[AgentResponse]):
    metric_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/metric/{id}"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/metric/{self.metric_id}"


class GetAgentMetricFieldValuesRequest(_BaseMetabaseRequest[AgentResponse]):
    metric_id: int | str
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/metric/{id}/field/{field-id}/values"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/metric/{self.metric_id}/field/{self.field_id}/values"


class AgentPingRequest(_BaseMetabaseRequest[AgentResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/ping"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)


class AgentSearchRequest(_BaseMetabaseRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/search"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetAgentTableRequest(_BaseMetabaseRequest[AgentResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/table/{id}"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/table/{self.table_id}"


class GetAgentTableFieldValuesRequest(_BaseMetabaseRequest[AgentResponse]):
    table_id: int | str
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/table/{id}/field/{field-id}/values"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def resolve_path(self) -> str:
        return f"/api/agent/v1/table/{self.table_id}/field/{self.field_id}/values"


class AgentConstructQueryRequest(_BaseMetabaseRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v2/construct-query"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class AgentQueryRequest(_BaseMetabaseRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v2/query"

    async def do(self, client: MetabaseRequestClient) -> AgentResponse:
        return await self.execute(client, AgentResponse)

    def do_sync(self, client: MetabaseRequestClient) -> AgentResponse:
        return self.execute_sync(client, AgentResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetMostRecentlyViewedDashboardRequest(_BaseMetabaseRequest[ActivityItem]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/most_recently_viewed_dashboard"

    async def do(self, client: MetabaseRequestClient) -> ActivityItem:
        return await self.execute(client, ActivityItem)

    def do_sync(self, client: MetabaseRequestClient) -> ActivityItem:
        return self.execute_sync(client, ActivityItem)


class ListPopularItemsRequest(_BaseMetabaseRequest[ListActivityItemsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/popular_items"

    async def do(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return await self.execute(client, ListActivityItemsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return self.execute_sync(client, ListActivityItemsResponse)


class ListRecentViewsRequest(_BaseMetabaseRequest[ListActivityItemsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/recent_views"

    async def do(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return await self.execute(client, ListActivityItemsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return self.execute_sync(client, ListActivityItemsResponse)


class ListRecentsRequest(_BaseMetabaseRequest[ListActivityItemsResponse]):
    context: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/activity/recents"

    async def do(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return await self.execute(client, ListActivityItemsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListActivityItemsResponse:
        return self.execute_sync(client, ListActivityItemsResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.context is None:
            return {}
        return {"context": self.context}


class CreateRecentRequest(_BaseMetabaseRequest[ActivityMutationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/activity/recents"

    async def do(self, client: MetabaseRequestClient) -> ActivityMutationResponse:
        return await self.execute(client, ActivityMutationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ActivityMutationResponse:
        return self.execute_sync(client, ActivityMutationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class CurrentUserRequest(_BaseMetabaseRequest[CurrentUserResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/current"

    async def do(self, client: MetabaseRequestClient) -> CurrentUserResponse:
        return await self.execute(client, CurrentUserResponse)

    def do_sync(self, client: MetabaseRequestClient) -> CurrentUserResponse:
        return self.execute_sync(client, CurrentUserResponse)


class ListDatabasesRequest(_BaseMetabaseRequest[ListDatabasesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> ListDatabasesResponse:
        return await self.execute(client, ListDatabasesResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListDatabasesResponse:
        return self.execute_sync(client, ListDatabasesResponse)


class CreateDatabaseRequest(_BaseMetabaseRequest[Database]):
    name: str
    engine: str
    details: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/database"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetDatabaseRequest(_BaseMetabaseRequest[Database]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/database/{id}"

    async def do(self, client: MetabaseRequestClient) -> Database:
        return await self.execute(client, Database)

    def do_sync(self, client: MetabaseRequestClient) -> Database:
        return self.execute_sync(client, Database)

    def resolve_path(self) -> str:
        return f"/api/database/{self.database_id}"


class ListCardsRequest(_BaseMetabaseRequest[ListCardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card"

    async def do(self, client: MetabaseRequestClient) -> ListCardsResponse:
        return await self.execute(client, ListCardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListCardsResponse:
        return self.execute_sync(client, ListCardsResponse)


class CreateCardRequest(_BaseMetabaseRequest[Card]):
    name: str
    dataset_query: dict[str, Any]
    display: str
    visualization_settings: dict[str, Any] = PydanticField(default_factory=dict)
    type: str | None = "question"
    collection_id: int | str | None = None
    description: str | None = None
    parameters: list[Any] | None = None
    result_metadata: list[Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetCardRequest(_BaseMetabaseRequest[Card]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class ListDashboardsRequest(_BaseMetabaseRequest[ListDashboardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard"

    async def do(self, client: MetabaseRequestClient) -> ListDashboardsResponse:
        return await self.execute(client, ListDashboardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListDashboardsResponse:
        return self.execute_sync(client, ListDashboardsResponse)


class GetDashboardRequest(_BaseMetabaseRequest[Dashboard]):
    dashboard_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/dashboard/{dashboard-id}"

    async def do(self, client: MetabaseRequestClient) -> Dashboard:
        return await self.execute(client, Dashboard)

    def do_sync(self, client: MetabaseRequestClient) -> Dashboard:
        return self.execute_sync(client, Dashboard)

    def resolve_path(self) -> str:
        return f"/api/dashboard/{self.dashboard_id}"


class ListUsersRequest(_BaseMetabaseRequest[ListUsersResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user"

    async def do(self, client: MetabaseRequestClient) -> ListUsersResponse:
        return await self.execute(client, ListUsersResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListUsersResponse:
        return self.execute_sync(client, ListUsersResponse)


class GetUserRequest(_BaseMetabaseRequest[User]):
    user_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user/{user_id}"

    async def do(self, client: MetabaseRequestClient) -> User:
        return await self.execute(client, User)

    def do_sync(self, client: MetabaseRequestClient) -> User:
        return self.execute_sync(client, User)

    def resolve_path(self) -> str:
        return f"/api/user/{self.user_id}"


class ListCollectionsRequest(_BaseMetabaseRequest[ListCollectionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection"

    async def do(self, client: MetabaseRequestClient) -> ListCollectionsResponse:
        return await self.execute(client, ListCollectionsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListCollectionsResponse:
        return self.execute_sync(client, ListCollectionsResponse)


class GetCollectionRequest(_BaseMetabaseRequest[Collection]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"

    async def do(self, client: MetabaseRequestClient) -> Collection:
        return await self.execute(client, Collection)

    def do_sync(self, client: MetabaseRequestClient) -> Collection:
        return self.execute_sync(client, Collection)

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}"


class ListTablesRequest(_BaseMetabaseRequest[ListTablesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table"

    async def do(self, client: MetabaseRequestClient) -> ListTablesResponse:
        return await self.execute(client, ListTablesResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListTablesResponse:
        return self.execute_sync(client, ListTablesResponse)


class GetTableRequest(_BaseMetabaseRequest[Table]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/table/{table_id}"

    async def do(self, client: MetabaseRequestClient) -> Table:
        return await self.execute(client, Table)

    def do_sync(self, client: MetabaseRequestClient) -> Table:
        return self.execute_sync(client, Table)

    def resolve_path(self) -> str:
        return f"/api/table/{self.table_id}"


class GetFieldRequest(_BaseMetabaseRequest[MetabaseField]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}"

    async def do(self, client: MetabaseRequestClient) -> MetabaseField:
        return await self.execute(client, MetabaseField)

    def do_sync(self, client: MetabaseRequestClient) -> MetabaseField:
        return self.execute_sync(client, MetabaseField)

    def resolve_path(self) -> str:
        return f"/api/field/{self.field_id}"


__all__ = [
    "AgentConstructQueryRequest",
    "AgentExecuteRequest",
    "AgentPingRequest",
    "AgentQueryRequest",
    "AgentSearchRequest",
    "AnalyzeChartRequest",
    "AutomagicDashboardRequest",
    "AutomagicDatabaseCandidatesRequest",
    "AutomagicModelIndexPrimaryKeyRequest",
    "CountApiKeysRequest",
    "CreateActionPublicLinkRequest",
    "CreateActionRequest",
    "CreateAnalyticsEventBatchRequest",
    "CreateApiKeyRequest",
    "CreateBookmarkRequest",
    "CreateCardRequest",
    "CreateDatabaseRequest",
    "CreateRecentRequest",
    "CurrentUserRequest",
    "DeleteActionPublicLinkRequest",
    "DeleteActionRequest",
    "DeleteAlertSubscriptionRequest",
    "DeleteApiKeyRequest",
    "DeleteBookmarkRequest",
    "ExecuteActionRequest",
    "GetActionExecuteRequest",
    "GetActionRequest",
    "GetAgentMetricFieldValuesRequest",
    "GetAgentMetricRequest",
    "GetAgentTableFieldValuesRequest",
    "GetAgentTableRequest",
    "GetAlertRequest",
    "GetAnonymousStatsRequest",
    "GetBugReportingConnectionPoolDetailsRequest",
    "GetBugReportingDetailsRequest",
    "GetCardRequest",
    "GetCollectionRequest",
    "GetDashboardRequest",
    "GetDatabaseRequest",
    "GetFieldRequest",
    "GetMostRecentlyViewedDashboardRequest",
    "GetTableRequest",
    "GetUserRequest",
    "ListActionsRequest",
    "ListAlertsRequest",
    "ListApiKeysRequest",
    "ListBookmarksRequest",
    "ListCardsRequest",
    "ListCollectionsRequest",
    "ListDashboardsRequest",
    "ListDatabasesRequest",
    "ListPopularItemsRequest",
    "ListPublicActionsRequest",
    "ListRecentViewsRequest",
    "ListRecentsRequest",
    "ListTablesRequest",
    "ListUsersRequest",
    "MetabaseRequestClient",
    "RegenerateApiKeyRequest",
    "UpdateActionRequest",
    "UpdateApiKeyRequest",
    "UpdateBookmarkOrderingRequest",
]
