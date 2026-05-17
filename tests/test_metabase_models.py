from __future__ import annotations

import asyncio
from collections.abc import Coroutine
from datetime import UTC
from datetime import datetime

import httpx

from metabaseapi.client import MetabaseClient
from metabaseapi.metabase import Action
from metabaseapi.metabase import ActionExecutionResponse
from metabaseapi.metabase import Card
from metabaseapi.metabase import Collection
from metabaseapi.metabase import CreateActionPublicLinkRequest
from metabaseapi.metabase import CreateActionRequest
from metabaseapi.metabase import CreateCardRequest
from metabaseapi.metabase import CreateDatabaseRequest
from metabaseapi.metabase import CurrentUserRequest
from metabaseapi.metabase import CurrentUserResponse
from metabaseapi.metabase import Dashboard
from metabaseapi.metabase import Database
from metabaseapi.metabase import DeleteActionPublicLinkRequest
from metabaseapi.metabase import DeleteActionRequest
from metabaseapi.metabase import ExecuteActionRequest
from metabaseapi.metabase import GetActionExecuteRequest
from metabaseapi.metabase import GetActionRequest
from metabaseapi.metabase import GetCardRequest
from metabaseapi.metabase import GetCollectionRequest
from metabaseapi.metabase import GetDashboardRequest
from metabaseapi.metabase import GetDatabaseRequest
from metabaseapi.metabase import GetFieldRequest
from metabaseapi.metabase import GetTableRequest
from metabaseapi.metabase import GetUserRequest
from metabaseapi.metabase import ListActionsRequest
from metabaseapi.metabase import ListActionsResponse
from metabaseapi.metabase import ListCardsRequest
from metabaseapi.metabase import ListCardsResponse
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
from metabaseapi.metabase import Table
from metabaseapi.metabase import UpdateActionRequest
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
    ]

    for request_model, response_type, expected_call in cases:
        stub = _StubClient({"id": 5, "name": "action"})
        response = request_model.do_sync(stub)

        assert isinstance(response, response_type)
        assert stub.calls == [expected_call]


def test_list_requests_use_expected_paths() -> None:
    for request_model, response_type, expected_path in [
        (ListCardsRequest(), ListCardsResponse, "/api/card"),
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
        ("GET", "/api/user"): {"data": [{"id": 4, "email": "user@example.com", "first_name": "Ada"}]},
        ("GET", "/api/collection"): {"data": [{"id": 7, "name": "collection"}]},
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
    cards = _run(client.list_cards_typed())
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
    assert isinstance(cards, ListCardsResponse)
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
