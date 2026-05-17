from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol
from typing import TypeVar
from typing import cast

import httpx

from metabaseapi.errors import MetabaseDecodeError
from metabaseapi.errors import MetabaseHTTPStatusError
from metabaseapi.errors import MetabaseNetworkError
from metabaseapi.metabase import Action
from metabaseapi.metabase import ActionExecutionResponse
from metabaseapi.metabase import ActivityItem
from metabaseapi.metabase import ActivityMutationResponse
from metabaseapi.metabase import AgentConstructQueryRequest
from metabaseapi.metabase import AgentExecuteRequest
from metabaseapi.metabase import AgentPingRequest
from metabaseapi.metabase import AgentQueryRequest
from metabaseapi.metabase import AgentResponse
from metabaseapi.metabase import AgentSearchRequest
from metabaseapi.metabase import Alert
from metabaseapi.metabase import AnalyzeChartRequest
from metabaseapi.metabase import Card
from metabaseapi.metabase import Collection
from metabaseapi.metabase import CreateActionPublicLinkRequest
from metabaseapi.metabase import CreateActionRequest
from metabaseapi.metabase import CreateAnalyticsEventBatchRequest
from metabaseapi.metabase import CreateCardRequest
from metabaseapi.metabase import CreateDatabaseRequest
from metabaseapi.metabase import CreateRecentRequest
from metabaseapi.metabase import CurrentUserRequest
from metabaseapi.metabase import CurrentUserResponse
from metabaseapi.metabase import Dashboard
from metabaseapi.metabase import Database
from metabaseapi.metabase import DeleteActionPublicLinkRequest
from metabaseapi.metabase import DeleteActionRequest
from metabaseapi.metabase import DeleteAlertSubscriptionRequest
from metabaseapi.metabase import ExecuteActionRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetActionExecuteRequest
from metabaseapi.metabase import GetActionRequest
from metabaseapi.metabase import GetAgentMetricFieldValuesRequest
from metabaseapi.metabase import GetAgentMetricRequest
from metabaseapi.metabase import GetAgentTableFieldValuesRequest
from metabaseapi.metabase import GetAgentTableRequest
from metabaseapi.metabase import GetAlertRequest
from metabaseapi.metabase import GetAnonymousStatsRequest
from metabaseapi.metabase import GetCardRequest
from metabaseapi.metabase import GetCollectionRequest
from metabaseapi.metabase import GetDashboardRequest
from metabaseapi.metabase import GetDatabaseRequest
from metabaseapi.metabase import GetFieldRequest
from metabaseapi.metabase import GetMostRecentlyViewedDashboardRequest
from metabaseapi.metabase import GetTableRequest
from metabaseapi.metabase import GetUserRequest
from metabaseapi.metabase import ListActionsRequest
from metabaseapi.metabase import ListActionsResponse
from metabaseapi.metabase import ListActivityItemsResponse
from metabaseapi.metabase import ListAlertsRequest
from metabaseapi.metabase import ListAlertsResponse
from metabaseapi.metabase import ListCardsRequest
from metabaseapi.metabase import ListCardsResponse
from metabaseapi.metabase import ListCollectionsRequest
from metabaseapi.metabase import ListCollectionsResponse
from metabaseapi.metabase import ListDashboardsRequest
from metabaseapi.metabase import ListDashboardsResponse
from metabaseapi.metabase import ListDatabasesRequest
from metabaseapi.metabase import ListDatabasesResponse
from metabaseapi.metabase import ListPopularItemsRequest
from metabaseapi.metabase import ListPublicActionsRequest
from metabaseapi.metabase import ListRecentsRequest
from metabaseapi.metabase import ListRecentViewsRequest
from metabaseapi.metabase import ListTablesRequest
from metabaseapi.metabase import ListTablesResponse
from metabaseapi.metabase import ListUsersRequest
from metabaseapi.metabase import ListUsersResponse
from metabaseapi.metabase import MetabaseField
from metabaseapi.metabase import Table
from metabaseapi.metabase import UpdateActionRequest
from metabaseapi.metabase import User
from metabaseapi.models import APIRequestModel
from metabaseapi.models import APIResponseModel
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue
from metabaseapi.settings import Settings


class _ExecutableRequest[ResponseT](Protocol):
    async def do(self, client: MetabaseClient) -> ResponseT: ...


ResponseT = TypeVar("ResponseT")


class MetabaseClient:
    """Async Metabase API client with a small convenience API surface."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout_seconds: float = 30.0,
        verify_ssl: bool = True,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout_seconds = timeout_seconds
        self.verify_ssl = verify_ssl
        self._provided_client = client
        self._client = client or httpx.AsyncClient(
            timeout=httpx.Timeout(timeout=timeout_seconds),
            verify=verify_ssl,
        )

    @classmethod
    def from_settings(cls, settings: Settings, client: httpx.AsyncClient | None = None) -> MetabaseClient:
        api_key = settings.requires_api_key()
        return cls(
            base_url=settings.base_url,
            api_key=api_key,
            timeout_seconds=settings.timeout_seconds,
            verify_ssl=settings.verify_ssl,
            client=client,
        )

    async def __aenter__(self) -> MetabaseClient:
        return self

    async def __aexit__(
        self,
        _exc_type: type[BaseException] | None,
        _exc_value: BaseException | None,
        _traceback: object | None,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        if self._provided_client is None:
            await self._client.aclose()

    def _request_url(self, path: str) -> str:
        normalized = path.strip()
        if not normalized.startswith("http://") and not normalized.startswith("https://"):
            normalized = f"/{normalized.lstrip('/')}"
            return f"{self.base_url}{normalized}"
        return normalized

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        json_data: JSONValue | None = None,
    ) -> JSONValue | None:
        request_model = APIRequestModel(
            method=method,
            path=path,
            params=dict(params or {}),
            body=json_data,
        )

        url = self._request_url(request_model.path)
        headers = {"X-API-Key": self.api_key, "Accept": "application/json"}
        try:
            match request_model.method:
                case "GET":
                    response = await self._client.get(url, params=request_model.params, headers=headers)
                case "POST":
                    response = await self._client.post(
                        url,
                        params=request_model.params,
                        json=request_model.body,
                        headers=headers,
                    )
                case "PUT":
                    response = await self._client.put(
                        url,
                        params=request_model.params,
                        json=request_model.body,
                        headers=headers,
                    )
                case "PATCH":
                    response = await self._client.patch(
                        url,
                        params=request_model.params,
                        json=request_model.body,
                        headers=headers,
                    )
                case "DELETE":
                    if request_model.body is None:
                        response = await self._client.delete(url, params=request_model.params, headers=headers)
                    else:
                        # httpx.AsyncClient.delete() has no JSON-body parameter, but Metabase documents
                        # DELETE /api/cache with a JSON body.
                        response = await self._client.request(
                            "DELETE",
                            url,
                            params=request_model.params,
                            json=request_model.body,
                            headers=headers,
                        )
                case _:
                    raise AssertionError("unsupported HTTP method after request validation")
        except httpx.TimeoutException as exc:
            raise MetabaseNetworkError("Metabase request timed out") from exc
        except httpx.NetworkError as exc:
            raise MetabaseNetworkError("Metabase network error") from exc

        payload = self._decode_response_payload(response)
        response_model = APIResponseModel(
            status_code=response.status_code,
            payload=payload,
            content_type=response.headers.get("content-type", None),
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise MetabaseHTTPStatusError(response.status_code, response_model.payload)

        return response_model.payload

    def _decode_response_payload(self, response: httpx.Response) -> JSONValue | None:

        if response.status_code == 204 or not response.content:
            return None

        content_type = response.headers.get("content-type", "").lower()
        if "application/json" in content_type or response.text.strip().startswith(("{", "[")):
            try:
                return response.json()
            except ValueError as exc:
                raise MetabaseDecodeError("Invalid JSON in response") from exc

        return {
            "content_type": content_type or None,
            "text": response.text,
        }

    async def get(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.request("GET", path, params=params)

    async def post(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("POST", path, params=params, json_data=body)

    async def put(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PUT", path, params=params, json_data=body)

    async def patch(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PATCH", path, params=params, json_data=body)

    async def delete(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("DELETE", path, params=params, json_data=body)

    async def list_actions(self, *, model_id: int | str | None = None) -> JSONValue | None:
        params = {"model-id": model_id} if model_id is not None else None
        return await self.get("/api/action", params=params)

    async def create_action(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/action", body=dict(body))

    async def list_public_actions(self) -> JSONValue | None:
        return await self.get("/api/action/public")

    async def get_action(self, action_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/action/{action_id}")

    async def delete_action(self, action_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/action/{action_id}")

    async def get_action_execute(
        self,
        action_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        query_params = cast(Mapping[str, QueryParamValue] | None, parameters)
        return await self.get(f"/api/action/{action_id}/execute", params=query_params)

    async def update_action(self, action_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put(f"/api/action/{action_id}", body=dict(body))

    async def execute_action(
        self,
        action_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(f"/api/action/{action_id}/execute", body={"parameters": dict(parameters or {})})

    async def create_action_public_link(self, action_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/action/{action_id}/public_link")

    async def delete_action_public_link(self, action_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/action/{action_id}/public_link")

    async def analyze_chart(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/ai-entity-analysis/analyze-chart", body=dict(body))

    async def list_alerts(self, *, user_id: int | str | None = None) -> JSONValue | None:
        params = {"user_id": user_id} if user_id is not None else None
        return await self.get("/api/alert", params=params)

    async def get_alert(self, alert_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/alert/{alert_id}")

    async def delete_alert_subscription(self, alert_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/alert/{alert_id}/subscription")

    async def anonymous_stats(self) -> JSONValue | None:
        return await self.get("/api/analytics/anonymous-stats")

    async def create_analytics_event_batch(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/analytics/internal", body=dict(body))

    async def agent_execute(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v1/execute", body=dict(body))

    async def get_agent_metric(self, metric_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/metric/{metric_id}")

    async def get_agent_metric_field_values(self, metric_id: int | str, field_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/metric/{metric_id}/field/{field_id}/values")

    async def agent_ping(self) -> JSONValue | None:
        return await self.get("/api/agent/v1/ping")

    async def agent_search(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v1/search", body=dict(body))

    async def get_agent_table(self, table_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/table/{table_id}")

    async def get_agent_table_field_values(self, table_id: int | str, field_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/agent/v1/table/{table_id}/field/{field_id}/values")

    async def agent_construct_query(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v2/construct-query", body=dict(body))

    async def agent_query(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/agent/v2/query", body=dict(body))

    async def most_recently_viewed_dashboard(self) -> JSONValue | None:
        return await self.get("/api/activity/most_recently_viewed_dashboard")

    async def list_popular_items(self) -> JSONValue | None:
        return await self.get("/api/activity/popular_items")

    async def list_recent_views(self) -> JSONValue | None:
        return await self.get("/api/activity/recent_views")

    async def list_recents(self, *, context: str | None = None) -> JSONValue | None:
        params = {"context": context} if context is not None else None
        return await self.get("/api/activity/recents", params=params)

    async def create_recent(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/activity/recents", body=dict(body))

    async def current_user(self) -> JSONValue | None:
        return await self.get("/api/user/current")

    async def list_databases(self) -> JSONValue | None:
        return await self.get("/api/database")

    async def create_database(
        self,
        *,
        name: str,
        engine: str,
        details: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {"name": name, "engine": engine}
        if details is not None:
            body["details"] = dict(details)
        return await self.post("/api/database", body=body)

    async def get_database(self, database_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/database/{database_id}")

    async def list_cards(self) -> JSONValue | None:
        return await self.get("/api/card")

    async def create_card(
        self,
        *,
        name: str,
        dataset_query: Mapping[str, object],
        display: str,
        visualization_settings: Mapping[str, object] | None = None,
        card_type: str | None = "question",
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {
            "name": name,
            "dataset_query": dict(dataset_query),
            "display": display,
            "visualization_settings": dict(visualization_settings or {}),
        }
        if card_type is not None:
            body["type"] = card_type
        if collection_id is not None:
            body["collection_id"] = collection_id
        if description is not None:
            body["description"] = description
        if parameters is not None:
            body["parameters"] = parameters
        if result_metadata is not None:
            body["result_metadata"] = result_metadata
        return await self.post("/api/card", body=body)

    async def create_question(
        self,
        *,
        name: str,
        dataset_query: Mapping[str, object],
        display: str,
        visualization_settings: Mapping[str, object] | None = None,
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> JSONValue | None:
        return await self.create_card(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def get_card(self, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}")

    async def list_dashboards(self) -> JSONValue | None:
        return await self.get("/api/dashboard")

    async def get_dashboard(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/dashboard/{dashboard_id}")

    async def list_users(self) -> JSONValue | None:
        return await self.get("/api/user")

    async def get_user(self, user_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/user/{user_id}")

    async def list_collections(self) -> JSONValue | None:
        return await self.get("/api/collection")

    async def get_collection(self, collection_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/collection/{collection_id}")

    async def list_tables(self) -> JSONValue | None:
        return await self.get("/api/table")

    async def get_table(self, table_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/table/{table_id}")

    async def get_field(self, field_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/field/{field_id}")

    async def run[ResponseT](self, request_model: _ExecutableRequest[ResponseT]) -> ResponseT:
        return await request_model.do(self)

    async def list_actions_typed(self, *, model_id: int | str | None = None) -> ListActionsResponse:
        return await self.run(ListActionsRequest(model_id=model_id))

    async def create_action_typed(self, body: dict[str, object]) -> Action:
        return await self.run(CreateActionRequest(body=body))

    async def list_public_actions_typed(self) -> ListActionsResponse:
        return await self.run(ListPublicActionsRequest())

    async def get_action_typed(self, action_id: int | str) -> Action:
        return await self.run(GetActionRequest(action_id=action_id))

    async def delete_action_typed(self, action_id: int | str) -> ActionExecutionResponse:
        return await self.run(DeleteActionRequest(action_id=action_id))

    async def get_action_execute_typed(
        self,
        action_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> ActionExecutionResponse:
        return await self.run(GetActionExecuteRequest(action_id=action_id, parameters=parameters or {}))

    async def update_action_typed(self, action_id: int | str, body: dict[str, object]) -> Action:
        return await self.run(UpdateActionRequest(action_id=action_id, body=body))

    async def execute_action_typed(
        self,
        action_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> ActionExecutionResponse:
        return await self.run(ExecuteActionRequest(action_id=action_id, parameters=parameters or {}))

    async def create_action_public_link_typed(self, action_id: int | str) -> ActionExecutionResponse:
        return await self.run(CreateActionPublicLinkRequest(action_id=action_id))

    async def delete_action_public_link_typed(self, action_id: int | str) -> ActionExecutionResponse:
        return await self.run(DeleteActionPublicLinkRequest(action_id=action_id))

    async def analyze_chart_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(AnalyzeChartRequest(body=body))

    async def list_alerts_typed(self, *, user_id: int | str | None = None) -> ListAlertsResponse:
        return await self.run(ListAlertsRequest(user_id=user_id))

    async def get_alert_typed(self, alert_id: int | str) -> Alert:
        return await self.run(GetAlertRequest(alert_id=alert_id))

    async def delete_alert_subscription_typed(self, alert_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteAlertSubscriptionRequest(alert_id=alert_id))

    async def anonymous_stats_typed(self) -> GenericOperationResponse:
        return await self.run(GetAnonymousStatsRequest())

    async def create_analytics_event_batch_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(CreateAnalyticsEventBatchRequest(body=body))

    async def agent_execute_typed(self, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentExecuteRequest(body=body))

    async def get_agent_metric_typed(self, metric_id: int | str) -> AgentResponse:
        return await self.run(GetAgentMetricRequest(metric_id=metric_id))

    async def get_agent_metric_field_values_typed(self, metric_id: int | str, field_id: int | str) -> AgentResponse:
        return await self.run(GetAgentMetricFieldValuesRequest(metric_id=metric_id, field_id=field_id))

    async def agent_ping_typed(self) -> AgentResponse:
        return await self.run(AgentPingRequest())

    async def agent_search_typed(self, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentSearchRequest(body=body))

    async def get_agent_table_typed(self, table_id: int | str) -> AgentResponse:
        return await self.run(GetAgentTableRequest(table_id=table_id))

    async def get_agent_table_field_values_typed(self, table_id: int | str, field_id: int | str) -> AgentResponse:
        return await self.run(GetAgentTableFieldValuesRequest(table_id=table_id, field_id=field_id))

    async def agent_construct_query_typed(self, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentConstructQueryRequest(body=body))

    async def agent_query_typed(self, body: dict[str, object]) -> AgentResponse:
        return await self.run(AgentQueryRequest(body=body))

    async def most_recently_viewed_dashboard_typed(self) -> ActivityItem:
        return await self.run(GetMostRecentlyViewedDashboardRequest())

    async def list_popular_items_typed(self) -> ListActivityItemsResponse:
        return await self.run(ListPopularItemsRequest())

    async def list_recent_views_typed(self) -> ListActivityItemsResponse:
        return await self.run(ListRecentViewsRequest())

    async def list_recents_typed(self, *, context: str | None = None) -> ListActivityItemsResponse:
        return await self.run(ListRecentsRequest(context=context))

    async def create_recent_typed(self, body: dict[str, object]) -> ActivityMutationResponse:
        return await self.run(CreateRecentRequest(body=body))

    async def current_user_typed(self) -> CurrentUserResponse:
        return await self.run(CurrentUserRequest())

    async def list_databases_typed(self) -> ListDatabasesResponse:
        return await self.run(ListDatabasesRequest())

    async def list_cards_typed(self) -> ListCardsResponse:
        return await self.run(ListCardsRequest())

    async def list_dashboards_typed(self) -> ListDashboardsResponse:
        return await self.run(ListDashboardsRequest())

    async def list_users_typed(self) -> ListUsersResponse:
        return await self.run(ListUsersRequest())

    async def list_collections_typed(self) -> ListCollectionsResponse:
        return await self.run(ListCollectionsRequest())

    async def list_tables_typed(self) -> ListTablesResponse:
        return await self.run(ListTablesRequest())

    async def create_database_typed(
        self,
        *,
        name: str,
        engine: str,
        details: dict[str, object] | None = None,
    ) -> Database:
        request = CreateDatabaseRequest(name=name, engine=engine, details=details or {})
        return await self.run(request)

    async def create_card_typed(
        self,
        *,
        name: str,
        dataset_query: dict[str, object],
        display: str,
        visualization_settings: dict[str, object] | None = None,
        card_type: str | None = "question",
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> Card:
        request = CreateCardRequest(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings or {},
            type=card_type,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )
        return await self.run(request)

    async def create_question_typed(
        self,
        *,
        name: str,
        dataset_query: dict[str, object],
        display: str,
        visualization_settings: dict[str, object] | None = None,
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> Card:
        return await self.create_card_typed(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def get_database_typed(self, database_id: int | str) -> Database:
        return await self.run(GetDatabaseRequest(database_id=database_id))

    async def get_card_typed(self, card_id: int | str) -> Card:
        return await self.run(GetCardRequest(card_id=card_id))

    async def get_dashboard_typed(self, dashboard_id: int | str) -> Dashboard:
        return await self.run(GetDashboardRequest(dashboard_id=dashboard_id))

    async def get_user_typed(self, user_id: int | str) -> User:
        return await self.run(GetUserRequest(user_id=user_id))

    async def get_collection_typed(self, collection_id: int | str) -> Collection:
        return await self.run(GetCollectionRequest(collection_id=collection_id))

    async def get_table_typed(self, table_id: int | str) -> Table:
        return await self.run(GetTableRequest(table_id=table_id))

    async def get_field_typed(self, field_id: int | str) -> MetabaseField:
        return await self.run(GetFieldRequest(field_id=field_id))
