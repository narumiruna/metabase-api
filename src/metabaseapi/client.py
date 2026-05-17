from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol
from typing import TypeVar

import httpx

from .errors import MetabaseDecodeError
from .errors import MetabaseHTTPStatusError
from .errors import MetabaseNetworkError
from .metabase import Card
from .metabase import Collection
from .metabase import CreateDatabaseRequest
from .metabase import CurrentUserRequest
from .metabase import CurrentUserResponse
from .metabase import Dashboard
from .metabase import Database
from .metabase import GetCardRequest
from .metabase import GetCollectionRequest
from .metabase import GetDashboardRequest
from .metabase import GetDatabaseRequest
from .metabase import GetFieldRequest
from .metabase import GetTableRequest
from .metabase import GetUserRequest
from .metabase import ListCardsRequest
from .metabase import ListCardsResponse
from .metabase import ListCollectionsRequest
from .metabase import ListCollectionsResponse
from .metabase import ListDashboardsRequest
from .metabase import ListDashboardsResponse
from .metabase import ListDatabasesRequest
from .metabase import ListDatabasesResponse
from .metabase import ListFieldsRequest
from .metabase import ListFieldsResponse
from .metabase import ListTablesRequest
from .metabase import ListTablesResponse
from .metabase import ListUsersRequest
from .metabase import ListUsersResponse
from .metabase import MetabaseField
from .metabase import Table
from .metabase import User
from .models import APIRequestModel
from .models import APIResponseModel
from .models import JSONValue
from .settings import Settings


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
        params: Mapping[str, str | int | bool | float | None] | None = None,
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
                    response = await self._client.delete(url, params=request_model.params, headers=headers)
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

    async def run[ResponseT](self, request_model: _ExecutableRequest[ResponseT]) -> ResponseT:
        return await request_model.do(self)

    async def current_user_typed(self) -> CurrentUserResponse:
        return await self.run(CurrentUserRequest())

    async def list_databases_typed(self) -> ListDatabasesResponse:
        return await self.run(ListDatabasesRequest())

    async def list_cards_typed(self) -> ListCardsResponse:
        return await self.run(ListCardsRequest())

    async def list_dashboards_typed(self) -> ListDashboardsResponse:
        return await self.run(ListDashboardsRequest())

    async def list_users_typed(self) -> ListUsersResponse:
        return await self.run(ListUsersRequest())

    async def list_collections_typed(self) -> ListCollectionsResponse:
        return await self.run(ListCollectionsRequest())

    async def list_tables_typed(self) -> ListTablesResponse:
        return await self.run(ListTablesRequest())

    async def list_fields_typed(self) -> ListFieldsResponse:
        return await self.run(ListFieldsRequest())

    async def create_database_typed(
        self,
        *,
        name: str,
        engine: str,
        details: dict[str, object] | None = None,
    ) -> Database:
        request = CreateDatabaseRequest(name=name, engine=engine, details=details or {})
        return await self.run(request)

    async def get_database_typed(self, database_id: int | str) -> Database:
        return await self.run(GetDatabaseRequest(database_id=database_id))

    async def get_card_typed(self, card_id: int | str) -> Card:
        return await self.run(GetCardRequest(card_id=card_id))

    async def get_dashboard_typed(self, dashboard_id: int | str) -> Dashboard:
        return await self.run(GetDashboardRequest(dashboard_id=dashboard_id))

    async def get_user_typed(self, user_id: int | str) -> User:
        return await self.run(GetUserRequest(user_id=user_id))

    async def get_collection_typed(self, collection_id: int | str) -> Collection:
        return await self.run(GetCollectionRequest(collection_id=collection_id))

    async def get_table_typed(self, table_id: int | str) -> Table:
        return await self.run(GetTableRequest(table_id=table_id))

    async def get_field_typed(self, field_id: int | str) -> MetabaseField:
        return await self.run(GetFieldRequest(field_id=field_id))
