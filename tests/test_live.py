from __future__ import annotations

import asyncio
import os

import pytest
from pydantic import BaseModel

from metabaseapi.client import MetabaseClient
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.requests.card import ListCardsRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTreeRequest
from metabaseapi.endpoints.requests.collection import ListCollectionsRequest
from metabaseapi.endpoints.requests.dashboard import ListDashboardsRequest
from metabaseapi.endpoints.requests.database import ListDatabasesRequest
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.endpoints.requests.user import ListUsersRequest
from metabaseapi.settings import Settings

pytestmark = pytest.mark.skipif(
    os.environ.get("METABASE_LIVE_TEST") != "1",
    reason="set METABASE_LIVE_TEST=1 to run live Metabase API checks",
)


async def _run_request[ResponseT: BaseModel](request_model: EndpointRequest[ResponseT]) -> ResponseT:
    settings = Settings()
    settings.requires_api_key()

    async with MetabaseClient.from_settings(settings) as client:
        return await client.run(request_model)


def test_live_current_user_endpoint_returns_identity() -> None:
    current_user = asyncio.run(_run_request(CurrentUserRequest()))

    assert any(
        value is not None
        for value in (
            current_user.common_name,
            current_user.email,
            current_user.id,
        )
    )


def test_live_database_list_endpoint_decodes() -> None:
    databases = asyncio.run(_run_request(ListDatabasesRequest()))

    assert isinstance(databases.databases, list)


def test_live_collection_list_endpoint_decodes() -> None:
    collections = asyncio.run(_run_request(ListCollectionsRequest()))

    assert isinstance(collections.collections, list)


def test_live_collection_tree_endpoint_decodes() -> None:
    tree = asyncio.run(_run_request(GetCollectionTreeRequest()))

    assert isinstance(tree.children, list)


def test_live_card_list_endpoint_decodes() -> None:
    cards = asyncio.run(_run_request(ListCardsRequest()))

    assert isinstance(cards.cards, list)


def test_live_dashboard_list_endpoint_decodes() -> None:
    dashboards = asyncio.run(_run_request(ListDashboardsRequest()))

    assert isinstance(dashboards.dashboards, list)


def test_live_user_list_endpoint_decodes() -> None:
    users = asyncio.run(_run_request(ListUsersRequest()))

    assert isinstance(users.users, list)
