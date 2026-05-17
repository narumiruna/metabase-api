from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from datetime import UTC
from datetime import datetime

import httpx

from metabaseapi.client import MetabaseClient
from metabaseapi.metabase import Action
from metabaseapi.metabase import ActionExecutionResponse
from metabaseapi.metabase import CancelCloudMigrationRequest
from metabaseapi.metabase import Card
from metabaseapi.metabase import CardParamsSearchRequest
from metabaseapi.metabase import CardParamsValuesRequest
from metabaseapi.metabase import CardQueryExportRequest
from metabaseapi.metabase import CardQueryRequest
from metabaseapi.metabase import CardRemappingRequest
from metabaseapi.metabase import CardsDashboardsRequest
from metabaseapi.metabase import CardsDashboardsResponse
from metabaseapi.metabase import Collection
from metabaseapi.metabase import CopyCardRequest
from metabaseapi.metabase import CreateActionPublicLinkRequest
from metabaseapi.metabase import CreateActionRequest
from metabaseapi.metabase import CreateCardPublicLinkRequest
from metabaseapi.metabase import CreateCardRequest
from metabaseapi.metabase import CreateChannelRequest
from metabaseapi.metabase import CreateCloudMigrationRequest
from metabaseapi.metabase import CreateCollectionRequest
from metabaseapi.metabase import CreateDatabaseRequest
from metabaseapi.metabase import CurrentUserRequest
from metabaseapi.metabase import CurrentUserResponse
from metabaseapi.metabase import Dashboard
from metabaseapi.metabase import Database
from metabaseapi.metabase import DeleteActionPublicLinkRequest
from metabaseapi.metabase import DeleteActionRequest
from metabaseapi.metabase import DeleteCacheRequest
from metabaseapi.metabase import DeleteCardPublicLinkRequest
from metabaseapi.metabase import DeleteCardRequest
from metabaseapi.metabase import DeleteCollectionRequest
from metabaseapi.metabase import DeleteCommentRequest
from metabaseapi.metabase import ExecuteActionRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetActionExecuteRequest
from metabaseapi.metabase import GetActionRequest
from metabaseapi.metabase import GetCacheRequest
from metabaseapi.metabase import GetCardCollectionsRequest
from metabaseapi.metabase import GetCardDashboardsRequest
from metabaseapi.metabase import GetCardEmbeddableRequest
from metabaseapi.metabase import GetCardPublicRequest
from metabaseapi.metabase import GetCardQueryMetadataRequest
from metabaseapi.metabase import GetCardRequest
from metabaseapi.metabase import GetCardSeriesRequest
from metabaseapi.metabase import GetChannelRequest
from metabaseapi.metabase import GetCloudMigrationRequest
from metabaseapi.metabase import GetCollectionDashboardQuestionCandidatesRequest
from metabaseapi.metabase import GetCollectionGraphRequest
from metabaseapi.metabase import GetCollectionItemsRequest
from metabaseapi.metabase import GetCollectionRequest
from metabaseapi.metabase import GetCollectionRootDashboardQuestionCandidatesRequest
from metabaseapi.metabase import GetCollectionRootItemsRequest
from metabaseapi.metabase import GetCollectionRootRequest
from metabaseapi.metabase import GetCollectionTrashRequest
from metabaseapi.metabase import GetCollectionTreeRequest
from metabaseapi.metabase import GetCommentMentionsRequest
from metabaseapi.metabase import GetCommentRequest
from metabaseapi.metabase import GetDashboardRequest
from metabaseapi.metabase import GetDatabaseRequest
from metabaseapi.metabase import GetFieldRequest
from metabaseapi.metabase import GetTableRequest
from metabaseapi.metabase import GetUserRequest
from metabaseapi.metabase import InvalidateCacheRequest
from metabaseapi.metabase import ListActionsRequest
from metabaseapi.metabase import ListActionsResponse
from metabaseapi.metabase import ListCardsRequest
from metabaseapi.metabase import ListCardsResponse
from metabaseapi.metabase import ListChannelsRequest
from metabaseapi.metabase import ListChannelsResponse
from metabaseapi.metabase import ListCollectionsRequest
from metabaseapi.metabase import ListCollectionsResponse
from metabaseapi.metabase import ListDashboardsResponse
from metabaseapi.metabase import ListDatabasesRequest
from metabaseapi.metabase import ListDatabasesResponse
from metabaseapi.metabase import ListPublicActionsRequest
from metabaseapi.metabase import ListTablesRequest
from metabaseapi.metabase import ListTablesResponse
from metabaseapi.metabase import ListUsersRequest
from metabaseapi.metabase import ListUsersResponse
from metabaseapi.metabase import MetabaseField
from metabaseapi.metabase import MoveCardsRequest
from metabaseapi.metabase import PostCardPivotQueryRequest
from metabaseapi.metabase import PostCollectionMoveDashboardQuestionCandidatesRequest
from metabaseapi.metabase import PostCollectionRootMoveDashboardQuestionCandidatesRequest
from metabaseapi.metabase import PostCommentReactionRequest
from metabaseapi.metabase import PostCommentRequest
from metabaseapi.metabase import PostDashboardRequest
from metabaseapi.metabase import PutCacheRequest
from metabaseapi.metabase import PutCollectionGraphRequest
from metabaseapi.metabase import PutCollectionRequest
from metabaseapi.metabase import Table
from metabaseapi.metabase import TestChannelRequest
from metabaseapi.metabase import UpdateActionRequest
from metabaseapi.metabase import UpdateCardRequest
from metabaseapi.metabase import UpdateChannelRequest
from metabaseapi.metabase import UpdateCommentRequest
from metabaseapi.metabase import User
from metabaseapi.models import QueryParamValue


class _StubClient:
    def __init__(self, response: object) -> None:
        self.response = response
        self.calls: list[tuple[str, str, dict[str, QueryParamValue], object | None]] = []

    async def request(
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

    result = CurrentUserRequest().do_sync(client)

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
    response = request.do_sync(client)

    assert isinstance(response, ListDatabasesResponse)
    assert len(response.databases) == 1
    assert response.databases[0].name == "db"
    assert client.calls == [("GET", "/api/database", {}, None)]


def test_create_database_request_includes_body_for_post() -> None:
    payload = {"id": 1, "name": "analytics", "engine": "postgres", "details": {"host": "db.local"}}
    client = _StubClient(payload)

    request = CreateDatabaseRequest(name="analytics", engine="postgres", details={"host": "db.local"})
    response = request.do_sync(client)

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
    response = request.do_sync(client)

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
            GenericOperationResponse,
            ("POST", "/api/cloud-migration", {}, {"environment": "prod"}),
        ),
        (
            GetCloudMigrationRequest(),
            GenericOperationResponse,
            ("GET", "/api/cloud-migration", {}, None),
        ),
        (
            CancelCloudMigrationRequest(),
            GenericOperationResponse,
            ("PUT", "/api/cloud-migration/cancel", {}, None),
        ),
        (CreateCollectionRequest(body={"name": "New"}), Collection, ("POST", "/api/collection", {}, {"name": "New"})),
        (GetCollectionGraphRequest(), GenericOperationResponse, ("GET", "/api/collection/graph", {}, None)),
        (
            PutCollectionRequest(collection_id="7", body={"name": "Updated"}),
            GenericOperationResponse,
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
        (PostDashboardRequest(body={"name": "Sales"}), Dashboard, ("POST", "/api/dashboard", {}, {"name": "Sales"})),
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
    ]

    for request_model, response_type, expected_call in cases:
        stub = _StubClient({"id": 5, "name": "action"})
        response = request_model.do_sync(stub)

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
        response = request_model.do_sync(stub)

        assert isinstance(response, response_type)
        assert stub.calls == [("GET", expected_path, {}, None)]


def test_get_path_based_requests_use_expected_paths() -> None:
    expectations = [
        (GetDatabaseRequest(database_id=4), "/api/database/4", Database),
        (GetCardRequest(card_id=8), "/api/card/8", Card),
        (GetDashboardRequest(dashboard_id=9), "/api/dashboard/9", Dashboard),
        (GetUserRequest(user_id=10), "/api/user/10", User),
        (GetCollectionRequest(collection_id="c1"), "/api/collection/c1", Collection),
        (GetTableRequest(table_id=11), "/api/table/11", Table),
        (GetFieldRequest(field_id=12), "/api/field/12", MetabaseField),
    ]
    for request, path, model_type in expectations:
        stub = _StubClient({"id": 1, "name": "x"})
        response = request.do_sync(stub)
        assert isinstance(response, model_type)
        assert stub.calls[0][0] == "GET"
        assert stub.calls[0][1] == path


def test_get_card_and_dashboard_requests_use_path_parameters() -> None:
    card_client = _StubClient({"id": 7, "name": "card", "display": "table"})
    dashboard_client = _StubClient({"id": 8, "name": "dashboard", "collection_id": 3})

    card_result = GetCardRequest(card_id=7).do_sync(card_client)
    dashboard_result = GetDashboardRequest(dashboard_id=8).do_sync(dashboard_client)

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
        ("POST", "/api/database"): {"id": 9, "name": "analytics", "engine": "postgres"},
        ("POST", "/api/card"): {"id": 12, "name": "Orders", "display": "table", "type": "question"},
        ("GET", "/api/card"): {"data": [{"id": 5, "name": "card", "display": "line"}]},
        ("GET", "/api/dashboard"): {"data": [{"id": 6, "name": "dash", "collection_id": 1}]},
        ("POST", "/api/dashboard"): {"id": 7, "name": "Sales", "collection_id": 1},
        ("GET", "/api/user"): {"data": [{"id": 4, "email": "user@example.com", "first_name": "Ada"}]},
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
        ("PUT", "/api/collection/7"): {"updated": True},
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


def test_typed_methods_in_client_return_models() -> None:
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

    actions = _run(client.list_actions_typed())
    created_action = _run(client.create_action_typed({"name": "created action"}))
    public_actions = _run(client.list_public_actions_typed())
    action = _run(client.get_action_typed(5))
    deleted_action = _run(client.delete_action_typed(5))
    action_execute = _run(client.get_action_execute_typed(5, parameters={"id": 1}))
    updated_action = _run(client.update_action_typed(5, {"name": "updated action"}))
    executed_action = _run(client.execute_action_typed(5, parameters={"id": 1}))
    action_public_link = _run(client.create_action_public_link_typed(5))
    deleted_action_public_link = _run(client.delete_action_public_link_typed(5))
    current_user = _run(client.current_user_typed())
    dashboard = _run(client.get_dashboard_typed(3))
    card = _run(client.get_card_typed(11))
    created_card = _run(
        client.create_question_typed(
            name="Orders",
            dataset_query={"database": 1, "type": "query", "query": {"source-table": 2}},
            display="table",
        ),
    )
    databases = _run(client.list_databases_typed())
    channels = _run(client.list_channels_typed())
    create_channel = _run(client.create_channel_typed({"name": "Slack"}))
    test_channel = _run(client.test_channel_typed({"name": "Slack"}))
    channel = _run(client.get_channel_typed(11))
    updated_channel = _run(client.update_channel_typed(11, {"name": "Slack"}))
    cloud_migration = _run(client.create_cloud_migration_typed({"environment": "prod"}))
    latest_cloud_migration = _run(client.get_cloud_migration_typed())
    canceled_cloud_migration = _run(client.cancel_cloud_migration_typed())
    created_collection = _run(client.create_collection_typed({"name": "New"}))
    created_dashboard = _run(client.create_dashboard_typed({"name": "Sales"}))
    updated_collection = _run(client.update_collection_typed("7", {"name": "Updated"}))
    deleted_collection = _run(client.delete_collection_typed("7"))
    comments = _run(client.get_comment_typed(model="card", model_id=13))
    comments_mentions = _run(client.get_comment_mentions_typed())
    created_comment = _run(client.create_comment_typed({"text": "Hi"}))
    updated_comment = _run(client.update_comment_typed("7", {"text": "updated"}))
    reaction_comment = _run(client.post_comment_reaction_typed("11", {"emoji": "👍"}))
    deleted_comment = _run(client.delete_comment_typed("7"))
    collection_graph = _run(client.get_collection_graph_typed())
    collection_graph_update = _run(client.put_collection_graph_typed({"groups": ["admin"]}))
    collection_root = _run(client.get_collection_root_typed())
    collection_root_candidates = _run(client.get_collection_root_dashboard_question_candidates_typed())
    collection_root_items = _run(client.get_collection_root_items_typed())
    collection_root_candidates_moved = _run(
        client.post_collection_root_move_dashboard_question_candidates_typed({"card_ids": [1]})
    )
    collection_move_candidates = _run(
        client.post_collection_move_dashboard_question_candidates_typed("7", {"card_ids": [1]})
    )
    collection_dashboard_question_candidates = _run(client.get_collection_dashboard_question_candidates_typed("7"))
    collection_items = _run(client.get_collection_items_typed("7"))
    collection_trash = _run(client.get_collection_trash_typed())
    collection_tree = _run(client.get_collection_tree_typed())
    cards = _run(client.list_cards_typed())
    cards_dashboards = _run(client.cards_dashboards_typed([1, 2]))
    moved_cards = _run(client.move_cards_typed({"card_ids": [1], "collection_id": "root"}))
    dashboards = _run(client.list_dashboards_typed())
    users = _run(client.list_users_typed())
    collections = _run(client.list_collections_typed())
    tables = _run(client.list_tables_typed())
    db = _run(client.get_database_typed(4))
    user = _run(client.get_user_typed(10))
    collection = _run(client.get_collection_typed("c1"))
    table = _run(client.get_table_typed(11))
    field = _run(client.get_field_typed(12))

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
    assert isinstance(cloud_migration, GenericOperationResponse)
    assert isinstance(latest_cloud_migration, GenericOperationResponse)
    assert isinstance(canceled_cloud_migration, GenericOperationResponse)
    assert isinstance(created_collection, Collection)
    assert created_collection.name == "New"
    assert isinstance(created_dashboard, Dashboard)
    assert created_dashboard.name == "Sales"
    assert isinstance(updated_collection, GenericOperationResponse)
    assert isinstance(deleted_collection, GenericOperationResponse)
    assert isinstance(comments, GenericOperationResponse)
    assert isinstance(comments_mentions, GenericOperationResponse)
    assert isinstance(created_comment, GenericOperationResponse)
    assert isinstance(updated_comment, GenericOperationResponse)
    assert isinstance(reaction_comment, GenericOperationResponse)
    assert isinstance(deleted_comment, GenericOperationResponse)
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
    assert isinstance(users, ListUsersResponse)
    assert isinstance(collections, ListCollectionsResponse)
    assert isinstance(tables, ListTablesResponse)
    assert db.name == "db4"
    assert isinstance(user, User)
    assert user.id == 10
    assert isinstance(collection, Collection)
    assert isinstance(table, Table)
    assert isinstance(field, MetabaseField)
