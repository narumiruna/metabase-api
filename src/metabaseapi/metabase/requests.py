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
from metabaseapi.metabase.responses import CardsDashboardsResponse
from metabaseapi.metabase.responses import GenericOperationResponse
from metabaseapi.metabase.responses import ListActionsResponse
from metabaseapi.metabase.responses import ListActivityItemsResponse
from metabaseapi.metabase.responses import ListAlertsResponse
from metabaseapi.metabase.responses import ListApiKeysResponse
from metabaseapi.metabase.responses import ListBookmarksResponse
from metabaseapi.metabase.responses import ListCardsResponse
from metabaseapi.metabase.responses import ListChannelsResponse
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


class GetCacheRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    limit: int | None = None
    offset: int | None = None
    sort_column: str | None = None
    sort_direction: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/cache"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.sort_column is not None:
            params["sort_column"] = self.sort_column
        if self.sort_direction is not None:
            params["sort_direction"] = self.sort_direction
        return params


class ListChannelsRequest(_BaseMetabaseRequest[ListChannelsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel"

    async def do(self, client: MetabaseRequestClient) -> ListChannelsResponse:
        return await self.execute(client, ListChannelsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListChannelsResponse:
        return self.execute_sync(client, ListChannelsResponse)


class CreateChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class TestChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    __test__ = False
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/channel/test"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    channel_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/channel/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/channel/{self.channel_id}"


class UpdateChannelRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    channel_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/channel/{id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/channel/{self.channel_id}"

    def request_body(self) -> JSONValue:
        return self.body


class PutCacheRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/cache"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCacheRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/cache"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body or None


class InvalidateCacheRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cache/invalidate"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_params(self) -> dict[str, QueryParamValue]:
        return dict(self.params)


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


class CreateCloudMigrationRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cloud-migration"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetCloudMigrationRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/cloud-migration"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class CancelCloudMigrationRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/cloud-migration/cancel"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


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


class GetCardCollectionsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_ids: list[int | str] | None = None
    collection_id: int | str | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/collections"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        body: dict[str, object] = {}
        if self.card_ids is not None:
            body["card_ids"] = self.card_ids
        if self.collection_id is not None:
            body["collection_id"] = self.collection_id
        return body or None


class GetCardEmbeddableRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/embeddable"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class PostCardPivotQueryRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/pivot/{card-id}/query"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/pivot/{self.card_id}/query"

    def request_body(self) -> JSONValue:
        return self.body or None


class GetCardPublicRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/public"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class CardParamsSearchRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str
    query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/search/{query}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/search/{self.query}"


class CardParamsValuesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/values"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/values"


class CreateCardPublicLinkRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/public_link"


class DeleteCardPublicLinkRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/public_link"


class CardQueryRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query"

    def request_body(self) -> JSONValue:
        return self.body or None


class CardQueryExportRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str
    export_format: str
    body: dict[str, Any] = PydanticField(default_factory=dict)
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query/{export_format}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query/{self.export_format}"

    def request_body(self) -> JSONValue:
        return self.body or None

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class UpdateCardRequest(_BaseMetabaseRequest[Card]):
    card_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCardRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class CopyCardRequest(_BaseMetabaseRequest[Card]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/copy"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/copy"

    def request_body(self) -> JSONValue:
        return self.body or None


class GetCardDashboardsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/dashboards"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/dashboards"


class CardRemappingRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/remapping"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/remapping"


class GetCardQueryMetadataRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query_metadata"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query_metadata"


class GetCardSeriesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/series"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/series"


class CardsDashboardsRequest(_BaseMetabaseRequest[CardsDashboardsResponse]):
    card_ids: list[int | str]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/dashboards"

    async def do(self, client: MetabaseRequestClient) -> CardsDashboardsResponse:
        return await self.execute(client, CardsDashboardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> CardsDashboardsResponse:
        return self.execute_sync(client, CardsDashboardsResponse)

    def request_body(self) -> JSONValue:
        return {"card_ids": self.card_ids}


class MoveCardsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/move"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


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


class CreateCollectionRequest(_BaseMetabaseRequest[Collection]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection"

    async def do(self, client: MetabaseRequestClient) -> Collection:
        return await self.execute(client, Collection)

    def do_sync(self, client: MetabaseRequestClient) -> Collection:
        return self.execute_sync(client, Collection)

    def request_body(self) -> JSONValue:
        return self.body


class GetCollectionGraphRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/graph"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class PutCollectionGraphRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/collection/graph"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class GetCollectionRootRequest(_BaseMetabaseRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root"

    async def do(self, client: MetabaseRequestClient) -> Collection:
        return await self.execute(client, Collection)

    def do_sync(self, client: MetabaseRequestClient) -> Collection:
        return self.execute_sync(client, Collection)


class GetCollectionTreeRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/tree"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetCollectionRootDashboardQuestionCandidatesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/dashboard-question-candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetCollectionRootItemsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/items"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class GetCollectionDashboardQuestionCandidatesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/dashboard-question-candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}/dashboard-question-candidates"


class GetCollectionItemsRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/items"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}/items"


class GetCollectionTrashRequest(_BaseMetabaseRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/trash"

    async def do(self, client: MetabaseRequestClient) -> Collection:
        return await self.execute(client, Collection)

    def do_sync(self, client: MetabaseRequestClient) -> Collection:
        return self.execute_sync(client, Collection)


class PostCollectionRootMoveDashboardQuestionCandidatesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/root/move-dashboard-question-candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body


class PostCollectionMoveDashboardQuestionCandidatesRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)
    collection_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/move-dashboard-question-candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}/move-dashboard-question-candidates"

    def request_body(self) -> JSONValue:
        return self.body


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


class PutCollectionRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    body: dict[str, Any]
    collection_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCollectionRequest(_BaseMetabaseRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

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
    "CancelCloudMigrationRequest",
    "CardParamsSearchRequest",
    "CardParamsValuesRequest",
    "CardQueryExportRequest",
    "CardQueryRequest",
    "CardRemappingRequest",
    "CardsDashboardsRequest",
    "CopyCardRequest",
    "CountApiKeysRequest",
    "CreateActionPublicLinkRequest",
    "CreateActionRequest",
    "CreateAnalyticsEventBatchRequest",
    "CreateApiKeyRequest",
    "CreateBookmarkRequest",
    "CreateCardPublicLinkRequest",
    "CreateCardRequest",
    "CreateChannelRequest",
    "CreateCloudMigrationRequest",
    "CreateCollectionRequest",
    "CreateDatabaseRequest",
    "CreateRecentRequest",
    "CurrentUserRequest",
    "DeleteActionPublicLinkRequest",
    "DeleteActionRequest",
    "DeleteAlertSubscriptionRequest",
    "DeleteApiKeyRequest",
    "DeleteBookmarkRequest",
    "DeleteCacheRequest",
    "DeleteCardPublicLinkRequest",
    "DeleteCardRequest",
    "DeleteCollectionRequest",
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
    "GetCacheRequest",
    "GetCardCollectionsRequest",
    "GetCardDashboardsRequest",
    "GetCardEmbeddableRequest",
    "GetCardPublicRequest",
    "GetCardQueryMetadataRequest",
    "GetCardRequest",
    "GetCardSeriesRequest",
    "GetChannelRequest",
    "GetCloudMigrationRequest",
    "GetCollectionDashboardQuestionCandidatesRequest",
    "GetCollectionGraphRequest",
    "GetCollectionItemsRequest",
    "GetCollectionRequest",
    "GetCollectionRootDashboardQuestionCandidatesRequest",
    "GetCollectionRootItemsRequest",
    "GetCollectionRootRequest",
    "GetCollectionTrashRequest",
    "GetCollectionTreeRequest",
    "GetDashboardRequest",
    "GetDatabaseRequest",
    "GetFieldRequest",
    "GetMostRecentlyViewedDashboardRequest",
    "GetTableRequest",
    "GetUserRequest",
    "InvalidateCacheRequest",
    "ListActionsRequest",
    "ListAlertsRequest",
    "ListApiKeysRequest",
    "ListBookmarksRequest",
    "ListCardsRequest",
    "ListChannelsRequest",
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
    "MoveCardsRequest",
    "PostCardPivotQueryRequest",
    "PostCollectionMoveDashboardQuestionCandidatesRequest",
    "PostCollectionRootMoveDashboardQuestionCandidatesRequest",
    "PutCacheRequest",
    "PutCollectionGraphRequest",
    "PutCollectionRequest",
    "RegenerateApiKeyRequest",
    "TestChannelRequest",
    "UpdateActionRequest",
    "UpdateApiKeyRequest",
    "UpdateBookmarkOrderingRequest",
    "UpdateCardRequest",
    "UpdateChannelRequest",
]
