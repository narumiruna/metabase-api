from __future__ import annotations

import asyncio
import os

import pytest

from metabaseapi.client import MetabaseClient
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.settings import Settings

pytestmark = pytest.mark.skipif(
    os.environ.get("METABASE_LIVE_TEST") != "1",
    reason="set METABASE_LIVE_TEST=1 to run live Metabase API checks",
)


async def _fetch_current_user() -> bool:
    settings = Settings()
    settings.requires_api_key()

    async with MetabaseClient.from_settings(settings) as client:
        current_user = await client.run(CurrentUserRequest())

    return any(
        value is not None
        for value in (
            current_user.common_name,
            current_user.email,
            current_user.id,
        )
    )


def test_live_current_user_endpoint_returns_identity() -> None:
    assert asyncio.run(_fetch_current_user())
