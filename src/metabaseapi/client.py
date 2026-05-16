from __future__ import annotations

from collections.abc import Mapping

import httpx

from .errors import MetabaseDecodeError
from .errors import MetabaseHTTPStatusError
from .errors import MetabaseNetworkError
from .metabase.models import Card
from .metabase.models import CreateDatabaseRequest
from .metabase.models import CurrentUserRequest
from .metabase.models import CurrentUserResponse
from .metabase.models import Dashboard
from .metabase.models import Database
from .metabase.models import GetCardRequest
from .metabase.models import GetDashboardRequest
from .metabase.models import ListDatabasesRequest
from .metabase.models import ListDatabasesResponse
from .models import JSONValue
from .models import get_request_model
from .models import get_response_model
from .settings import Settings


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
        params: Mapping[str, str | int | bool | float | None] | None = None,
        json_data: JSONValue | None = None,
    ) -> JSONValue | None:
        request_model_type = get_request_model(method, path)
        request_model = request_model_type(
            method=method,
            path=path,
            params=dict(params or {}),
            body=json_data,
        )

        url = self._request_url(request_model.path)
        headers = {"X-API-Key": self.api_key, "Accept": "application/json"}
        try:
            response = await self._client.request(
                request_model.method,
                url,
                params=request_model.params,
                json=request_model.body,
                headers=headers,
            )
        except httpx.TimeoutException as exc:
            raise MetabaseNetworkError("Metabase request timed out") from exc
        except httpx.NetworkError as exc:
            raise MetabaseNetworkError("Metabase network error") from exc

        payload = self._decode_response_payload(response)
        response_model_type = get_response_model(request_model.method, request_model.path)
        response_model = response_model_type(
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
        params: Mapping[str, str | int | bool | float | None] | None = None,
    ) -> JSONValue | None:
        return await self.request("GET", path, params=params)

    async def post(
        self,
        path: str,
        *,
        params: Mapping[str, str | int | bool | float | None] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("POST", path, params=params, json_data=body)

    async def put(
        self,
        path: str,
        *,
        params: Mapping[str, str | int | bool | float | None] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PUT", path, params=params, json_data=body)

    async def patch(
        self,
        path: str,
        *,
        params: Mapping[str, str | int | bool | float | None] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PATCH", path, params=params, json_data=body)

    async def delete(
        self,
        path: str,
        *,
        params: Mapping[str, str | int | bool | float | None] | None = None,
    ) -> JSONValue | None:
        return await self.request("DELETE", path, params=params)

    async def current_user(self) -> JSONValue | None:
        return await self.get("/api/user/current")

    async def list_databases(self) -> JSONValue | None:
        return await self.get("/api/database")

    async def get_dashboard(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/dashboard/{dashboard_id}")

    async def get_card(self, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}")

    async def current_user_typed(self) -> CurrentUserResponse:
        return await CurrentUserRequest().do(self)

    async def list_databases_typed(self) -> ListDatabasesResponse:
        return await ListDatabasesRequest().do(self)

    async def create_database_typed(
        self,
        *,
        name: str,
        engine: str,
        details: dict[str, object] | None = None,
    ) -> Database:
        request = CreateDatabaseRequest(name=name, engine=engine, details=details or {})
        return await request.do(self)

    async def get_card_typed(self, card_id: int | str) -> Card:
        return await GetCardRequest(card_id=card_id).do(self)

    async def get_dashboard_typed(self, dashboard_id: int | str) -> Dashboard:
        return await GetDashboardRequest(dashboard_id=dashboard_id).do(self)
