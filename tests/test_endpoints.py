from __future__ import annotations

import asyncio
import json
import re
from collections.abc import Coroutine
from collections.abc import Iterable
from pathlib import Path

import httpx
import pytest

from metabaseapi.client import MetabaseClient
from metabaseapi.models import _ENDPOINT_MODELS
from metabaseapi.models import _ENDPOINT_PATHS_BY_METHOD
from metabaseapi.models import APIRequestModel
from metabaseapi.models import APIResponseModel
from metabaseapi.models import JSONValue
from metabaseapi.models import get_request_model
from metabaseapi.models import get_response_model

_PATH_PARAM_PATTERN = re.compile(r"\{[^/{}]+\}")
_SUPPORTED_METHODS = {"delete", "get", "post", "put", "patch"}


def _run(coro: Coroutine[object, object, JSONValue | None]) -> JSONValue | None:
    return asyncio.run(coro)


def _sample_path(path: str) -> str:
    return _PATH_PARAM_PATTERN.sub("1", path)


def _load_api_endpoints() -> list[tuple[str, str]]:
    spec_path = Path(__file__).parent / "fixtures" / "api.json"
    if not spec_path.exists():
        pytest.skip("API spec fixture is missing", allow_module_level=True)

    data = json.loads(spec_path.read_text(encoding="utf-8"))
    endpoint_pairs: list[tuple[str, str]] = []
    for raw_path, operations in data["paths"].items():
        for method in operations:
            if method not in _SUPPORTED_METHODS:
                continue
            endpoint_pairs.append((method.upper(), raw_path))
    return endpoint_pairs


def _endpoint_ids(cases: Iterable[tuple[str, str]]) -> Iterable[str]:
    for method, path in cases:
        yield f"{method} {path}"


_ENDPOINT_CASES = _load_api_endpoints()


def test_openapi_endpoint_model_count_matches_fixture() -> None:
    assert len(_ENDPOINT_CASES) == len(_ENDPOINT_MODELS)
    for method, paths in _ENDPOINT_PATHS_BY_METHOD.items():
        assert len(paths) == len([key for key in _ENDPOINT_MODELS if key[0] == method])


@pytest.mark.parametrize(
    "method,path",
    _ENDPOINT_CASES,
    ids=_endpoint_ids(_ENDPOINT_CASES),
)
def test_all_openapi_endpoints_have_pydantic_models(method: str, path: str) -> None:
    request_model = get_request_model(method, path)
    response_model = get_response_model(method, path)

    assert issubclass(request_model, APIRequestModel)
    assert issubclass(response_model, APIResponseModel)
    assert request_model.endpoint_path == path
    assert response_model.endpoint_path == path
    assert request_model.endpoint_method == method
    assert response_model.endpoint_method == method

    parsed_request = request_model(method=method, path=path)
    assert parsed_request.path == path
    assert parsed_request.method == method
    assert parsed_request.endpoint_path == path
    assert parsed_request.endpoint_method == method


@pytest.mark.parametrize(
    "method,path",
    _ENDPOINT_CASES,
    ids=_endpoint_ids(_ENDPOINT_CASES),
)
def test_all_openapi_endpoints_are_callable(method: str, path: str) -> None:
    captured: dict[str, str] = {}

    async def handler(request: httpx.Request) -> httpx.Response:
        captured["method"] = request.method
        captured["path"] = request.url.path
        return httpx.Response(200, json={"ok": True})

    tested_path = _sample_path(path)
    request_model = get_request_model(method, path)
    response_model = get_response_model(method, path)

    assert issubclass(request_model, APIRequestModel)
    assert issubclass(response_model, APIResponseModel)
    assert request_model.endpoint_path == path
    assert response_model.endpoint_path == path

    parsed_request = request_model(method=method, path=tested_path)
    assert parsed_request.path == tested_path
    assert parsed_request.method == method

    transport = httpx.MockTransport(handler)
    client = MetabaseClient(
        base_url="http://localhost:3000",
        api_key="abc",
        client=httpx.AsyncClient(transport=transport),
    )

    result = _run(client.request(method, tested_path))

    assert result == {"ok": True}
    assert captured["method"] == method
    assert captured["path"] == tested_path

    typed_response = response_model(
        status_code=200,
        payload=result or {},
        content_type="application/json",
    )
    assert typed_response.status_code == 200
    assert typed_response.payload == {"ok": True}
