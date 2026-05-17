from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING
from typing import Protocol
from typing import TypeVar

import httpx

from metabaseapi.client.raw import action as _raw_action
from metabaseapi.client.raw import activity as _raw_activity
from metabaseapi.client.raw import agent as _raw_agent
from metabaseapi.client.raw import alert as _raw_alert
from metabaseapi.client.raw import analytics as _raw_analytics
from metabaseapi.client.raw import api_key as _raw_api_key
from metabaseapi.client.raw import automagic as _raw_automagic
from metabaseapi.client.raw import bookmark as _raw_bookmark
from metabaseapi.client.raw import bug_reporting as _raw_bug_reporting
from metabaseapi.client.raw import cache as _raw_cache
from metabaseapi.client.raw import card as _raw_card
from metabaseapi.client.raw import channel as _raw_channel
from metabaseapi.client.raw import cloud_migration as _raw_cloud_migration
from metabaseapi.client.raw import collection as _raw_collection
from metabaseapi.client.raw import comment as _raw_comment
from metabaseapi.client.raw import dashboard as _raw_dashboard
from metabaseapi.client.raw import data_studio as _raw_data_studio
from metabaseapi.client.raw import database as _raw_database
from metabaseapi.client.raw import schema as _raw_schema
from metabaseapi.client.raw import user as _raw_user
from metabaseapi.client.typed import action as _typed_action
from metabaseapi.client.typed import activity as _typed_activity
from metabaseapi.client.typed import agent as _typed_agent
from metabaseapi.client.typed import alert as _typed_alert
from metabaseapi.client.typed import analytics as _typed_analytics
from metabaseapi.client.typed import api_key as _typed_api_key
from metabaseapi.client.typed import automagic as _typed_automagic
from metabaseapi.client.typed import bookmark as _typed_bookmark
from metabaseapi.client.typed import bug_reporting as _typed_bug_reporting
from metabaseapi.client.typed import cache as _typed_cache
from metabaseapi.client.typed import card as _typed_card
from metabaseapi.client.typed import channel as _typed_channel
from metabaseapi.client.typed import cloud_migration as _typed_cloud_migration
from metabaseapi.client.typed import collection as _typed_collection
from metabaseapi.client.typed import comment as _typed_comment
from metabaseapi.client.typed import dashboard as _typed_dashboard
from metabaseapi.client.typed import data_studio as _typed_data_studio
from metabaseapi.client.typed import database as _typed_database
from metabaseapi.client.typed import schema as _typed_schema
from metabaseapi.client.typed import user as _typed_user

if TYPE_CHECKING:
    from metabaseapi.endpoints.entities import Action
    from metabaseapi.endpoints.entities import ActivityItem
    from metabaseapi.endpoints.entities import Alert
    from metabaseapi.endpoints.entities import ApiKey
    from metabaseapi.endpoints.entities import Bookmark
    from metabaseapi.endpoints.entities import Card
    from metabaseapi.endpoints.entities import Collection
    from metabaseapi.endpoints.entities import CurrentUserResponse
    from metabaseapi.endpoints.entities import Dashboard
    from metabaseapi.endpoints.entities import Database
    from metabaseapi.endpoints.entities import MetabaseField
    from metabaseapi.endpoints.entities import Table
    from metabaseapi.endpoints.entities import User
    from metabaseapi.endpoints.responses import ActionExecutionResponse
    from metabaseapi.endpoints.responses import ActivityMutationResponse
    from metabaseapi.endpoints.responses import AgentResponse
    from metabaseapi.endpoints.responses import CardsDashboardsResponse
    from metabaseapi.endpoints.responses import GenericOperationResponse
    from metabaseapi.endpoints.responses import ListActionsResponse
    from metabaseapi.endpoints.responses import ListActivityItemsResponse
    from metabaseapi.endpoints.responses import ListAlertsResponse
    from metabaseapi.endpoints.responses import ListApiKeysResponse
    from metabaseapi.endpoints.responses import ListBookmarksResponse
    from metabaseapi.endpoints.responses import ListCardsResponse
    from metabaseapi.endpoints.responses import ListChannelsResponse
    from metabaseapi.endpoints.responses import ListCollectionsResponse
    from metabaseapi.endpoints.responses import ListDashboardsResponse
    from metabaseapi.endpoints.responses import ListDatabasesResponse
    from metabaseapi.endpoints.responses import ListTablesResponse
    from metabaseapi.endpoints.responses import ListUsersResponse

from metabaseapi.errors import MetabaseDecodeError
from metabaseapi.errors import MetabaseHTTPStatusError
from metabaseapi.errors import MetabaseNetworkError
from metabaseapi.settings import Settings
from metabaseapi.wire import APIRequestModel
from metabaseapi.wire import APIResponseModel
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

__all__ = [
    "MetabaseClient",
]


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

    async def run[ResponseT](self, request_model: _ExecutableRequest[ResponseT]) -> ResponseT:
        return await request_model.do(self)

    # Domain endpoint methods are generated from client.raw/client.typed function modules.
    async def list_actions(
        self,
        *,
        model_id: int | str | None = None,
    ) -> JSONValue | None:
        return await _raw_action.list_actions(
            self,
            model_id=model_id,
        )

    async def create_action(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_action.create_action(
            self,
            body,
        )

    async def list_public_actions(
        self,
    ) -> JSONValue | None:
        return await _raw_action.list_public_actions(
            self,
        )

    async def get_action(
        self,
        action_id: int | str,
    ) -> JSONValue | None:
        return await _raw_action.get_action(
            self,
            action_id,
        )

    async def delete_action(
        self,
        action_id: int | str,
    ) -> JSONValue | None:
        return await _raw_action.delete_action(
            self,
            action_id,
        )

    async def get_action_execute(
        self,
        action_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_action.get_action_execute(
            self,
            action_id,
            parameters=parameters,
        )

    async def update_action(
        self,
        action_id: int | str,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_action.update_action(
            self,
            action_id,
            body,
        )

    async def execute_action(
        self,
        action_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_action.execute_action(
            self,
            action_id,
            parameters=parameters,
        )

    async def create_action_public_link(
        self,
        action_id: int | str,
    ) -> JSONValue | None:
        return await _raw_action.create_action_public_link(
            self,
            action_id,
        )

    async def delete_action_public_link(
        self,
        action_id: int | str,
    ) -> JSONValue | None:
        return await _raw_action.delete_action_public_link(
            self,
            action_id,
        )

    async def most_recently_viewed_dashboard(
        self,
    ) -> JSONValue | None:
        return await _raw_activity.most_recently_viewed_dashboard(
            self,
        )

    async def list_popular_items(
        self,
    ) -> JSONValue | None:
        return await _raw_activity.list_popular_items(
            self,
        )

    async def list_recent_views(
        self,
    ) -> JSONValue | None:
        return await _raw_activity.list_recent_views(
            self,
        )

    async def list_recents(
        self,
        *,
        context: str | None = None,
    ) -> JSONValue | None:
        return await _raw_activity.list_recents(
            self,
            context=context,
        )

    async def create_recent(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_activity.create_recent(
            self,
            body,
        )

    async def agent_execute(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_agent.agent_execute(
            self,
            body,
        )

    async def get_agent_metric(
        self,
        metric_id: int | str,
    ) -> JSONValue | None:
        return await _raw_agent.get_agent_metric(
            self,
            metric_id,
        )

    async def get_agent_metric_field_values(
        self,
        metric_id: int | str,
        field_id: int | str,
    ) -> JSONValue | None:
        return await _raw_agent.get_agent_metric_field_values(
            self,
            metric_id,
            field_id,
        )

    async def agent_ping(
        self,
    ) -> JSONValue | None:
        return await _raw_agent.agent_ping(
            self,
        )

    async def agent_search(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_agent.agent_search(
            self,
            body,
        )

    async def get_agent_table(
        self,
        table_id: int | str,
    ) -> JSONValue | None:
        return await _raw_agent.get_agent_table(
            self,
            table_id,
        )

    async def get_agent_table_field_values(
        self,
        table_id: int | str,
        field_id: int | str,
    ) -> JSONValue | None:
        return await _raw_agent.get_agent_table_field_values(
            self,
            table_id,
            field_id,
        )

    async def agent_construct_query(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_agent.agent_construct_query(
            self,
            body,
        )

    async def agent_query(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_agent.agent_query(
            self,
            body,
        )

    async def list_alerts(
        self,
        *,
        user_id: int | str | None = None,
    ) -> JSONValue | None:
        return await _raw_alert.list_alerts(
            self,
            user_id=user_id,
        )

    async def get_alert(
        self,
        alert_id: int | str,
    ) -> JSONValue | None:
        return await _raw_alert.get_alert(
            self,
            alert_id,
        )

    async def delete_alert_subscription(
        self,
        alert_id: int | str,
    ) -> JSONValue | None:
        return await _raw_alert.delete_alert_subscription(
            self,
            alert_id,
        )

    async def analyze_chart(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_analytics.analyze_chart(
            self,
            body,
        )

    async def anonymous_stats(
        self,
    ) -> JSONValue | None:
        return await _raw_analytics.anonymous_stats(
            self,
        )

    async def create_analytics_event_batch(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_analytics.create_analytics_event_batch(
            self,
            body,
        )

    async def create_api_key(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_api_key.create_api_key(
            self,
            body,
        )

    async def list_api_keys(
        self,
    ) -> JSONValue | None:
        return await _raw_api_key.list_api_keys(
            self,
        )

    async def count_api_keys(
        self,
    ) -> JSONValue | None:
        return await _raw_api_key.count_api_keys(
            self,
        )

    async def update_api_key(
        self,
        api_key_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_api_key.update_api_key(
            self,
            api_key_id,
            body,
        )

    async def delete_api_key(
        self,
        api_key_id: int | str,
    ) -> JSONValue | None:
        return await _raw_api_key.delete_api_key(
            self,
            api_key_id,
        )

    async def regenerate_api_key(
        self,
        api_key_id: int | str,
    ) -> JSONValue | None:
        return await _raw_api_key.regenerate_api_key(
            self,
            api_key_id,
        )

    async def automagic_database_candidates(
        self,
        database_id: int | str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_database_candidates(
            self,
            database_id,
        )

    async def automagic_model_index_primary_key(
        self,
        model_index_id: int | str,
        primary_key_id: int | str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_model_index_primary_key(
            self,
            model_index_id,
            primary_key_id,
        )

    async def automagic_dashboard_path(
        self,
        path: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_dashboard_path(
            self,
            path,
        )

    async def automagic_entity(
        self,
        entity: str,
        entity_id_or_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity(
            self,
            entity,
            entity_id_or_query,
        )

    async def automagic_entity_cell(
        self,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_cell(
            self,
            entity,
            entity_id_or_query,
            cell_query,
        )

    async def automagic_entity_cell_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_cell_compare(
            self,
            entity,
            entity_id_or_query,
            cell_query,
            comparison_entity,
            comparison_entity_id_or_query,
        )

    async def automagic_entity_cell_rule(
        self,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        prefix: str,
        dashboard_template: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_cell_rule(
            self,
            entity,
            entity_id_or_query,
            cell_query,
            prefix,
            dashboard_template,
        )

    async def automagic_entity_cell_rule_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        prefix: str,
        dashboard_template: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_cell_rule_compare(
            self,
            entity,
            entity_id_or_query,
            cell_query,
            prefix,
            dashboard_template,
            comparison_entity,
            comparison_entity_id_or_query,
        )

    async def automagic_entity_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_compare(
            self,
            entity,
            entity_id_or_query,
            comparison_entity,
            comparison_entity_id_or_query,
        )

    async def automagic_entity_query_metadata(
        self,
        entity: str,
        entity_id_or_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_query_metadata(
            self,
            entity,
            entity_id_or_query,
        )

    async def automagic_entity_rule(
        self,
        entity: str,
        entity_id_or_query: str,
        prefix: str,
        dashboard_template: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_rule(
            self,
            entity,
            entity_id_or_query,
            prefix,
            dashboard_template,
        )

    async def automagic_entity_rule_compare(
        self,
        entity: str,
        entity_id_or_query: str,
        prefix: str,
        dashboard_template: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await _raw_automagic.automagic_entity_rule_compare(
            self,
            entity,
            entity_id_or_query,
            prefix,
            dashboard_template,
            comparison_entity,
            comparison_entity_id_or_query,
        )

    async def list_bookmarks(
        self,
    ) -> JSONValue | None:
        return await _raw_bookmark.list_bookmarks(
            self,
        )

    async def update_bookmark_ordering(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_bookmark.update_bookmark_ordering(
            self,
            body,
        )

    async def create_bookmark(
        self,
        model: str,
        item_id: int | str,
    ) -> JSONValue | None:
        return await _raw_bookmark.create_bookmark(
            self,
            model,
            item_id,
        )

    async def delete_bookmark(
        self,
        model: str,
        item_id: int | str,
    ) -> JSONValue | None:
        return await _raw_bookmark.delete_bookmark(
            self,
            model,
            item_id,
        )

    async def bug_reporting_connection_pool_details(
        self,
    ) -> JSONValue | None:
        return await _raw_bug_reporting.bug_reporting_connection_pool_details(
            self,
        )

    async def bug_reporting_details(
        self,
    ) -> JSONValue | None:
        return await _raw_bug_reporting.bug_reporting_details(
            self,
        )

    async def get_cache(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sort_column: str | None = None,
        sort_direction: str | None = None,
    ) -> JSONValue | None:
        return await _raw_cache.get_cache(
            self,
            limit=limit,
            offset=offset,
            sort_column=sort_column,
            sort_direction=sort_direction,
        )

    async def put_cache(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_cache.put_cache(
            self,
            body,
        )

    async def delete_cache(
        self,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_cache.delete_cache(
            self,
            body,
        )

    async def invalidate_cache(
        self,
        params: Mapping[str, QueryParamValue],
    ) -> JSONValue | None:
        return await _raw_cache.invalidate_cache(
            self,
            params,
        )

    async def list_cards(
        self,
    ) -> JSONValue | None:
        return await _raw_card.list_cards(
            self,
        )

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
        return await _raw_card.create_card(
            self,
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type=card_type,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

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
        return await _raw_card.create_question(
            self,
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def card_collections(
        self,
        card_ids: list[int | str],
        collection_id: int | str | None = None,
    ) -> JSONValue | None:
        return await _raw_card.card_collections(
            self,
            card_ids,
            collection_id,
        )

    async def list_embeddable_cards(
        self,
    ) -> JSONValue | None:
        return await _raw_card.list_embeddable_cards(
            self,
        )

    async def pivot_query(
        self,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_card.pivot_query(
            self,
            card_id,
            body,
        )

    async def list_public_cards(
        self,
    ) -> JSONValue | None:
        return await _raw_card.list_public_cards(
            self,
        )

    async def get_card_param_search_values(
        self,
        card_id: int | str,
        param_key: str,
        query: str,
    ) -> JSONValue | None:
        return await _raw_card.get_card_param_search_values(
            self,
            card_id,
            param_key,
            query,
        )

    async def get_card_param_values(
        self,
        card_id: int | str,
        param_key: str,
    ) -> JSONValue | None:
        return await _raw_card.get_card_param_values(
            self,
            card_id,
            param_key,
        )

    async def create_card_public_link(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.create_card_public_link(
            self,
            card_id,
        )

    async def delete_card_public_link(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.delete_card_public_link(
            self,
            card_id,
        )

    async def query_card(
        self,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_card.query_card(
            self,
            card_id,
            body,
        )

    async def query_card_export(
        self,
        card_id: int | str,
        export_format: str,
        body: Mapping[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> JSONValue | None:
        return await _raw_card.query_card_export(
            self,
            card_id,
            export_format,
            body,
            pivot_results=pivot_results,
            format_rows=format_rows,
        )

    async def update_card(
        self,
        card_id: int | str,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_card.update_card(
            self,
            card_id,
            body,
        )

    async def delete_card(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.delete_card(
            self,
            card_id,
        )

    async def copy_card(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.copy_card(
            self,
            card_id,
        )

    async def cards_dashboards(
        self,
        card_ids: list[int | str],
    ) -> JSONValue | None:
        return await _raw_card.cards_dashboards(
            self,
            card_ids,
        )

    async def move_cards(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_card.move_cards(
            self,
            body,
        )

    async def get_card_dashboards(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.get_card_dashboards(
            self,
            card_id,
        )

    async def get_card_param_remapping(
        self,
        card_id: int | str,
        param_key: str,
    ) -> JSONValue | None:
        return await _raw_card.get_card_param_remapping(
            self,
            card_id,
            param_key,
        )

    async def get_card_query_metadata(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.get_card_query_metadata(
            self,
            card_id,
        )

    async def get_card_series(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.get_card_series(
            self,
            card_id,
        )

    async def get_card(
        self,
        card_id: int | str,
    ) -> JSONValue | None:
        return await _raw_card.get_card(
            self,
            card_id,
        )

    async def list_channels(
        self,
    ) -> JSONValue | None:
        return await _raw_channel.list_channels(
            self,
        )

    async def create_channel(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_channel.create_channel(
            self,
            body,
        )

    async def test_channel(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_channel.test_channel(
            self,
            body,
        )

    async def get_channel(
        self,
        channel_id: int | str,
    ) -> JSONValue | None:
        return await _raw_channel.get_channel(
            self,
            channel_id,
        )

    async def update_channel(
        self,
        channel_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_channel.update_channel(
            self,
            channel_id,
            body,
        )

    async def create_cloud_migration(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_cloud_migration.create_cloud_migration(
            self,
            body,
        )

    async def get_cloud_migration(
        self,
    ) -> JSONValue | None:
        return await _raw_cloud_migration.get_cloud_migration(
            self,
        )

    async def cancel_cloud_migration(
        self,
    ) -> JSONValue | None:
        return await _raw_cloud_migration.cancel_cloud_migration(
            self,
        )

    async def list_collections(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.list_collections(
            self,
        )

    async def create_collection(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_collection.create_collection(
            self,
            body,
        )

    async def get_collection(
        self,
        collection_id: int | str,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection(
            self,
            collection_id,
        )

    async def update_collection(
        self,
        collection_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_collection.update_collection(
            self,
            collection_id,
            body,
        )

    async def delete_collection(
        self,
        collection_id: int | str,
    ) -> JSONValue | None:
        return await _raw_collection.delete_collection(
            self,
            collection_id,
        )

    async def get_collection_dashboard_question_candidates(
        self,
        collection_id: int | str,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_dashboard_question_candidates(
            self,
            collection_id,
        )

    async def get_collection_items(
        self,
        collection_id: int | str,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_items(
            self,
            collection_id,
        )

    async def post_collection_move_dashboard_question_candidates(
        self,
        collection_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_collection.post_collection_move_dashboard_question_candidates(
            self,
            collection_id,
            body,
        )

    async def get_collection_graph(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_graph(
            self,
        )

    async def put_collection_graph(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_collection.put_collection_graph(
            self,
            body,
        )

    async def get_collection_root(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_root(
            self,
        )

    async def get_collection_root_dashboard_question_candidates(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_root_dashboard_question_candidates(
            self,
        )

    async def get_collection_root_items(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_root_items(
            self,
        )

    async def post_collection_root_move_dashboard_question_candidates(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_collection.post_collection_root_move_dashboard_question_candidates(
            self,
            body,
        )

    async def get_collection_trash(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_trash(
            self,
        )

    async def get_collection_tree(
        self,
    ) -> JSONValue | None:
        return await _raw_collection.get_collection_tree(
            self,
        )

    async def get_comment(
        self,
        *,
        model: str | None = None,
        model_id: int | str | None = None,
    ) -> JSONValue | None:
        return await _raw_comment.get_comment(
            self,
            model=model,
            model_id=model_id,
        )

    async def get_comment_mentions(
        self,
    ) -> JSONValue | None:
        return await _raw_comment.get_comment_mentions(
            self,
        )

    async def create_comment(
        self,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_comment.create_comment(
            self,
            body,
        )

    async def update_comment(
        self,
        comment_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_comment.update_comment(
            self,
            comment_id,
            body,
        )

    async def post_comment_reaction(
        self,
        comment_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await _raw_comment.post_comment_reaction(
            self,
            comment_id,
            body,
        )

    async def delete_comment(
        self,
        comment_id: int | str,
    ) -> JSONValue | None:
        return await _raw_comment.delete_comment(
            self,
            comment_id,
        )

    async def create_dashboard(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_dashboard.create_dashboard(
            self,
            body,
        )

    async def list_dashboards(
        self,
    ) -> JSONValue | None:
        return await _raw_dashboard.list_dashboards(
            self,
        )

    async def get_dashboard(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard(
            self,
            dashboard_id,
        )

    async def get_dashboard_embeddable(
        self,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_embeddable(
            self,
        )

    async def get_dashboard_public(
        self,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_public(
            self,
        )

    async def get_dashboard_params_valid_filter_fields(
        self,
        *,
        filtered: list[int | str] | None = None,
        filtering: list[int | str] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_params_valid_filter_fields(
            self,
            filtered=filtered,
            filtering=filtering,
        )

    async def query_dashboard_card(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.query_dashboard_card(
            self,
            dashboard_id,
            dashcard_id,
            card_id,
            body,
        )

    async def query_dashboard_card_export(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        export_format: str,
        body: Mapping[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.query_dashboard_card_export(
            self,
            dashboard_id,
            dashcard_id,
            card_id,
            export_format,
            body,
            pivot_results=pivot_results,
            format_rows=format_rows,
        )

    async def query_dashboard_card_pivot(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.query_dashboard_card_pivot(
            self,
            dashboard_id,
            dashcard_id,
            card_id,
            body,
        )

    async def save_dashboard(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_dashboard.save_dashboard(
            self,
            body,
        )

    async def save_dashboard_to_collection(
        self,
        parent_collection_id: int | str,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_dashboard.save_dashboard_to_collection(
            self,
            parent_collection_id,
            body,
        )

    async def get_dashboard_dashcard_execute(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_dashcard_execute(
            self,
            dashboard_id,
            dashcard_id,
            parameters=parameters,
        )

    async def execute_dashboard_dashcard(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.execute_dashboard_dashcard(
            self,
            dashboard_id,
            dashcard_id,
            parameters=parameters,
        )

    async def create_dashboard_public_link(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.create_dashboard_public_link(
            self,
            dashboard_id,
        )

    async def delete_dashboard_public_link(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.delete_dashboard_public_link(
            self,
            dashboard_id,
        )

    async def copy_dashboard(
        self,
        from_dashboard_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.copy_dashboard(
            self,
            from_dashboard_id,
            body,
        )

    async def delete_dashboard(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.delete_dashboard(
            self,
            dashboard_id,
        )

    async def update_dashboard(
        self,
        dashboard_id: int | str,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_dashboard.update_dashboard(
            self,
            dashboard_id,
            body,
        )

    async def update_dashboard_cards(
        self,
        dashboard_id: int | str,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_dashboard.update_dashboard_cards(
            self,
            dashboard_id,
            body,
        )

    async def get_dashboard_items(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_items(
            self,
            dashboard_id,
        )

    async def get_dashboard_param_remapping(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_param_remapping(
            self,
            dashboard_id,
            param_key,
            parameters=parameters,
        )

    async def get_dashboard_param_search_values(
        self,
        dashboard_id: int | str,
        param_key: str,
        query: str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_param_search_values(
            self,
            dashboard_id,
            param_key,
            query,
            parameters=parameters,
        )

    async def get_dashboard_param_values(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_param_values(
            self,
            dashboard_id,
            param_key,
            parameters=parameters,
        )

    async def get_dashboard_query_metadata(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_query_metadata(
            self,
            dashboard_id,
        )

    async def get_dashboard_related(
        self,
        dashboard_id: int | str,
    ) -> JSONValue | None:
        return await _raw_dashboard.get_dashboard_related(
            self,
            dashboard_id,
        )

    async def data_studio_table_discard_values(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_data_studio.data_studio_table_discard_values(
            self,
            body,
        )

    async def data_studio_table_edit(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_data_studio.data_studio_table_edit(
            self,
            body,
        )

    async def data_studio_table_rescan_values(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_data_studio.data_studio_table_rescan_values(
            self,
            body,
        )

    async def data_studio_table_selection(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_data_studio.data_studio_table_selection(
            self,
            body,
        )

    async def data_studio_table_sync_schema(
        self,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await _raw_data_studio.data_studio_table_sync_schema(
            self,
            body,
        )

    async def list_databases(
        self,
    ) -> JSONValue | None:
        return await _raw_database.list_databases(
            self,
        )

    async def create_database(
        self,
        *,
        name: str,
        engine: str,
        details: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await _raw_database.create_database(
            self,
            name=name,
            engine=engine,
            details=details,
        )

    async def get_database(
        self,
        database_id: int | str,
    ) -> JSONValue | None:
        return await _raw_database.get_database(
            self,
            database_id,
        )

    async def list_tables(
        self,
    ) -> JSONValue | None:
        return await _raw_schema.list_tables(
            self,
        )

    async def get_table(
        self,
        table_id: int | str,
    ) -> JSONValue | None:
        return await _raw_schema.get_table(
            self,
            table_id,
        )

    async def get_field(
        self,
        field_id: int | str,
    ) -> JSONValue | None:
        return await _raw_schema.get_field(
            self,
            field_id,
        )

    async def current_user(
        self,
    ) -> JSONValue | None:
        return await _raw_user.current_user(
            self,
        )

    async def list_users(
        self,
    ) -> JSONValue | None:
        return await _raw_user.list_users(
            self,
        )

    async def get_user(
        self,
        user_id: int | str,
    ) -> JSONValue | None:
        return await _raw_user.get_user(
            self,
            user_id,
        )

    async def get_user_key_value_namespace(
        self,
        namespace: int | str,
    ) -> JSONValue | None:
        return await _raw_user.get_user_key_value_namespace(
            self,
            namespace,
        )

    async def get_user_key_value_namespace_key(
        self,
        namespace: int | str,
        key: str,
    ) -> JSONValue | None:
        return await _raw_user.get_user_key_value_namespace_key(
            self,
            namespace,
            key,
        )

    async def put_user_key_value_namespace_key(
        self,
        namespace: int | str,
        key: str,
        body: JSONValue,
    ) -> JSONValue | None:
        return await _raw_user.put_user_key_value_namespace_key(
            self,
            namespace,
            key,
            body,
        )

    async def delete_user_key_value_namespace_key(
        self,
        namespace: int | str,
        key: str,
    ) -> JSONValue | None:
        return await _raw_user.delete_user_key_value_namespace_key(
            self,
            namespace,
            key,
        )

    async def list_actions_typed(
        self,
        *,
        model_id: int | str | None = None,
    ) -> ListActionsResponse:
        return await _typed_action.list_actions_typed(
            self,
            model_id=model_id,
        )

    async def create_action_typed(
        self,
        body: dict[str, object],
    ) -> Action:
        return await _typed_action.create_action_typed(
            self,
            body,
        )

    async def list_public_actions_typed(
        self,
    ) -> ListActionsResponse:
        return await _typed_action.list_public_actions_typed(
            self,
        )

    async def get_action_typed(
        self,
        action_id: int | str,
    ) -> Action:
        return await _typed_action.get_action_typed(
            self,
            action_id,
        )

    async def delete_action_typed(
        self,
        action_id: int | str,
    ) -> ActionExecutionResponse:
        return await _typed_action.delete_action_typed(
            self,
            action_id,
        )

    async def get_action_execute_typed(
        self,
        action_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> ActionExecutionResponse:
        return await _typed_action.get_action_execute_typed(
            self,
            action_id,
            parameters=parameters,
        )

    async def update_action_typed(
        self,
        action_id: int | str,
        body: dict[str, object],
    ) -> Action:
        return await _typed_action.update_action_typed(
            self,
            action_id,
            body,
        )

    async def execute_action_typed(
        self,
        action_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> ActionExecutionResponse:
        return await _typed_action.execute_action_typed(
            self,
            action_id,
            parameters=parameters,
        )

    async def create_action_public_link_typed(
        self,
        action_id: int | str,
    ) -> ActionExecutionResponse:
        return await _typed_action.create_action_public_link_typed(
            self,
            action_id,
        )

    async def delete_action_public_link_typed(
        self,
        action_id: int | str,
    ) -> ActionExecutionResponse:
        return await _typed_action.delete_action_public_link_typed(
            self,
            action_id,
        )

    async def most_recently_viewed_dashboard_typed(
        self,
    ) -> ActivityItem:
        return await _typed_activity.most_recently_viewed_dashboard_typed(
            self,
        )

    async def list_popular_items_typed(
        self,
    ) -> ListActivityItemsResponse:
        return await _typed_activity.list_popular_items_typed(
            self,
        )

    async def list_recent_views_typed(
        self,
    ) -> ListActivityItemsResponse:
        return await _typed_activity.list_recent_views_typed(
            self,
        )

    async def list_recents_typed(
        self,
        *,
        context: str | None = None,
    ) -> ListActivityItemsResponse:
        return await _typed_activity.list_recents_typed(
            self,
            context=context,
        )

    async def create_recent_typed(
        self,
        body: dict[str, object],
    ) -> ActivityMutationResponse:
        return await _typed_activity.create_recent_typed(
            self,
            body,
        )

    async def agent_execute_typed(
        self,
        body: dict[str, object],
    ) -> AgentResponse:
        return await _typed_agent.agent_execute_typed(
            self,
            body,
        )

    async def get_agent_metric_typed(
        self,
        metric_id: int | str,
    ) -> AgentResponse:
        return await _typed_agent.get_agent_metric_typed(
            self,
            metric_id,
        )

    async def get_agent_metric_field_values_typed(
        self,
        metric_id: int | str,
        field_id: int | str,
    ) -> AgentResponse:
        return await _typed_agent.get_agent_metric_field_values_typed(
            self,
            metric_id,
            field_id,
        )

    async def agent_ping_typed(
        self,
    ) -> AgentResponse:
        return await _typed_agent.agent_ping_typed(
            self,
        )

    async def agent_search_typed(
        self,
        body: dict[str, object],
    ) -> AgentResponse:
        return await _typed_agent.agent_search_typed(
            self,
            body,
        )

    async def get_agent_table_typed(
        self,
        table_id: int | str,
    ) -> AgentResponse:
        return await _typed_agent.get_agent_table_typed(
            self,
            table_id,
        )

    async def get_agent_table_field_values_typed(
        self,
        table_id: int | str,
        field_id: int | str,
    ) -> AgentResponse:
        return await _typed_agent.get_agent_table_field_values_typed(
            self,
            table_id,
            field_id,
        )

    async def agent_construct_query_typed(
        self,
        body: dict[str, object],
    ) -> AgentResponse:
        return await _typed_agent.agent_construct_query_typed(
            self,
            body,
        )

    async def agent_query_typed(
        self,
        body: dict[str, object],
    ) -> AgentResponse:
        return await _typed_agent.agent_query_typed(
            self,
            body,
        )

    async def list_alerts_typed(
        self,
        *,
        user_id: int | str | None = None,
    ) -> ListAlertsResponse:
        return await _typed_alert.list_alerts_typed(
            self,
            user_id=user_id,
        )

    async def get_alert_typed(
        self,
        alert_id: int | str,
    ) -> Alert:
        return await _typed_alert.get_alert_typed(
            self,
            alert_id,
        )

    async def delete_alert_subscription_typed(
        self,
        alert_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_alert.delete_alert_subscription_typed(
            self,
            alert_id,
        )

    async def analyze_chart_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_analytics.analyze_chart_typed(
            self,
            body,
        )

    async def create_analytics_event_batch_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_analytics.create_analytics_event_batch_typed(
            self,
            body,
        )

    async def create_api_key_typed(
        self,
        body: dict[str, object],
    ) -> ApiKey:
        return await _typed_api_key.create_api_key_typed(
            self,
            body,
        )

    async def list_api_keys_typed(
        self,
    ) -> ListApiKeysResponse:
        return await _typed_api_key.list_api_keys_typed(
            self,
        )

    async def count_api_keys_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_api_key.count_api_keys_typed(
            self,
        )

    async def update_api_key_typed(
        self,
        api_key_id: int | str,
        body: dict[str, object],
    ) -> ApiKey:
        return await _typed_api_key.update_api_key_typed(
            self,
            api_key_id,
            body,
        )

    async def delete_api_key_typed(
        self,
        api_key_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_api_key.delete_api_key_typed(
            self,
            api_key_id,
        )

    async def regenerate_api_key_typed(
        self,
        api_key_id: int | str,
    ) -> ApiKey:
        return await _typed_api_key.regenerate_api_key_typed(
            self,
            api_key_id,
        )

    async def automagic_database_candidates_typed(
        self,
        database_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_automagic.automagic_database_candidates_typed(
            self,
            database_id,
        )

    async def automagic_model_index_primary_key_typed(
        self,
        model_index_id: int | str,
        primary_key_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_automagic.automagic_model_index_primary_key_typed(
            self,
            model_index_id,
            primary_key_id,
        )

    async def automagic_dashboard_path_typed(
        self,
        path: str,
    ) -> GenericOperationResponse:
        return await _typed_automagic.automagic_dashboard_path_typed(
            self,
            path,
        )

    async def list_bookmarks_typed(
        self,
    ) -> ListBookmarksResponse:
        return await _typed_bookmark.list_bookmarks_typed(
            self,
        )

    async def update_bookmark_ordering_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_bookmark.update_bookmark_ordering_typed(
            self,
            body,
        )

    async def create_bookmark_typed(
        self,
        model: str,
        item_id: int | str,
    ) -> Bookmark:
        return await _typed_bookmark.create_bookmark_typed(
            self,
            model,
            item_id,
        )

    async def delete_bookmark_typed(
        self,
        model: str,
        item_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_bookmark.delete_bookmark_typed(
            self,
            model,
            item_id,
        )

    async def bug_reporting_connection_pool_details_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_bug_reporting.bug_reporting_connection_pool_details_typed(
            self,
        )

    async def bug_reporting_details_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_bug_reporting.bug_reporting_details_typed(
            self,
        )

    async def get_cache_typed(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        sort_column: str | None = None,
        sort_direction: str | None = None,
    ) -> GenericOperationResponse:
        return await _typed_cache.get_cache_typed(
            self,
            limit=limit,
            offset=offset,
            sort_column=sort_column,
            sort_direction=sort_direction,
        )

    async def put_cache_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_cache.put_cache_typed(
            self,
            body,
        )

    async def delete_cache_typed(
        self,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_cache.delete_cache_typed(
            self,
            body,
        )

    async def invalidate_cache_typed(
        self,
        params: dict[str, QueryParamValue],
    ) -> GenericOperationResponse:
        return await _typed_cache.invalidate_cache_typed(
            self,
            params,
        )

    async def list_cards_typed(
        self,
    ) -> ListCardsResponse:
        return await _typed_card.list_cards_typed(
            self,
        )

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
        return await _typed_card.create_card_typed(
            self,
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type=card_type,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

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
        return await _typed_card.create_question_typed(
            self,
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def get_card_typed(
        self,
        card_id: int | str,
    ) -> Card:
        return await _typed_card.get_card_typed(
            self,
            card_id,
        )

    async def get_card_collections_typed(
        self,
        card_ids: list[int | str],
        collection_id: int | str | None = None,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_collections_typed(
            self,
            card_ids,
            collection_id,
        )

    async def list_card_embeddable_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_card.list_card_embeddable_typed(
            self,
        )

    async def pivot_card_query_typed(
        self,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_card.pivot_card_query_typed(
            self,
            card_id,
            body,
        )

    async def list_public_cards_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_card.list_public_cards_typed(
            self,
        )

    async def get_card_param_search_values_typed(
        self,
        card_id: int | str,
        param_key: str,
        query: str,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_param_search_values_typed(
            self,
            card_id,
            param_key,
            query,
        )

    async def get_card_param_values_typed(
        self,
        card_id: int | str,
        param_key: str,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_param_values_typed(
            self,
            card_id,
            param_key,
        )

    async def create_card_public_link_typed(
        self,
        card_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_card.create_card_public_link_typed(
            self,
            card_id,
        )

    async def delete_card_public_link_typed(
        self,
        card_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_card.delete_card_public_link_typed(
            self,
            card_id,
        )

    async def query_card_typed(
        self,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_card.query_card_typed(
            self,
            card_id,
            body,
        )

    async def query_card_export_typed(
        self,
        card_id: int | str,
        export_format: str,
        body: dict[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> GenericOperationResponse:
        return await _typed_card.query_card_export_typed(
            self,
            card_id,
            export_format,
            body,
            pivot_results=pivot_results,
            format_rows=format_rows,
        )

    async def cards_dashboards_typed(
        self,
        card_ids: list[int | str],
    ) -> CardsDashboardsResponse:
        return await _typed_card.cards_dashboards_typed(
            self,
            card_ids,
        )

    async def move_cards_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_card.move_cards_typed(
            self,
            body,
        )

    async def update_card_typed(
        self,
        card_id: int | str,
        body: dict[str, object],
    ) -> Card:
        return await _typed_card.update_card_typed(
            self,
            card_id,
            body,
        )

    async def delete_card_typed(
        self,
        card_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_card.delete_card_typed(
            self,
            card_id,
        )

    async def copy_card_typed(
        self,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> Card:
        return await _typed_card.copy_card_typed(
            self,
            card_id,
            body,
        )

    async def get_card_dashboards_typed(
        self,
        card_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_dashboards_typed(
            self,
            card_id,
        )

    async def get_card_param_remapping_typed(
        self,
        card_id: int | str,
        param_key: str,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_param_remapping_typed(
            self,
            card_id,
            param_key,
        )

    async def get_card_query_metadata_typed(
        self,
        card_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_query_metadata_typed(
            self,
            card_id,
        )

    async def get_card_series_typed(
        self,
        card_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_card.get_card_series_typed(
            self,
            card_id,
        )

    async def list_channels_typed(
        self,
    ) -> ListChannelsResponse:
        return await _typed_channel.list_channels_typed(
            self,
        )

    async def create_channel_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_channel.create_channel_typed(
            self,
            body,
        )

    async def test_channel_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_channel.test_channel_typed(
            self,
            body,
        )

    async def get_channel_typed(
        self,
        channel_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_channel.get_channel_typed(
            self,
            channel_id,
        )

    async def update_channel_typed(
        self,
        channel_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_channel.update_channel_typed(
            self,
            channel_id,
            body,
        )

    async def create_cloud_migration_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_cloud_migration.create_cloud_migration_typed(
            self,
            body,
        )

    async def get_cloud_migration_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_cloud_migration.get_cloud_migration_typed(
            self,
        )

    async def cancel_cloud_migration_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_cloud_migration.cancel_cloud_migration_typed(
            self,
        )

    async def list_collections_typed(
        self,
    ) -> ListCollectionsResponse:
        return await _typed_collection.list_collections_typed(
            self,
        )

    async def create_collection_typed(
        self,
        body: dict[str, object],
    ) -> Collection:
        return await _typed_collection.create_collection_typed(
            self,
            body,
        )

    async def get_collection_typed(
        self,
        collection_id: int | str,
    ) -> Collection:
        return await _typed_collection.get_collection_typed(
            self,
            collection_id,
        )

    async def update_collection_typed(
        self,
        collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_collection.update_collection_typed(
            self,
            collection_id,
            body,
        )

    async def delete_collection_typed(
        self,
        collection_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_collection.delete_collection_typed(
            self,
            collection_id,
        )

    async def get_collection_dashboard_question_candidates_typed(
        self,
        collection_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_collection.get_collection_dashboard_question_candidates_typed(
            self,
            collection_id,
        )

    async def get_collection_items_typed(
        self,
        collection_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_collection.get_collection_items_typed(
            self,
            collection_id,
        )

    async def post_collection_move_dashboard_question_candidates_typed(
        self,
        collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_collection.post_collection_move_dashboard_question_candidates_typed(
            self,
            collection_id,
            body,
        )

    async def get_collection_graph_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_collection.get_collection_graph_typed(
            self,
        )

    async def put_collection_graph_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_collection.put_collection_graph_typed(
            self,
            body,
        )

    async def get_collection_root_typed(
        self,
    ) -> Collection:
        return await _typed_collection.get_collection_root_typed(
            self,
        )

    async def get_collection_root_dashboard_question_candidates_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_collection.get_collection_root_dashboard_question_candidates_typed(
            self,
        )

    async def get_collection_root_items_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_collection.get_collection_root_items_typed(
            self,
        )

    async def post_collection_root_move_dashboard_question_candidates_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_collection.post_collection_root_move_dashboard_question_candidates_typed(
            self,
            body,
        )

    async def get_collection_trash_typed(
        self,
    ) -> Collection:
        return await _typed_collection.get_collection_trash_typed(
            self,
        )

    async def get_collection_tree_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_collection.get_collection_tree_typed(
            self,
        )

    async def delete_comment_typed(
        self,
        comment_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_comment.delete_comment_typed(
            self,
            comment_id,
        )

    async def get_comment_mentions_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_comment.get_comment_mentions_typed(
            self,
        )

    async def update_comment_typed(
        self,
        comment_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_comment.update_comment_typed(
            self,
            comment_id,
            body,
        )

    async def post_comment_reaction_typed(
        self,
        comment_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_comment.post_comment_reaction_typed(
            self,
            comment_id,
            body,
        )

    async def get_comment_typed(
        self,
        *,
        model: str | None = None,
        model_id: int | str | None = None,
    ) -> GenericOperationResponse:
        return await _typed_comment.get_comment_typed(
            self,
            model=model,
            model_id=model_id,
        )

    async def create_comment_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_comment.create_comment_typed(
            self,
            body,
        )

    async def create_dashboard_typed(
        self,
        body: dict[str, object],
    ) -> Dashboard:
        return await _typed_dashboard.create_dashboard_typed(
            self,
            body,
        )

    async def list_dashboards_typed(
        self,
    ) -> ListDashboardsResponse:
        return await _typed_dashboard.list_dashboards_typed(
            self,
        )

    async def get_dashboard_typed(
        self,
        dashboard_id: int | str,
    ) -> Dashboard:
        return await _typed_dashboard.get_dashboard_typed(
            self,
            dashboard_id,
        )

    async def get_dashboard_embeddable_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_embeddable_typed(
            self,
        )

    async def get_dashboard_public_typed(
        self,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_public_typed(
            self,
        )

    async def query_dashboard_card_pivot_typed(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.query_dashboard_card_pivot_typed(
            self,
            dashboard_id,
            dashcard_id,
            card_id,
            body,
        )

    async def save_dashboard_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_dashboard.save_dashboard_typed(
            self,
            body,
        )

    async def save_dashboard_to_collection_typed(
        self,
        parent_collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_dashboard.save_dashboard_to_collection_typed(
            self,
            parent_collection_id,
            body,
        )

    async def get_dashboard_dashcard_execute_typed(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_dashcard_execute_typed(
            self,
            dashboard_id,
            dashcard_id,
            parameters=parameters,
        )

    async def execute_dashboard_dashcard_typed(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.execute_dashboard_dashcard_typed(
            self,
            dashboard_id,
            dashcard_id,
            parameters=parameters,
        )

    async def create_dashboard_public_link_typed(
        self,
        dashboard_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.create_dashboard_public_link_typed(
            self,
            dashboard_id,
        )

    async def delete_dashboard_public_link_typed(
        self,
        dashboard_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.delete_dashboard_public_link_typed(
            self,
            dashboard_id,
        )

    async def copy_dashboard_typed(
        self,
        from_dashboard_id: int | str,
        body: dict[str, object] | None = None,
    ) -> Dashboard:
        return await _typed_dashboard.copy_dashboard_typed(
            self,
            from_dashboard_id,
            body,
        )

    async def delete_dashboard_typed(
        self,
        dashboard_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.delete_dashboard_typed(
            self,
            dashboard_id,
        )

    async def update_dashboard_typed(
        self,
        dashboard_id: int | str,
        body: dict[str, object],
    ) -> Dashboard:
        return await _typed_dashboard.update_dashboard_typed(
            self,
            dashboard_id,
            body,
        )

    async def update_dashboard_cards_typed(
        self,
        dashboard_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_dashboard.update_dashboard_cards_typed(
            self,
            dashboard_id,
            body,
        )

    async def get_dashboard_items_typed(
        self,
        dashboard_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_items_typed(
            self,
            dashboard_id,
        )

    async def get_dashboard_param_remapping_typed(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_param_remapping_typed(
            self,
            dashboard_id,
            param_key,
            parameters=parameters,
        )

    async def get_dashboard_param_search_values_typed(
        self,
        dashboard_id: int | str,
        param_key: str,
        query: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_param_search_values_typed(
            self,
            dashboard_id,
            param_key,
            query,
            parameters=parameters,
        )

    async def get_dashboard_param_values_typed(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_param_values_typed(
            self,
            dashboard_id,
            param_key,
            parameters=parameters,
        )

    async def get_dashboard_query_metadata_typed(
        self,
        dashboard_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_query_metadata_typed(
            self,
            dashboard_id,
        )

    async def get_dashboard_related_typed(
        self,
        dashboard_id: int | str,
    ) -> GenericOperationResponse:
        return await _typed_dashboard.get_dashboard_related_typed(
            self,
            dashboard_id,
        )

    async def data_studio_table_discard_values_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_data_studio.data_studio_table_discard_values_typed(
            self,
            body,
        )

    async def data_studio_table_edit_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_data_studio.data_studio_table_edit_typed(
            self,
            body,
        )

    async def data_studio_table_rescan_values_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_data_studio.data_studio_table_rescan_values_typed(
            self,
            body,
        )

    async def data_studio_table_selection_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_data_studio.data_studio_table_selection_typed(
            self,
            body,
        )

    async def data_studio_table_sync_schema_typed(
        self,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await _typed_data_studio.data_studio_table_sync_schema_typed(
            self,
            body,
        )

    async def list_databases_typed(
        self,
    ) -> ListDatabasesResponse:
        return await _typed_database.list_databases_typed(
            self,
        )

    async def create_database_typed(
        self,
        *,
        name: str,
        engine: str,
        details: dict[str, object] | None = None,
    ) -> Database:
        return await _typed_database.create_database_typed(
            self,
            name=name,
            engine=engine,
            details=details,
        )

    async def get_database_typed(
        self,
        database_id: int | str,
    ) -> Database:
        return await _typed_database.get_database_typed(
            self,
            database_id,
        )

    async def list_tables_typed(
        self,
    ) -> ListTablesResponse:
        return await _typed_schema.list_tables_typed(
            self,
        )

    async def get_table_typed(
        self,
        table_id: int | str,
    ) -> Table:
        return await _typed_schema.get_table_typed(
            self,
            table_id,
        )

    async def get_field_typed(
        self,
        field_id: int | str,
    ) -> MetabaseField:
        return await _typed_schema.get_field_typed(
            self,
            field_id,
        )

    async def current_user_typed(
        self,
    ) -> CurrentUserResponse:
        return await _typed_user.current_user_typed(
            self,
        )

    async def list_users_typed(
        self,
    ) -> ListUsersResponse:
        return await _typed_user.list_users_typed(
            self,
        )

    async def get_user_typed(
        self,
        user_id: int | str,
    ) -> User:
        return await _typed_user.get_user_typed(
            self,
            user_id,
        )

    async def get_user_key_value_namespace_typed(
        self,
        namespace: int | str,
    ) -> GenericOperationResponse:
        return await _typed_user.get_user_key_value_namespace_typed(
            self,
            namespace,
        )

    async def put_user_key_value_namespace_key_typed(
        self,
        namespace: int | str,
        key: str,
        body: JSONValue,
    ) -> GenericOperationResponse:
        return await _typed_user.put_user_key_value_namespace_key_typed(
            self,
            namespace,
            key,
            body,
        )

    async def get_user_key_value_namespace_key_typed(
        self,
        namespace: int | str,
        key: str,
    ) -> GenericOperationResponse:
        return await _typed_user.get_user_key_value_namespace_key_typed(
            self,
            namespace,
            key,
        )

    async def delete_user_key_value_namespace_key_typed(
        self,
        namespace: int | str,
        key: str,
    ) -> GenericOperationResponse:
        return await _typed_user.delete_user_key_value_namespace_key_typed(
            self,
            namespace,
            key,
        )
