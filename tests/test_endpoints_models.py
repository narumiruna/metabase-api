from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from datetime import UTC
from datetime import datetime

import httpx

from metabaseapi.client import MetabaseClient
from metabaseapi.endpoints.entities import Action
from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.entities import CurrentUserResponse
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.entities import Database
from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.entities import Table
from metabaseapi.endpoints.entities import User
from metabaseapi.endpoints.requests.action import CreateActionPublicLinkRequest
from metabaseapi.endpoints.requests.action import CreateActionRequest
from metabaseapi.endpoints.requests.action import DeleteActionPublicLinkRequest
from metabaseapi.endpoints.requests.action import DeleteActionRequest
from metabaseapi.endpoints.requests.action import ExecuteActionRequest
from metabaseapi.endpoints.requests.action import GetActionExecuteRequest
from metabaseapi.endpoints.requests.action import GetActionRequest
from metabaseapi.endpoints.requests.action import ListActionsRequest
from metabaseapi.endpoints.requests.action import ListPublicActionsRequest
from metabaseapi.endpoints.requests.action import UpdateActionRequest
from metabaseapi.endpoints.requests.ai_entity_analysis import AnalyzeChartRequest
from metabaseapi.endpoints.requests.alert import DeleteAlertSubscriptionRequest
from metabaseapi.endpoints.requests.analytics import CreateAnalyticsEventBatchRequest
from metabaseapi.endpoints.requests.analytics import GetAnonymousStatsRequest
from metabaseapi.endpoints.requests.bug_reporting import GetBugReportingConnectionPoolDetailsRequest
from metabaseapi.endpoints.requests.bug_reporting import GetBugReportingDetailsRequest
from metabaseapi.endpoints.requests.cache import DeleteCacheRequest
from metabaseapi.endpoints.requests.cache import GetCacheRequest
from metabaseapi.endpoints.requests.cache import InvalidateCacheRequest
from metabaseapi.endpoints.requests.cache import PutCacheRequest
from metabaseapi.endpoints.requests.card import CopyCardRequest
from metabaseapi.endpoints.requests.card import CreateCardPublicLinkRequest
from metabaseapi.endpoints.requests.card import CreateCardRequest
from metabaseapi.endpoints.requests.card import DeleteCardPublicLinkRequest
from metabaseapi.endpoints.requests.card import DeleteCardRequest
from metabaseapi.endpoints.requests.card import GetCardCollectionsRequest
from metabaseapi.endpoints.requests.card import GetCardEmbeddableRequest
from metabaseapi.endpoints.requests.card import GetCardPublicRequest
from metabaseapi.endpoints.requests.card import GetCardRequest
from metabaseapi.endpoints.requests.card import ListCardsRequest
from metabaseapi.endpoints.requests.card import MoveCardsRequest
from metabaseapi.endpoints.requests.card import UpdateCardRequest
from metabaseapi.endpoints.requests.card_query import CardParamsSearchRequest
from metabaseapi.endpoints.requests.card_query import CardParamsValuesRequest
from metabaseapi.endpoints.requests.card_query import CardQueryExportRequest
from metabaseapi.endpoints.requests.card_query import CardQueryRequest
from metabaseapi.endpoints.requests.card_query import CardRemappingRequest
from metabaseapi.endpoints.requests.card_query import CardsDashboardsRequest
from metabaseapi.endpoints.requests.card_query import GetCardDashboardsRequest
from metabaseapi.endpoints.requests.card_query import GetCardQueryMetadataRequest
from metabaseapi.endpoints.requests.card_query import GetCardSeriesRequest
from metabaseapi.endpoints.requests.card_query import PostCardPivotQueryRequest
from metabaseapi.endpoints.requests.channel import CreateChannelRequest
from metabaseapi.endpoints.requests.channel import GetChannelRequest
from metabaseapi.endpoints.requests.channel import ListChannelsRequest
from metabaseapi.endpoints.requests.channel import TestChannelRequest
from metabaseapi.endpoints.requests.channel import UpdateChannelRequest
from metabaseapi.endpoints.requests.cloud_migration import CancelCloudMigrationRequest
from metabaseapi.endpoints.requests.cloud_migration import CreateCloudMigrationRequest
from metabaseapi.endpoints.requests.cloud_migration import GetCloudMigrationRequest
from metabaseapi.endpoints.requests.collection import CreateCollectionRequest
from metabaseapi.endpoints.requests.collection import DeleteCollectionRequest
from metabaseapi.endpoints.requests.collection import GetCollectionDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import GetCollectionItemsRequest
from metabaseapi.endpoints.requests.collection import GetCollectionRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTrashRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTreeRequest
from metabaseapi.endpoints.requests.collection import ListCollectionsRequest
from metabaseapi.endpoints.requests.collection import PostCollectionMoveDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import PutCollectionRequest
from metabaseapi.endpoints.requests.collection_graph import GetCollectionGraphRequest
from metabaseapi.endpoints.requests.collection_graph import PutCollectionGraphRequest
from metabaseapi.endpoints.requests.collection_root import GetCollectionRootDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection_root import GetCollectionRootItemsRequest
from metabaseapi.endpoints.requests.collection_root import GetCollectionRootRequest
from metabaseapi.endpoints.requests.collection_root import PostCollectionRootMoveDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.comment import DeleteCommentRequest
from metabaseapi.endpoints.requests.comment import GetCommentMentionsRequest
from metabaseapi.endpoints.requests.comment import GetCommentRequest
from metabaseapi.endpoints.requests.comment import PostCommentReactionRequest
from metabaseapi.endpoints.requests.comment import PostCommentRequest
from metabaseapi.endpoints.requests.comment import UpdateCommentRequest
from metabaseapi.endpoints.requests.dashboard import CopyDashboardRequest
from metabaseapi.endpoints.requests.dashboard import CreateDashboardPublicLinkRequest
from metabaseapi.endpoints.requests.dashboard import DeleteDashboardPublicLinkRequest
from metabaseapi.endpoints.requests.dashboard import DeleteDashboardRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardEmbeddableRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardItemsRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardPublicRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardRequest
from metabaseapi.endpoints.requests.dashboard import ListDashboardsRequest
from metabaseapi.endpoints.requests.dashboard import PostDashboardRequest
from metabaseapi.endpoints.requests.dashboard import SaveDashboardRequest
from metabaseapi.endpoints.requests.dashboard import SaveDashboardToCollectionRequest
from metabaseapi.endpoints.requests.dashboard import UpdateDashboardCardsRequest
from metabaseapi.endpoints.requests.dashboard import UpdateDashboardRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamRemappingRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamSearchRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamValuesRequest
from metabaseapi.endpoints.requests.dashboard_query import ExecuteDashboardDashcardRequest
from metabaseapi.endpoints.requests.dashboard_query import GetDashboardDashcardExecuteRequest
from metabaseapi.endpoints.requests.dashboard_query import GetDashboardQueryMetadataRequest
from metabaseapi.endpoints.requests.dashboard_query import GetDashboardRelatedRequest
from metabaseapi.endpoints.requests.dashboard_query import PostDashboardPivotQueryRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableDiscardValuesRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableEditRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableRescanValuesRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableSelectionRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableSyncSchemaRequest
from metabaseapi.endpoints.requests.database import CreateDatabaseRequest
from metabaseapi.endpoints.requests.database import GetDatabaseRequest
from metabaseapi.endpoints.requests.database import ListDatabasesRequest
from metabaseapi.endpoints.requests.field import GetFieldRequest
from metabaseapi.endpoints.requests.table import GetTableRequest
from metabaseapi.endpoints.requests.table import ListTablesRequest
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.endpoints.requests.user import GetUserRequest
from metabaseapi.endpoints.requests.user import ListUsersRequest
from metabaseapi.endpoints.requests.user_key_value import DeleteUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.requests.user_key_value import GetUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.requests.user_key_value import GetUserKeyValueNamespaceRequest
from metabaseapi.endpoints.requests.user_key_value import PutUserKeyValueNamespaceKeyRequest
from metabaseapi.endpoints.responses.action import ActionExecutionResponse
from metabaseapi.endpoints.responses.action import ListActionsResponse
from metabaseapi.endpoints.responses.ai_entity_analysis import AnalyzeChartResponse
from metabaseapi.endpoints.responses.alert import AlertSubscriptionDeleteResponse
from metabaseapi.endpoints.responses.analytics import AnalyticsEventBatchResponse
from metabaseapi.endpoints.responses.analytics import AnonymousStatsResponse
from metabaseapi.endpoints.responses.bug_reporting import BugReportingConnectionPoolDetailsResponse
from metabaseapi.endpoints.responses.bug_reporting import BugReportingDetailsResponse
from metabaseapi.endpoints.responses.card import CardsDashboardsResponse
from metabaseapi.endpoints.responses.card import ListCardsResponse
from metabaseapi.endpoints.responses.channel import ListChannelsResponse
from metabaseapi.endpoints.responses.cloud_migration import CancelCloudMigrationResponse
from metabaseapi.endpoints.responses.cloud_migration import CloudMigrationStatusResponse
from metabaseapi.endpoints.responses.cloud_migration import CreateCloudMigrationResponse
from metabaseapi.endpoints.responses.collection import ListCollectionsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.endpoints.responses.dashboard import ListDashboardsResponse
from metabaseapi.endpoints.responses.database import ListDatabasesResponse
from metabaseapi.endpoints.responses.table import ListTablesResponse
from metabaseapi.endpoints.responses.user import ListUsersResponse
from metabaseapi.wire import QueryParamValue


class _StubClient:
    def __init__(self, response: object) -> None:
        self.response = response
        self.calls: list[tuple[str, str, dict[str, QueryParamValue], object | None]] = []

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, QueryParamValue] | None = None,
        json_data: object | None = None,
    ) -> object:
        self.calls.append((method, path, params or {}, json_data))
        return self.response


def test_current_user_response_validates_epoch_datetime() -> None:
    payload = {"id": 1, "email": "alice@example.com", "created_at": 1_697_653_800_557}

    model = CurrentUserResponse.model_validate(payload)

    assert model.id == 1
    assert model.email == "alice@example.com"
    assert isinstance(model.created_at, datetime)
    assert model.created_at.tzinfo == UTC


def test_current_user_request_parses_response_model() -> None:
    payload = {"id": 1, "email": "alice@example.com"}
    client = _StubClient(payload)

    result = _run(CurrentUserRequest().do(client))

    assert isinstance(result, CurrentUserResponse)
    assert result.id == 1
    assert result.email == "alice@example.com"
    assert client.calls == [("GET", "/api/user/current", {}, None)]


def test_list_databases_response_normalizes_payload() -> None:
    sample_list = [
        {"id": 1, "name": "db1", "engine": "postgres"},
        {"id": "uuid", "name": "db2", "engine": "mysql"},
    ]

    result = ListDatabasesResponse.model_validate(sample_list)

    assert len(result.databases) == 2
    assert result.databases[0].name == "db1"
    assert result.databases[1].engine == "mysql"


def test_list_databases_request_posts_to_expected_endpoint() -> None:
    payload = {"data": [{"id": 1, "name": "db"}]}
    client = _StubClient(payload)

    request = ListDatabasesRequest()
    response = _run(request.do(client))

    assert isinstance(response, ListDatabasesResponse)
    assert len(response.databases) == 1
    assert response.databases[0].name == "db"
    assert client.calls == [("GET", "/api/database", {}, None)]


def test_create_database_request_includes_body_for_post() -> None:
    payload = {"id": 1, "name": "analytics", "engine": "postgres", "details": {"host": "db.local"}}
    client = _StubClient(payload)

    request = CreateDatabaseRequest(name="analytics", engine="postgres", details={"host": "db.local"})
    response = _run(request.do(client))

    assert isinstance(response, Database)
    assert response.name == "analytics"
    assert response.engine == "postgres"
    assert client.calls == [
        (
            "POST",
            "/api/database",
            {},
            {"name": "analytics", "engine": "postgres", "details": {"host": "db.local"}},
        ),
    ]


def test_create_card_request_includes_question_body_for_post() -> None:
    payload = {"id": 9, "name": "Orders", "display": "table", "type": "question"}
    client = _StubClient(payload)

    request = CreateCardRequest(
        name="Orders",
        dataset_query={"database": 1, "type": "query", "query": {"source-table": 2}},
        display="table",
        visualization_settings={"table.pivot": False},
        collection_id="root",
        description="Orders question",
    )
    response = _run(request.do(client))

    assert isinstance(response, Card)
    assert response.name == "Orders"
    assert client.calls == [
        (
            "POST",
            "/api/card",
            {},
            {
                "name": "Orders",
                "dataset_query": {"database": 1, "type": "query", "query": {"source-table": 2}},
                "display": "table",
                "visualization_settings": {"table.pivot": False},
                "type": "question",
                "collection_id": "root",
                "description": "Orders question",
            },
        ),
    ]


def test_list_response_models_handle_wrapped_and_unwrapped_payloads() -> None:
    list_payload = {
        "data": [
            {"id": 1, "name": "card", "collection_id": 2},
        ]
    }
    wrapped = ListCardsResponse.model_validate(list_payload)
    unwrapped = ListCardsResponse.model_validate(
        [
            {"id": 2, "name": "card2", "collection_id": 3},
        ]
    )

    assert len(wrapped.cards) == 1
    assert wrapped.cards[0].name == "card"
    assert len(unwrapped.cards) == 1
    assert unwrapped.cards[0].id == 2


def test_action_requests_use_expected_paths_and_payloads() -> None:
    cases = [
        (ListActionsRequest(model_id=42), ListActionsResponse, ("GET", "/api/action", {"model-id": 42}, None)),
        (CreateActionRequest(body={"name": "a"}), Action, ("POST", "/api/action", {}, {"name": "a"})),
        (ListPublicActionsRequest(), ListActionsResponse, ("GET", "/api/action/public", {}, None)),
        (GetActionRequest(action_id=5), Action, ("GET", "/api/action/5", {}, None)),
        (DeleteActionRequest(action_id=5), ActionExecutionResponse, ("DELETE", "/api/action/5", {}, None)),
        (
            GetActionExecuteRequest(action_id=5, parameters={"id": 1}),
            ActionExecutionResponse,
            ("GET", "/api/action/5/execute", {"id": 1}, None),
        ),
        (UpdateActionRequest(action_id=5, body={"name": "b"}), Action, ("PUT", "/api/action/5", {}, {"name": "b"})),
        (
            ExecuteActionRequest(action_id=5, parameters={"id": 1}),
            ActionExecutionResponse,
            ("POST", "/api/action/5/execute", {}, {"parameters": {"id": 1}}),
        ),
        (
            CreateActionPublicLinkRequest(action_id=5),
            ActionExecutionResponse,
            ("POST", "/api/action/5/public_link", {}, None),
        ),
        (
            DeleteActionPublicLinkRequest(action_id=5),
            ActionExecutionResponse,
            ("DELETE", "/api/action/5/public_link", {}, None),
        ),
        (
            AnalyzeChartRequest(body={"image": "base64"}),
            AnalyzeChartResponse,
            ("POST", "/api/ai-entity-analysis/analyze-chart", {}, {"image": "base64"}),
        ),
        (GetAnonymousStatsRequest(), AnonymousStatsResponse, ("GET", "/api/analytics/anonymous-stats", {}, None)),
        (
            CreateAnalyticsEventBatchRequest(body={"events": []}),
            AnalyticsEventBatchResponse,
            ("POST", "/api/analytics/internal", {}, {"events": []}),
        ),
        (
            DeleteAlertSubscriptionRequest(alert_id=7),
            AlertSubscriptionDeleteResponse,
            ("DELETE", "/api/alert/7/subscription", {}, None),
        ),
        (
            GetBugReportingConnectionPoolDetailsRequest(),
            BugReportingConnectionPoolDetailsResponse,
            ("GET", "/api/bug-reporting/connection-pool-details", {}, None),
        ),
        (
            GetBugReportingDetailsRequest(),
            BugReportingDetailsResponse,
            ("GET", "/api/bug-reporting/details", {}, None),
        ),
        (
            GetCacheRequest(limit=10, offset=20, sort_column="name", sort_direction="asc"),
            GenericOperationResponse,
            ("GET", "/api/cache", {"limit": 10, "offset": 20, "sort_column": "name", "sort_direction": "asc"}, None),
        ),
        (PutCacheRequest(body={"type": "lru"}), GenericOperationResponse, ("PUT", "/api/cache", {}, {"type": "lru"})),
        (
            DeleteCacheRequest(body={"status": "all"}),
            GenericOperationResponse,
            ("DELETE", "/api/cache", {}, {"status": "all"}),
        ),
        (
            InvalidateCacheRequest(params={"dashboard": [15], "include": ["question"]}),
            GenericOperationResponse,
            ("POST", "/api/cache/invalidate", {"dashboard": [15], "include": ["question"]}, None),
        ),
        (ListChannelsRequest(), ListChannelsResponse, ("GET", "/api/channel", {}, None)),
        (
            CreateChannelRequest(body={"name": "Slack"}),
            GenericOperationResponse,
            ("POST", "/api/channel", {}, {"name": "Slack"}),
        ),
        (
            TestChannelRequest(body={"name": "Slack"}),
            GenericOperationResponse,
            ("POST", "/api/channel/test", {}, {"name": "Slack"}),
        ),
        (GetChannelRequest(channel_id=11), GenericOperationResponse, ("GET", "/api/channel/11", {}, None)),
        (
            UpdateChannelRequest(channel_id=11, body={"name": "Slack"}),
            GenericOperationResponse,
            ("PUT", "/api/channel/11", {}, {"name": "Slack"}),
        ),
        (
            CreateCloudMigrationRequest(body={"environment": "prod"}),
            CreateCloudMigrationResponse,
            ("POST", "/api/cloud-migration", {}, {"environment": "prod"}),
        ),
        (
            GetCloudMigrationRequest(),
            CloudMigrationStatusResponse,
            ("GET", "/api/cloud-migration", {}, None),
        ),
        (
            CancelCloudMigrationRequest(),
            CancelCloudMigrationResponse,
            ("PUT", "/api/cloud-migration/cancel", {}, None),
        ),
        (CreateCollectionRequest(body={"name": "New"}), Collection, ("POST", "/api/collection", {}, {"name": "New"})),
        (GetCollectionGraphRequest(), GenericOperationResponse, ("GET", "/api/collection/graph", {}, None)),
        (
            PutCollectionRequest(collection_id="7", body={"name": "Updated"}),
            Collection,
            ("PUT", "/api/collection/7", {}, {"name": "Updated"}),
        ),
        (
            DeleteCollectionRequest(collection_id="7"),
            GenericOperationResponse,
            ("DELETE", "/api/collection/7", {}, None),
        ),
        (
            GetCommentRequest(model="card", model_id=13),
            GenericOperationResponse,
            ("GET", "/api/comment", {"model": "card", "model-id": 13}, None),
        ),
        (
            GetCommentMentionsRequest(),
            GenericOperationResponse,
            ("GET", "/api/comment/mentions", {}, None),
        ),
        (
            UpdateCommentRequest(comment_id="7", body={"text": "updated"}),
            GenericOperationResponse,
            ("PUT", "/api/comment/7", {}, {"text": "updated"}),
        ),
        (
            PostCommentReactionRequest(comment_id="11", body={"emoji": "👍"}),
            GenericOperationResponse,
            ("POST", "/api/comment/11/reaction", {}, {"emoji": "👍"}),
        ),
        (
            PostCommentRequest(body={"text": "Hi"}),
            GenericOperationResponse,
            ("POST", "/api/comment", {}, {"text": "Hi"}),
        ),
        (GetDashboardRequest(dashboard_id=9), Dashboard, ("GET", "/api/dashboard/9", {}, None)),
        (GetDashboardEmbeddableRequest(), GenericOperationResponse, ("GET", "/api/dashboard/embeddable", {}, None)),
        (GetDashboardPublicRequest(), GenericOperationResponse, ("GET", "/api/dashboard/public", {}, None)),
        (PostDashboardRequest(body={"name": "Sales"}), Dashboard, ("POST", "/api/dashboard", {}, {"name": "Sales"})),
        (
            PostDashboardPivotQueryRequest(dashboard_id=9, dashcard_id=10, card_id=11, body={"x": 1}),
            GenericOperationResponse,
            ("POST", "/api/dashboard/pivot/9/dashcard/10/card/11/query", {}, {"x": 1}),
        ),
        (
            SaveDashboardRequest(body={"name": "Sales"}),
            GenericOperationResponse,
            ("POST", "/api/dashboard/save", {}, {"name": "Sales"}),
        ),
        (
            SaveDashboardToCollectionRequest(parent_collection_id="root", body={"name": "Sales"}),
            GenericOperationResponse,
            ("POST", "/api/dashboard/save/collection/root", {}, {"name": "Sales"}),
        ),
        (
            GetDashboardDashcardExecuteRequest(dashboard_id=9, dashcard_id=10, parameters={"id": 1}),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/dashcard/10/execute", {"id": 1}, None),
        ),
        (
            ExecuteDashboardDashcardRequest(dashboard_id=9, dashcard_id=10, parameters={"id": 1}),
            GenericOperationResponse,
            ("POST", "/api/dashboard/9/dashcard/10/execute", {}, {"parameters": {"id": 1}}),
        ),
        (
            CreateDashboardPublicLinkRequest(dashboard_id=9),
            GenericOperationResponse,
            ("POST", "/api/dashboard/9/public_link", {}, None),
        ),
        (
            DeleteDashboardPublicLinkRequest(dashboard_id=9),
            GenericOperationResponse,
            ("DELETE", "/api/dashboard/9/public_link", {}, None),
        ),
        (CopyDashboardRequest(from_dashboard_id=9), Dashboard, ("POST", "/api/dashboard/9/copy", {}, None)),
        (DeleteDashboardRequest(dashboard_id=9), GenericOperationResponse, ("DELETE", "/api/dashboard/9", {}, None)),
        (
            UpdateDashboardRequest(dashboard_id=9, body={"name": "Sales"}),
            Dashboard,
            ("PUT", "/api/dashboard/9", {}, {"name": "Sales"}),
        ),
        (
            UpdateDashboardCardsRequest(dashboard_id=9, body={"cards": []}),
            GenericOperationResponse,
            ("PUT", "/api/dashboard/9/cards", {}, {"cards": []}),
        ),
        (
            GetDashboardItemsRequest(dashboard_id=9),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/items", {}, None),
        ),
        (
            DashboardParamRemappingRequest(dashboard_id=9, param_key="abc", parameters={"value": 100}),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/params/abc/remapping", {"value": 100}, None),
        ),
        (
            DashboardParamSearchRequest(dashboard_id=9, param_key="abc", query="Orange", parameters={"limit": 10}),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/params/abc/search/Orange", {"limit": 10}, None),
        ),
        (
            DashboardParamValuesRequest(dashboard_id=9, param_key="abc", parameters={"limit": 10}),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/params/abc/values", {"limit": 10}, None),
        ),
        (
            GetDashboardQueryMetadataRequest(dashboard_id=9),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/query_metadata", {}, None),
        ),
        (
            GetDashboardRelatedRequest(dashboard_id=9),
            GenericOperationResponse,
            ("GET", "/api/dashboard/9/related", {}, None),
        ),
        (
            DataStudioTableDiscardValuesRequest(body={"table_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/data-studio/table/discard-values", {}, {"table_ids": [1]}),
        ),
        (
            DataStudioTableEditRequest(body={"table_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/data-studio/table/edit", {}, {"table_ids": [1]}),
        ),
        (
            DataStudioTableRescanValuesRequest(body={"table_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/data-studio/table/rescan-values", {}, {"table_ids": [1]}),
        ),
        (
            DataStudioTableSelectionRequest(body={"table_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/data-studio/table/selection", {}, {"table_ids": [1]}),
        ),
        (
            DataStudioTableSyncSchemaRequest(body={"table_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/data-studio/table/sync-schema", {}, {"table_ids": [1]}),
        ),
        (
            DeleteCommentRequest(comment_id="7"),
            GenericOperationResponse,
            ("DELETE", "/api/comment/7", {}, None),
        ),
        (
            DeleteCommentRequest(comment_id="7"),
            GenericOperationResponse,
            ("DELETE", "/api/comment/7", {}, None),
        ),
        (GetCollectionRootRequest(), Collection, ("GET", "/api/collection/root", {}, None)),
        (
            GetCollectionRootDashboardQuestionCandidatesRequest(),
            GenericOperationResponse,
            ("GET", "/api/collection/root/dashboard-question-candidates", {}, None),
        ),
        (
            GetCollectionRootItemsRequest(),
            GenericOperationResponse,
            ("GET", "/api/collection/root/items", {}, None),
        ),
        (
            GetCollectionTrashRequest(),
            Collection,
            ("GET", "/api/collection/trash", {}, None),
        ),
        (
            GetCollectionDashboardQuestionCandidatesRequest(collection_id="7"),
            GenericOperationResponse,
            ("GET", "/api/collection/7/dashboard-question-candidates", {}, None),
        ),
        (
            GetCollectionItemsRequest(collection_id="7"),
            GenericOperationResponse,
            ("GET", "/api/collection/7/items", {}, None),
        ),
        (
            GetCollectionTreeRequest(),
            GenericOperationResponse,
            ("GET", "/api/collection/tree", {}, None),
        ),
        (
            PostCollectionRootMoveDashboardQuestionCandidatesRequest(body={"card_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/collection/root/move-dashboard-question-candidates", {}, {"card_ids": [1]}),
        ),
        (
            PostCollectionMoveDashboardQuestionCandidatesRequest(collection_id="7", body={"card_ids": [1]}),
            GenericOperationResponse,
            ("POST", "/api/collection/7/move-dashboard-question-candidates", {}, {"card_ids": [1]}),
        ),
        (
            PutCollectionGraphRequest(body={"groups": ["admin"]}),
            GenericOperationResponse,
            ("PUT", "/api/collection/graph", {}, {"groups": ["admin"]}),
        ),
        (
            GetCardCollectionsRequest(card_ids=[1, 2], collection_id="root"),
            GenericOperationResponse,
            ("POST", "/api/card/collections", {}, {"card_ids": [1, 2], "collection_id": "root"}),
        ),
        (GetCardEmbeddableRequest(), GenericOperationResponse, ("GET", "/api/card/embeddable", {}, None)),
        (
            PostCardPivotQueryRequest(card_id=13, body={"x": 1}),
            GenericOperationResponse,
            ("POST", "/api/card/pivot/13/query", {}, {"x": 1}),
        ),
        (GetCardPublicRequest(), GenericOperationResponse, ("GET", "/api/card/public", {}, None)),
        (
            CardParamsSearchRequest(card_id=13, param_key="abc", query="Orange"),
            GenericOperationResponse,
            ("GET", "/api/card/13/params/abc/search/Orange", {}, None),
        ),
        (
            CardParamsValuesRequest(card_id=13, param_key="abc"),
            GenericOperationResponse,
            ("GET", "/api/card/13/params/abc/values", {}, None),
        ),
        (
            CreateCardPublicLinkRequest(card_id=13),
            GenericOperationResponse,
            ("POST", "/api/card/13/public_link", {}, None),
        ),
        (
            DeleteCardPublicLinkRequest(card_id=13),
            GenericOperationResponse,
            ("DELETE", "/api/card/13/public_link", {}, None),
        ),
        (
            CardQueryRequest(card_id=13, body={"x": 1}),
            GenericOperationResponse,
            ("POST", "/api/card/13/query", {}, {"x": 1}),
        ),
        (
            CardQueryExportRequest(
                card_id=13, export_format="csv", body={"x": 1}, pivot_results=True, format_rows=False
            ),
            GenericOperationResponse,
            ("POST", "/api/card/13/query/csv", {"pivot-results": True, "format-rows": False}, {"x": 1}),
        ),
        (UpdateCardRequest(card_id=13, body={"name": "x"}), Card, ("PUT", "/api/card/13", {}, {"name": "x"})),
        (DeleteCardRequest(card_id=13), GenericOperationResponse, ("DELETE", "/api/card/13", {}, None)),
        (
            CardsDashboardsRequest(card_ids=[1, 2]),
            CardsDashboardsResponse,
            ("POST", "/api/cards/dashboards", {}, {"card_ids": [1, 2]}),
        ),
        (
            MoveCardsRequest(body={"card_ids": [1], "collection_id": "root"}),
            GenericOperationResponse,
            ("POST", "/api/cards/move", {}, {"card_ids": [1], "collection_id": "root"}),
        ),
        (
            CopyCardRequest(card_id=13, body={"name": "Copy"}),
            Card,
            ("POST", "/api/card/13/copy", {}, {"name": "Copy"}),
        ),
        (GetCardDashboardsRequest(card_id=13), GenericOperationResponse, ("GET", "/api/card/13/dashboards", {}, None)),
        (
            CardRemappingRequest(card_id=13, param_key="abc"),
            GenericOperationResponse,
            ("GET", "/api/card/13/params/abc/remapping", {}, None),
        ),
        (
            GetCardQueryMetadataRequest(card_id=13),
            GenericOperationResponse,
            ("GET", "/api/card/13/query_metadata", {}, None),
        ),
        (GetCardSeriesRequest(card_id=13), GenericOperationResponse, ("GET", "/api/card/13/series", {}, None)),
        (
            GetUserKeyValueNamespaceRequest(namespace="user"),
            GenericOperationResponse,
            ("GET", "/api/user-key-value/namespace/user", {}, None),
        ),
        (
            PutUserKeyValueNamespaceKeyRequest(namespace="user", key="foo", body={"value": "bar"}),
            GenericOperationResponse,
            ("PUT", "/api/user-key-value/namespace/user/key/foo", {}, {"value": "bar"}),
        ),
        (
            GetUserKeyValueNamespaceKeyRequest(namespace="user", key="foo"),
            GenericOperationResponse,
            ("GET", "/api/user-key-value/namespace/user/key/foo", {}, None),
        ),
        (
            DeleteUserKeyValueNamespaceKeyRequest(namespace="user", key="foo"),
            GenericOperationResponse,
            ("DELETE", "/api/user-key-value/namespace/user/key/foo", {}, None),
        ),
    ]

    for request_model, response_type, expected_call in cases:
        stub = _StubClient({"id": 5, "name": "action"})
        response = _run(request_model.do(stub))

        assert isinstance(response, response_type)
        assert stub.calls == [expected_call]


def test_list_requests_use_expected_paths() -> None:
    for request_model, response_type, expected_path in [
        (ListCardsRequest(), ListCardsResponse, "/api/card"),
        (ListChannelsRequest(), ListChannelsResponse, "/api/channel"),
        (ListUsersRequest(), ListUsersResponse, "/api/user"),
        (ListCollectionsRequest(), ListCollectionsResponse, "/api/collection"),
        (ListTablesRequest(), ListTablesResponse, "/api/table"),
    ]:
        stub = _StubClient({"data": []})
        response = _run(request_model.do(stub))

        assert isinstance(response, response_type)
        assert stub.calls == [("GET", expected_path, {}, None)]


def test_get_path_based_requests_use_expected_paths() -> None:
    expectations = [
        (GetDatabaseRequest(database_id=4), "/api/database/4", Database),
        (GetCardRequest(card_id=8), "/api/card/8", Card),
        (GetDashboardRequest(dashboard_id=9), "/api/dashboard/9", Dashboard),
        (GetUserRequest(user_id=10), "/api/user/10", User),
        (
            GetUserKeyValueNamespaceRequest(namespace="user"),
            "/api/user-key-value/namespace/user",
            GenericOperationResponse,
        ),
        (
            GetUserKeyValueNamespaceKeyRequest(namespace="user", key="foo"),
            "/api/user-key-value/namespace/user/key/foo",
            GenericOperationResponse,
        ),
        (GetCollectionRequest(collection_id="c1"), "/api/collection/c1", Collection),
        (GetTableRequest(table_id=11), "/api/table/11", Table),
        (GetFieldRequest(field_id=12), "/api/field/12", MetabaseField),
    ]
    for request, path, model_type in expectations:
        stub = _StubClient({"id": 1, "name": "x"})
        response = _run(request.do(stub))
        assert isinstance(response, model_type)
        assert stub.calls[0][0] == "GET"
        assert stub.calls[0][1] == path


def test_get_card_and_dashboard_requests_use_path_parameters() -> None:
    card_client = _StubClient({"id": 7, "name": "card", "display": "table"})
    dashboard_client = _StubClient({"id": 8, "name": "dashboard", "collection_id": 3})

    card_result = _run(GetCardRequest(card_id=7).do(card_client))
    dashboard_result = _run(GetDashboardRequest(dashboard_id=8).do(dashboard_client))

    assert card_result.id == 7
    assert card_client.calls[0][0] == "GET"
    assert card_client.calls[0][1] == "/api/card/7"
    assert dashboard_result.id == 8
    assert dashboard_client.calls[0][1] == "/api/dashboard/8"


def _run[T](coro: Coroutine[object, object, T]) -> T:
    return asyncio.run(coro)


def _build_mock_endpoint_responses() -> dict[tuple[str, str], dict[str, object]]:
    return {
        ("GET", "/api/action"): {"data": [{"id": 1, "name": "action"}]},
        ("POST", "/api/action"): {"id": 2, "name": "created action"},
        ("GET", "/api/action/public"): {"data": [{"id": 3, "name": "public"}]},
        ("GET", "/api/action/5"): {"id": 5, "name": "action5"},
        ("DELETE", "/api/action/5"): {"ok": True},
        ("GET", "/api/action/5/execute"): {"values": []},
        ("PUT", "/api/action/5"): {"id": 5, "name": "updated action"},
        ("POST", "/api/action/5/execute"): {"ok": True},
        ("POST", "/api/action/5/public_link"): {"uuid": "abc"},
        ("DELETE", "/api/action/5/public_link"): {"ok": True},
        ("GET", "/api/user/current"): {"id": 9, "email": "client@example.com"},
        ("GET", "/api/card/11"): {"id": 11, "name": "card", "display": "bar"},
        ("GET", "/api/database"): {"data": [{"id": 2, "name": "main", "engine": "postgres"}]},
        ("POST", "/api/cloud-migration"): {"id": "migration-1", "status": "created"},
        ("GET", "/api/cloud-migration"): {"id": "migration-1", "status": "ready"},
        ("PUT", "/api/cloud-migration/cancel"): {"id": "migration-1", "status": "canceled"},
        ("POST", "/api/database"): {"id": 9, "name": "analytics", "engine": "postgres"},
        ("POST", "/api/card"): {"id": 12, "name": "Orders", "display": "table", "type": "question"},
        ("GET", "/api/card"): {"data": [{"id": 5, "name": "card", "display": "line"}]},
        ("GET", "/api/dashboard"): {"data": [{"id": 6, "name": "dash", "collection_id": 1}]},
        ("GET", "/api/dashboard/embeddable"): {"ok": True},
        ("GET", "/api/dashboard/public"): {"ok": True},
        ("POST", "/api/dashboard"): {"id": 7, "name": "Sales", "collection_id": 1},
        ("POST", "/api/dashboard/pivot/3/dashcard/4/card/5/query"): {"rows": []},
        ("POST", "/api/dashboard/save"): {"id": 8},
        ("POST", "/api/dashboard/save/collection/root"): {"id": 9},
        ("GET", "/api/dashboard/3/dashcard/4/execute"): {"values": []},
        ("POST", "/api/dashboard/3/dashcard/4/execute"): {"ok": True},
        ("POST", "/api/dashboard/3/public_link"): {"uuid": "dash"},
        ("DELETE", "/api/dashboard/3/public_link"): {"ok": True},
        ("POST", "/api/dashboard/3/copy"): {"id": 10, "name": "Copied"},
        ("DELETE", "/api/dashboard/3"): {"ok": True},
        ("PUT", "/api/dashboard/3"): {"id": 3, "name": "Updated"},
        ("PUT", "/api/dashboard/3/cards"): {"ok": True},
        ("GET", "/api/dashboard/3/items"): {"items": []},
        ("GET", "/api/dashboard/3/params/abc/remapping"): {"value": "A"},
        ("GET", "/api/dashboard/3/params/abc/search/Orange"): {"values": ["Orange"]},
        ("GET", "/api/dashboard/3/params/abc/values"): {"values": ["Orange"]},
        ("GET", "/api/dashboard/3/query_metadata"): {"metadata": []},
        ("GET", "/api/dashboard/3/related"): {"items": []},
        ("POST", "/api/data-studio/table/discard-values"): {"ok": True},
        ("POST", "/api/data-studio/table/edit"): {"ok": True},
        ("POST", "/api/data-studio/table/rescan-values"): {"ok": True},
        ("POST", "/api/data-studio/table/selection"): {"tables": []},
        ("POST", "/api/data-studio/table/sync-schema"): {"ok": True},
        ("GET", "/api/user"): {"data": [{"id": 4, "email": "user@example.com", "first_name": "Ada"}]},
        ("GET", "/api/user-key-value/namespace/user"): {"namespace": "user", "data": {"foo": "bar"}},
        ("PUT", "/api/user-key-value/namespace/user/key/foo"): {"status": "stored", "value": "bar"},
        ("GET", "/api/user-key-value/namespace/user/key/foo"): {"value": "bar"},
        ("DELETE", "/api/user-key-value/namespace/user/key/foo"): {"status": "deleted"},
        ("GET", "/api/collection"): {"data": [{"id": 7, "name": "collection"}]},
        ("POST", "/api/collection"): {"id": 15, "name": "New"},
        ("GET", "/api/collection/graph"): {"groups": ["admin"]},
        ("PUT", "/api/collection/graph"): {"id": 1},
        ("GET", "/api/collection/root"): {"id": "root", "name": "Root"},
        ("GET", "/api/collection/root/dashboard-question-candidates"): {"cards": [{"id": 1}]},
        ("GET", "/api/collection/root/items"): {"cards": [{"id": 2}]},
        ("GET", "/api/collection/7/dashboard-question-candidates"): {"cards": [{"id": 3}]},
        ("GET", "/api/collection/7/items"): {"cards": [{"id": 4}]},
        ("GET", "/api/collection/trash"): {"id": "trash", "name": "Trash"},
        ("GET", "/api/collection/tree"): {"id": "collections", "children": []},
        ("POST", "/api/collection/root/move-dashboard-question-candidates"): {"updated": True},
        ("POST", "/api/collection/7/move-dashboard-question-candidates"): {"updated": True},
        ("PUT", "/api/collection/7"): {"id": 7, "name": "Updated"},
        ("DELETE", "/api/collection/7"): {"ok": True},
        ("GET", "/api/comment"): {"comments": [{"id": 1, "text": "Hi"}]},
        ("GET", "/api/comment/mentions"): {"mentions": [{"id": 1, "name": "alice"}]},
        ("PUT", "/api/comment/7"): {"ok": True},
        ("POST", "/api/comment/11/reaction"): {"ok": True},
        ("POST", "/api/comment"): {"ok": True},
        ("DELETE", "/api/comment/7"): {"ok": True},
        ("GET", "/api/table"): {"data": [{"id": 8, "name": "table", "schema": "public", "db_id": 1}]},
        ("GET", "/api/database/4"): {"id": 4, "name": "db4", "engine": "postgres"},
        ("GET", "/api/user/10"): {"id": 10, "email": "u10@example.com", "first_name": "Turing"},
        ("GET", "/api/collection/c1"): {"id": "c1", "name": "col"},
        ("GET", "/api/table/11"): {"id": 11, "name": "table11", "schema": "public", "db_id": 4},
        ("GET", "/api/field/12"): {"id": 12, "name": "field12", "table_id": 11},
        ("GET", "/api/dashboard/3"): {"id": 3, "name": "dash"},
    }


def test_client_run_endpoint_requests_return_models() -> None:
    mock_responses = _build_mock_endpoint_responses()

    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.headers.get("X-API-Key") == "abc"
        payload = mock_responses.get((request.method, request.url.path))
        if payload is not None:
            return httpx.Response(200, json=payload)
        return httpx.Response(200, json={"id": 3, "name": "dash"})

    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=httpx.MockTransport(handler), verify=False),
    )

    actions = _run(client.run(ListActionsRequest()))
    created_action = _run(client.run(CreateActionRequest(body={"name": "created action"})))
    public_actions = _run(client.run(ListPublicActionsRequest()))
    action = _run(client.run(GetActionRequest(action_id=5)))
    deleted_action = _run(client.run(DeleteActionRequest(action_id=5)))
    action_execute = _run(client.run(GetActionExecuteRequest(action_id=5, parameters={"id": 1})))
    updated_action = _run(client.run(UpdateActionRequest(action_id=5, body={"name": "updated action"})))
    executed_action = _run(client.run(ExecuteActionRequest(action_id=5, parameters={"id": 1})))
    action_public_link = _run(client.run(CreateActionPublicLinkRequest(action_id=5)))
    deleted_action_public_link = _run(client.run(DeleteActionPublicLinkRequest(action_id=5)))
    current_user = _run(client.run(CurrentUserRequest()))
    dashboard = _run(client.run(GetDashboardRequest(dashboard_id=3)))
    card = _run(client.run(GetCardRequest(card_id=11)))
    created_card = _run(
        client.run(
            CreateCardRequest(
                name="Orders",
                dataset_query={"database": 1, "type": "query", "query": {"source-table": 2}},
                display="table",
            ),
        ),
    )
    databases = _run(client.run(ListDatabasesRequest()))
    channels = _run(client.run(ListChannelsRequest()))
    create_channel = _run(client.run(CreateChannelRequest(body={"name": "Slack"})))
    test_channel = _run(client.run(TestChannelRequest(body={"name": "Slack"})))
    channel = _run(client.run(GetChannelRequest(channel_id=11)))
    updated_channel = _run(client.run(UpdateChannelRequest(channel_id=11, body={"name": "Slack"})))
    cloud_migration = _run(client.run(CreateCloudMigrationRequest(body={"environment": "prod"})))
    latest_cloud_migration = _run(client.run(GetCloudMigrationRequest()))
    canceled_cloud_migration = _run(client.run(CancelCloudMigrationRequest()))
    created_collection = _run(client.run(CreateCollectionRequest(body={"name": "New"})))
    created_dashboard = _run(client.run(PostDashboardRequest(body={"name": "Sales"})))
    updated_collection = _run(client.run(PutCollectionRequest(collection_id="7", body={"name": "Updated"})))
    deleted_collection = _run(client.run(DeleteCollectionRequest(collection_id="7")))
    comments = _run(client.run(GetCommentRequest(model="card", model_id=13)))
    comments_mentions = _run(client.run(GetCommentMentionsRequest()))
    created_comment = _run(client.run(PostCommentRequest(body={"text": "Hi"})))
    updated_comment = _run(client.run(UpdateCommentRequest(comment_id="7", body={"text": "updated"})))
    reaction_comment = _run(client.run(PostCommentReactionRequest(comment_id="11", body={"emoji": "👍"})))
    deleted_comment = _run(client.run(DeleteCommentRequest(comment_id="7")))
    user_key_values = _run(client.run(GetUserKeyValueNamespaceRequest(namespace="user")))
    put_user_key_value = _run(
        client.run(PutUserKeyValueNamespaceKeyRequest(namespace="user", key="foo", body={"value": "bar"}))
    )
    get_user_key_value = _run(client.run(GetUserKeyValueNamespaceKeyRequest(namespace="user", key="foo")))
    delete_user_key_value = _run(client.run(DeleteUserKeyValueNamespaceKeyRequest(namespace="user", key="foo")))
    collection_graph = _run(client.run(GetCollectionGraphRequest()))
    collection_graph_update = _run(client.run(PutCollectionGraphRequest(body={"groups": ["admin"]})))
    collection_root = _run(client.run(GetCollectionRootRequest()))
    collection_root_candidates = _run(client.run(GetCollectionRootDashboardQuestionCandidatesRequest()))
    collection_root_items = _run(client.run(GetCollectionRootItemsRequest()))
    collection_root_candidates_moved = _run(
        client.run(PostCollectionRootMoveDashboardQuestionCandidatesRequest(body={"card_ids": [1]}))
    )
    collection_move_candidates = _run(
        client.run(PostCollectionMoveDashboardQuestionCandidatesRequest(collection_id="7", body={"card_ids": [1]}))
    )
    collection_dashboard_question_candidates = _run(
        client.run(GetCollectionDashboardQuestionCandidatesRequest(collection_id="7"))
    )
    collection_items = _run(client.run(GetCollectionItemsRequest(collection_id="7")))
    collection_trash = _run(client.run(GetCollectionTrashRequest()))
    collection_tree = _run(client.run(GetCollectionTreeRequest()))
    cards = _run(client.run(ListCardsRequest()))
    cards_dashboards = _run(client.run(CardsDashboardsRequest(card_ids=[1, 2])))
    moved_cards = _run(client.run(MoveCardsRequest(body={"card_ids": [1], "collection_id": "root"})))
    dashboards = _run(client.run(ListDashboardsRequest()))
    dashboard_embeddable = _run(client.run(GetDashboardEmbeddableRequest()))
    dashboard_public = _run(client.run(GetDashboardPublicRequest()))
    dashboard_pivot = _run(
        client.run(PostDashboardPivotQueryRequest(dashboard_id=3, dashcard_id=4, card_id=5, body={"x": 1}))
    )
    saved_dashboard = _run(client.run(SaveDashboardRequest(body={"name": "Sales"})))
    saved_dashboard_to_collection = _run(
        client.run(SaveDashboardToCollectionRequest(parent_collection_id="root", body={"name": "Sales"}))
    )
    dashboard_dashcard_execute = _run(
        client.run(GetDashboardDashcardExecuteRequest(dashboard_id=3, dashcard_id=4, parameters={"id": 1}))
    )
    executed_dashboard_dashcard = _run(
        client.run(ExecuteDashboardDashcardRequest(dashboard_id=3, dashcard_id=4, parameters={"id": 1}))
    )
    dashboard_public_link = _run(client.run(CreateDashboardPublicLinkRequest(dashboard_id=3)))
    deleted_dashboard_public_link = _run(client.run(DeleteDashboardPublicLinkRequest(dashboard_id=3)))
    copied_dashboard = _run(client.run(CopyDashboardRequest(from_dashboard_id=3)))
    deleted_dashboard = _run(client.run(DeleteDashboardRequest(dashboard_id=3)))
    updated_dashboard = _run(client.run(UpdateDashboardRequest(dashboard_id=3, body={"name": "Updated"})))
    updated_dashboard_cards = _run(client.run(UpdateDashboardCardsRequest(dashboard_id=3, body={"cards": []})))
    dashboard_items = _run(client.run(GetDashboardItemsRequest(dashboard_id=3)))
    dashboard_param_remapping = _run(
        client.run(DashboardParamRemappingRequest(dashboard_id=3, param_key="abc", parameters={"value": 100}))
    )
    dashboard_param_search = _run(
        client.run(
            DashboardParamSearchRequest(dashboard_id=3, param_key="abc", query="Orange", parameters={"limit": 10})
        )
    )
    dashboard_param_values = _run(
        client.run(DashboardParamValuesRequest(dashboard_id=3, param_key="abc", parameters={"limit": 10}))
    )
    dashboard_query_metadata = _run(client.run(GetDashboardQueryMetadataRequest(dashboard_id=3)))
    dashboard_related = _run(client.run(GetDashboardRelatedRequest(dashboard_id=3)))
    data_studio_table_discard_values = _run(
        client.run(DataStudioTableDiscardValuesRequest(body={"table_ids": [1]}))
    )
    data_studio_table_edit = _run(client.run(DataStudioTableEditRequest(body={"table_ids": [1]})))
    data_studio_table_rescan_values = _run(
        client.run(DataStudioTableRescanValuesRequest(body={"table_ids": [1]}))
    )
    data_studio_table_selection = _run(
        client.run(DataStudioTableSelectionRequest(body={"table_ids": [1]}))
    )
    data_studio_table_sync_schema = _run(
        client.run(DataStudioTableSyncSchemaRequest(body={"table_ids": [1]}))
    )
    users = _run(client.run(ListUsersRequest()))
    collections = _run(client.run(ListCollectionsRequest()))
    tables = _run(client.run(ListTablesRequest()))
    db = _run(client.run(GetDatabaseRequest(database_id=4)))
    user = _run(client.run(GetUserRequest(user_id=10)))
    collection = _run(client.run(GetCollectionRequest(collection_id="c1")))
    table = _run(client.run(GetTableRequest(table_id=11)))
    field = _run(client.run(GetFieldRequest(field_id=12)))

    assert isinstance(actions, ListActionsResponse)
    assert isinstance(created_action, Action)
    assert isinstance(public_actions, ListActionsResponse)
    assert isinstance(action, Action)
    assert isinstance(deleted_action, ActionExecutionResponse)
    assert isinstance(action_execute, ActionExecutionResponse)
    assert isinstance(updated_action, Action)
    assert isinstance(executed_action, ActionExecutionResponse)
    assert isinstance(action_public_link, ActionExecutionResponse)
    assert isinstance(deleted_action_public_link, ActionExecutionResponse)
    assert isinstance(current_user, CurrentUserResponse)
    assert current_user.email == "client@example.com"
    assert isinstance(dashboard, Dashboard)
    assert dashboard.id == 3
    assert isinstance(card, Card)
    assert isinstance(created_card, Card)
    assert created_card.name == "Orders"
    assert isinstance(databases, ListDatabasesResponse)
    assert databases.databases[0].engine == "postgres"
    assert isinstance(channels, ListChannelsResponse)
    assert isinstance(create_channel, GenericOperationResponse)
    assert isinstance(test_channel, GenericOperationResponse)
    assert isinstance(channel, GenericOperationResponse)
    assert isinstance(updated_channel, GenericOperationResponse)
    assert isinstance(cloud_migration, CreateCloudMigrationResponse)
    assert isinstance(latest_cloud_migration, CloudMigrationStatusResponse)
    assert isinstance(canceled_cloud_migration, CancelCloudMigrationResponse)
    assert isinstance(created_collection, Collection)
    assert created_collection.name == "New"
    assert isinstance(created_dashboard, Dashboard)
    assert created_dashboard.name == "Sales"
    assert isinstance(updated_collection, Collection)
    assert updated_collection.name == "Updated"
    assert isinstance(deleted_collection, GenericOperationResponse)
    assert isinstance(comments, GenericOperationResponse)
    assert isinstance(comments_mentions, GenericOperationResponse)
    assert isinstance(created_comment, GenericOperationResponse)
    assert isinstance(updated_comment, GenericOperationResponse)
    assert isinstance(reaction_comment, GenericOperationResponse)
    assert isinstance(deleted_comment, GenericOperationResponse)
    assert isinstance(user_key_values, GenericOperationResponse)
    assert isinstance(put_user_key_value, GenericOperationResponse)
    assert isinstance(get_user_key_value, GenericOperationResponse)
    assert isinstance(delete_user_key_value, GenericOperationResponse)
    assert isinstance(collection_graph, GenericOperationResponse)
    assert isinstance(collection_graph_update, GenericOperationResponse)
    assert isinstance(collection_root, Collection)
    assert collection_root.id == "root"
    assert collection_root.name == "Root"
    assert isinstance(collection_root_candidates, GenericOperationResponse)
    assert isinstance(collection_root_items, GenericOperationResponse)
    assert isinstance(collection_root_candidates_moved, GenericOperationResponse)
    assert isinstance(collection_move_candidates, GenericOperationResponse)
    assert isinstance(collection_dashboard_question_candidates, GenericOperationResponse)
    assert isinstance(collection_items, GenericOperationResponse)
    assert isinstance(collection_trash, Collection)
    assert collection_trash.id == "trash"
    assert collection_trash.name == "Trash"
    assert isinstance(collection_tree, GenericOperationResponse)
    assert collection_tree.model_dump(exclude_none=True) == {"id": "collections", "children": []}
    assert isinstance(cards, ListCardsResponse)
    assert isinstance(cards_dashboards, CardsDashboardsResponse)
    assert isinstance(moved_cards, GenericOperationResponse)
    assert isinstance(dashboards, ListDashboardsResponse)
    assert isinstance(dashboard_embeddable, GenericOperationResponse)
    assert isinstance(dashboard_public, GenericOperationResponse)
    assert isinstance(dashboard_pivot, GenericOperationResponse)
    assert isinstance(saved_dashboard, GenericOperationResponse)
    assert isinstance(saved_dashboard_to_collection, GenericOperationResponse)
    assert isinstance(dashboard_dashcard_execute, GenericOperationResponse)
    assert isinstance(executed_dashboard_dashcard, GenericOperationResponse)
    assert isinstance(dashboard_public_link, GenericOperationResponse)
    assert isinstance(deleted_dashboard_public_link, GenericOperationResponse)
    assert isinstance(copied_dashboard, Dashboard)
    assert isinstance(deleted_dashboard, GenericOperationResponse)
    assert isinstance(updated_dashboard, Dashboard)
    assert isinstance(updated_dashboard_cards, GenericOperationResponse)
    assert isinstance(dashboard_items, GenericOperationResponse)
    assert isinstance(dashboard_param_remapping, GenericOperationResponse)
    assert isinstance(dashboard_param_search, GenericOperationResponse)
    assert isinstance(dashboard_param_values, GenericOperationResponse)
    assert isinstance(dashboard_query_metadata, GenericOperationResponse)
    assert isinstance(dashboard_related, GenericOperationResponse)
    assert isinstance(data_studio_table_discard_values, GenericOperationResponse)
    assert isinstance(data_studio_table_edit, GenericOperationResponse)
    assert isinstance(data_studio_table_rescan_values, GenericOperationResponse)
    assert isinstance(data_studio_table_selection, GenericOperationResponse)
    assert isinstance(data_studio_table_sync_schema, GenericOperationResponse)
    assert isinstance(users, ListUsersResponse)
    assert isinstance(collections, ListCollectionsResponse)
    assert isinstance(tables, ListTablesResponse)
    assert db.name == "db4"
    assert isinstance(user, User)
    assert user.id == 10
    assert isinstance(collection, Collection)
    assert isinstance(table, Table)
    assert isinstance(field, MetabaseField)
