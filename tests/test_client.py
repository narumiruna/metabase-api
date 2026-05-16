from __future__ import annotations

import asyncio
import json
from collections.abc import Coroutine

import httpx
import pytest

from metabaseapi.client import MetabaseClient
from metabaseapi.errors import MetabaseDecodeError
from metabaseapi.errors import MetabaseHTTPStatusError
from metabaseapi.errors import MetabaseNetworkError


def _run(coro: Coroutine[object, object, object]) -> object:
    return asyncio.run(coro)


def test_request_includes_api_key_and_query_parameters() -> None:
    captured: dict[str, str | dict[str, str] | None] = {}

    async def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        captured["method"] = request.method
        captured["params"] = dict(request.url.params)
        captured["x-api-key"] = request.headers.get("X-API-Key")
        captured["accept"] = request.headers.get("Accept")
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000/",
        api_key="abc",
        timeout_seconds=3.0,
        verify_ssl=False,
        client=httpx.AsyncClient(transport=transport, timeout=3.0, verify=False),
    )

    result = _run(client.get("/api/user/current", params={"a": "1"}))

    request_url = captured["url"]
    assert isinstance(request_url, str)
    assert request_url.startswith("http://localhost:3000/api/user/current")
    assert captured["method"] == "GET"
    assert captured["params"] == {"a": "1"}
    assert captured["x-api-key"] == "abc"
    assert captured["accept"] == "application/json"
    assert result == {"ok": True}


def test_post_sends_json_body() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        payload = json.loads(request.content.decode())
        assert payload == {"foo": "bar"}
        return httpx.Response(200, json={"received": payload})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    result = _run(client.post("/api/session", body={"foo": "bar"}))
    assert result == {"received": {"foo": "bar"}}


def test_convenience_paths() -> None:
    captured: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request.url.path)
        return httpx.Response(200, json={"path": request.url.path})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="https://metabase.local",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    result1 = _run(client.get_card(12))
    result2 = _run(client.get_dashboard(99))

    assert result1 == {"path": "/api/card/12"}
    assert result2 == {"path": "/api/dashboard/99"}
    assert captured == ["/api/card/12", "/api/dashboard/99"]


def test_http_error_is_mapped_to_client_error() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"message": "not found"})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    with pytest.raises(MetabaseHTTPStatusError) as exc:
        _run(client.get("/api/card/1"))

    assert exc.value.status_code == 404


def test_decode_error_for_invalid_json() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"not-json", headers={"content-type": "application/json"})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    with pytest.raises(MetabaseDecodeError):
        _run(client.get("/api/card/1"))


def test_non_json_payload_is_wrapped_as_json_text() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"ok", headers={"content-type": "text/plain"})

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    result = _run(client.get("/api/health"))
    assert result == {"content_type": "text/plain", "text": "ok"}


def test_network_error_is_mapped() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.TimeoutException("timeout")

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    with pytest.raises(MetabaseNetworkError):
        _run(client.get("/api/card/1"))
