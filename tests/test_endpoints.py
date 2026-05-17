from __future__ import annotations

import asyncio
from collections.abc import Coroutine

import httpx
import pytest
from pydantic import ValidationError

from metabaseapi.client import MetabaseClient
from metabaseapi.models import APIRequestModel
from metabaseapi.models import APIResponseModel
from metabaseapi.models import JSONValue


def _run(coro: Coroutine[object, object, JSONValue | None]) -> JSONValue | None:
    return asyncio.run(coro)


def test_api_request_model_normalizes_supported_methods() -> None:
    request = APIRequestModel(method="post", path="/api/database", body={"name": "analytics"})

    assert request.method == "POST"
    assert request.path == "/api/database"
    assert request.body == {"name": "analytics"}


def test_api_request_model_rejects_unknown_methods() -> None:
    with pytest.raises(ValidationError, match="method must be DELETE, GET, PATCH, POST, or PUT"):
        APIRequestModel(method="OPTIONS", path="/api/card/1")


def test_api_response_model_wraps_status_payload_and_content_type() -> None:
    response = APIResponseModel(status_code=200, payload={"ok": True}, content_type="application/json")

    assert response.status_code == 200
    assert response.payload == {"ok": True}
    assert response.content_type == "application/json"


def test_client_request_dispatches_handwritten_http_methods() -> None:
    captured: list[tuple[str, str, dict[str, str], object | None]] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        body: object | None = None
        if request.content:
            body = request.content.decode()
        captured.append((request.method, request.url.path, dict(request.url.params), body))
        return httpx.Response(200, json={"method": request.method, "path": request.url.path})

    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=httpx.MockTransport(handler)),
    )

    get_result = _run(client.request("GET", "/api/user/current", params={"a": "1"}))
    post_result = _run(client.request("POST", "/api/database", json_data={"name": "analytics"}))
    put_result = _run(client.put("/api/card/1", body={"name": "updated"}))
    patch_result = _run(client.patch("/api/card/1", body={"archived": True}))
    delete_result = _run(client.delete("/api/card/1"))

    assert get_result == {"method": "GET", "path": "/api/user/current"}
    assert post_result == {"method": "POST", "path": "/api/database"}
    assert put_result == {"method": "PUT", "path": "/api/card/1"}
    assert patch_result == {"method": "PATCH", "path": "/api/card/1"}
    assert delete_result == {"method": "DELETE", "path": "/api/card/1"}
    assert captured[0] == ("GET", "/api/user/current", {"a": "1"}, None)
    assert captured[1][0:3] == ("POST", "/api/database", {})
    assert captured[1][3] == '{"name":"analytics"}'
    assert captured[2][0:3] == ("PUT", "/api/card/1", {})
    assert captured[2][3] == '{"name":"updated"}'
    assert captured[3][0:3] == ("PATCH", "/api/card/1", {})
    assert captured[3][3] == '{"archived":true}'
    assert captured[4] == ("DELETE", "/api/card/1", {}, None)
