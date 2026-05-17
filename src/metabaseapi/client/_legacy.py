from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol
from typing import TypeVar

import httpx

from metabaseapi.client.raw.activity import _MetabaseClientRawMixin as _MetabaseClientActivityRawMixin
from metabaseapi.client.raw.agent import _MetabaseClientRawMixin as _MetabaseClientAgentRawMixin
from metabaseapi.client.raw.alerts import _MetabaseClientRawMixin as _MetabaseClientAlertsRawMixin
from metabaseapi.client.raw.analytics import _MetabaseClientRawMixin as _MetabaseClientAnalyticsRawMixin
from metabaseapi.client.raw.api_key import _MetabaseClientRawMixin as _MetabaseClientApiKeyRawMixin
from metabaseapi.client.raw.automagic import _MetabaseClientRawMixin as _MetabaseClientAutomagicRawMixin
from metabaseapi.client.raw.bookmarks import _MetabaseClientRawMixin as _MetabaseClientBookmarksRawMixin
from metabaseapi.client.raw.bug_reporting import _MetabaseClientRawMixin as _MetabaseClientBugReportingRawMixin
from metabaseapi.client.raw.cache import _MetabaseClientRawMixin as _MetabaseClientCacheRawMixin
from metabaseapi.client.raw.cards import _MetabaseClientRawMixin as _MetabaseClientCardsRawMixin
from metabaseapi.client.raw.channels import _MetabaseClientRawMixin as _MetabaseClientChannelsRawMixin
from metabaseapi.client.raw.cloud import _MetabaseClientRawMixin as _MetabaseClientCloudRawMixin
from metabaseapi.client.raw.collections import _MetabaseClientRawMixin as _MetabaseClientCollectionsRawMixin
from metabaseapi.client.raw.comments import _MetabaseClientRawMixin as _MetabaseClientCommentsRawMixin
from metabaseapi.client.raw.dashboards import _MetabaseClientRawMixin as _MetabaseClientDashboardsRawMixin
from metabaseapi.client.raw.databases import _MetabaseClientRawMixin as _MetabaseClientDatabasesRawMixin
from metabaseapi.client.raw.misc import _MetabaseClientRawMixin as _MetabaseClientMiscRawMixin
from metabaseapi.client.raw.tables import _MetabaseClientRawMixin as _MetabaseClientTablesRawMixin
from metabaseapi.client.raw.users import _MetabaseClientRawMixin as _MetabaseClientUsersRawMixin
from metabaseapi.client.typed.activity import _MetabaseClientTypedMixin as _MetabaseClientActivityTypedMixin
from metabaseapi.client.typed.agent import _MetabaseClientTypedMixin as _MetabaseClientAgentTypedMixin
from metabaseapi.client.typed.alerts import _MetabaseClientTypedMixin as _MetabaseClientAlertsTypedMixin
from metabaseapi.client.typed.analytics import _MetabaseClientTypedMixin as _MetabaseClientAnalyticsTypedMixin
from metabaseapi.client.typed.api_key import _MetabaseClientTypedMixin as _MetabaseClientApiKeyTypedMixin
from metabaseapi.client.typed.automagic import _MetabaseClientTypedMixin as _MetabaseClientAutomagicTypedMixin
from metabaseapi.client.typed.bookmarks import _MetabaseClientTypedMixin as _MetabaseClientBookmarksTypedMixin
from metabaseapi.client.typed.bug_reporting import _MetabaseClientTypedMixin as _MetabaseClientBugReportingTypedMixin
from metabaseapi.client.typed.cache import _MetabaseClientTypedMixin as _MetabaseClientCacheTypedMixin
from metabaseapi.client.typed.cards import _MetabaseClientTypedMixin as _MetabaseClientCardsTypedMixin
from metabaseapi.client.typed.channels import _MetabaseClientTypedMixin as _MetabaseClientChannelsTypedMixin
from metabaseapi.client.typed.cloud import _MetabaseClientTypedMixin as _MetabaseClientCloudTypedMixin
from metabaseapi.client.typed.collections import _MetabaseClientTypedMixin as _MetabaseClientCollectionsTypedMixin
from metabaseapi.client.typed.comments import _MetabaseClientTypedMixin as _MetabaseClientCommentsTypedMixin
from metabaseapi.client.typed.dashboards import _MetabaseClientTypedMixin as _MetabaseClientDashboardsTypedMixin
from metabaseapi.client.typed.databases import _MetabaseClientTypedMixin as _MetabaseClientDatabasesTypedMixin
from metabaseapi.client.typed.misc import _MetabaseClientTypedMixin as _MetabaseClientMiscTypedMixin
from metabaseapi.client.typed.tables import _MetabaseClientTypedMixin as _MetabaseClientTablesTypedMixin
from metabaseapi.client.typed.users import _MetabaseClientTypedMixin as _MetabaseClientUsersTypedMixin
from metabaseapi.errors import MetabaseDecodeError
from metabaseapi.errors import MetabaseHTTPStatusError
from metabaseapi.errors import MetabaseNetworkError
from metabaseapi.models import APIRequestModel
from metabaseapi.models import APIResponseModel
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue
from metabaseapi.settings import Settings


class _MetabaseClientRawMixin(
    _MetabaseClientUsersRawMixin,
    _MetabaseClientAnalyticsRawMixin,
    _MetabaseClientAlertsRawMixin,
    _MetabaseClientApiKeyRawMixin,
    _MetabaseClientAgentRawMixin,
    _MetabaseClientActivityRawMixin,
    _MetabaseClientBookmarksRawMixin,
    _MetabaseClientCacheRawMixin,
    _MetabaseClientCollectionsRawMixin,
    _MetabaseClientChannelsRawMixin,
    _MetabaseClientCloudRawMixin,
    _MetabaseClientCardsRawMixin,
    _MetabaseClientDatabasesRawMixin,
    _MetabaseClientAutomagicRawMixin,
    _MetabaseClientDashboardsRawMixin,
    _MetabaseClientCommentsRawMixin,
    _MetabaseClientBugReportingRawMixin,
    _MetabaseClientMiscRawMixin,
    _MetabaseClientTablesRawMixin,
):
    """Resource-scoped raw mixin."""


class _MetabaseClientTypedMixin(
    _MetabaseClientRawMixin,
    _MetabaseClientUsersTypedMixin,
    _MetabaseClientAnalyticsTypedMixin,
    _MetabaseClientAlertsTypedMixin,
    _MetabaseClientApiKeyTypedMixin,
    _MetabaseClientAgentTypedMixin,
    _MetabaseClientBookmarksTypedMixin,
    _MetabaseClientCacheTypedMixin,
    _MetabaseClientCollectionsTypedMixin,
    _MetabaseClientChannelsTypedMixin,
    _MetabaseClientCloudTypedMixin,
    _MetabaseClientCardsTypedMixin,
    _MetabaseClientDatabasesTypedMixin,
    _MetabaseClientAutomagicTypedMixin,
    _MetabaseClientDashboardsTypedMixin,
    _MetabaseClientCommentsTypedMixin,
    _MetabaseClientBugReportingTypedMixin,
    _MetabaseClientMiscTypedMixin,
    _MetabaseClientTablesTypedMixin,
    _MetabaseClientActivityTypedMixin,
):
    """Resource-scoped typed mixin."""


class _ExecutableRequest[ResponseT](Protocol):
    async def do(self, client: MetabaseClient) -> ResponseT: ...


ResponseT = TypeVar("ResponseT")


class MetabaseClient(_MetabaseClientTypedMixin):
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
        params: Mapping[str, QueryParamValue] | None = None,
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
                    if request_model.body is None:
                        response = await self._client.delete(url, params=request_model.params, headers=headers)
                    else:
                        # httpx.AsyncClient.delete() has no JSON-body parameter, but Metabase documents
                        # DELETE /api/cache with a JSON body.
                        response = await self._client.request(
                            "DELETE",
                            url,
                            params=request_model.params,
                            json=request_model.body,
                            headers=headers,
                        )
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
        params: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.request("GET", path, params=params)

    async def post(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("POST", path, params=params, json_data=body)

    async def put(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PUT", path, params=params, json_data=body)

    async def patch(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PATCH", path, params=params, json_data=body)

    async def delete(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("DELETE", path, params=params, json_data=body)

    async def run[ResponseT](self, request_model: _ExecutableRequest[ResponseT]) -> ResponseT:
        return await request_model.do(self)
