from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final
from typing import Literal
from typing import Protocol
from typing import TypeVar

import httpx

from metabaseapi.client.raw.actions import _MetabaseClientRawMixin as _MetabaseClientActionsRawMixin
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
from metabaseapi.client.raw.data_studio import _MetabaseClientRawMixin as _MetabaseClientDataStudioRawMixin
from metabaseapi.client.raw.databases import _MetabaseClientRawMixin as _MetabaseClientDatabasesRawMixin
from metabaseapi.client.raw.tables import _MetabaseClientRawMixin as _MetabaseClientTablesRawMixin
from metabaseapi.client.raw.users import _MetabaseClientRawMixin as _MetabaseClientUsersRawMixin
from metabaseapi.client.typed.actions import _MetabaseClientTypedMixin as _MetabaseClientActionsTypedMixin
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
from metabaseapi.client.typed.data_studio import _MetabaseClientTypedMixin as _MetabaseClientDataStudioTypedMixin
from metabaseapi.client.typed.databases import _MetabaseClientTypedMixin as _MetabaseClientDatabasesTypedMixin
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

__all__ = [
    "CLIENT_MIXIN_LAYERS",
    "CLIENT_MIXIN_SEAM_REGISTRY",
    "CLIENT_RAW_MIXINS",
    "CLIENT_RAW_MIXIN_GROUPS",
    "CLIENT_TYPED_MIXINS",
    "CLIENT_TYPED_MIXIN_GROUPS",
    "MetabaseClient",
    "_MetabaseClientRawMixin",
    "_MetabaseClientTypedMixin",
    "client_mixin_group_names",
    "client_mixin_layers",
    "client_mixins_for_group",
    "client_mixins_in_layer",
]


CLIENT_MIXIN_SEAM_REGISTRY: Mapping[str, tuple[type, type]] = MappingProxyType(
    {
        "actions": (_MetabaseClientActionsRawMixin, _MetabaseClientActionsTypedMixin),
        "users": (_MetabaseClientUsersRawMixin, _MetabaseClientUsersTypedMixin),
        "analytics": (_MetabaseClientAnalyticsRawMixin, _MetabaseClientAnalyticsTypedMixin),
        "alerts": (_MetabaseClientAlertsRawMixin, _MetabaseClientAlertsTypedMixin),
        "api_key": (_MetabaseClientApiKeyRawMixin, _MetabaseClientApiKeyTypedMixin),
        "agent": (_MetabaseClientAgentRawMixin, _MetabaseClientAgentTypedMixin),
        "activity": (_MetabaseClientActivityRawMixin, _MetabaseClientActivityTypedMixin),
        "bookmarks": (_MetabaseClientBookmarksRawMixin, _MetabaseClientBookmarksTypedMixin),
        "cache": (_MetabaseClientCacheRawMixin, _MetabaseClientCacheTypedMixin),
        "collections": (_MetabaseClientCollectionsRawMixin, _MetabaseClientCollectionsTypedMixin),
        "channels": (_MetabaseClientChannelsRawMixin, _MetabaseClientChannelsTypedMixin),
        "cloud": (_MetabaseClientCloudRawMixin, _MetabaseClientCloudTypedMixin),
        "cards": (_MetabaseClientCardsRawMixin, _MetabaseClientCardsTypedMixin),
        "databases": (_MetabaseClientDatabasesRawMixin, _MetabaseClientDatabasesTypedMixin),
        "automagic": (_MetabaseClientAutomagicRawMixin, _MetabaseClientAutomagicTypedMixin),
        "dashboards": (_MetabaseClientDashboardsRawMixin, _MetabaseClientDashboardsTypedMixin),
        "comments": (_MetabaseClientCommentsRawMixin, _MetabaseClientCommentsTypedMixin),
        "bug_reporting": (_MetabaseClientBugReportingRawMixin, _MetabaseClientBugReportingTypedMixin),
        "data_studio": (_MetabaseClientDataStudioRawMixin, _MetabaseClientDataStudioTypedMixin),
        "tables": (_MetabaseClientTablesRawMixin, _MetabaseClientTablesTypedMixin),
    }
)

ClientMixinLayer = Literal["raw", "typed"]
CLIENT_MIXIN_LAYERS: Final[tuple[ClientMixinLayer, ClientMixinLayer]] = ("raw", "typed")


def _build_client_mixin_layer_groups(layer: ClientMixinLayer) -> Mapping[str, tuple[type, ...]]:
    """Build raw or typed mixin groups from the seam registry."""
    index = 0 if layer == "raw" else 1
    return MappingProxyType({group_name: (mixins[index],) for group_name, mixins in CLIENT_MIXIN_SEAM_REGISTRY.items()})


CLIENT_RAW_MIXIN_GROUPS: Mapping[str, tuple[type, ...]] = _build_client_mixin_layer_groups("raw")
CLIENT_TYPED_MIXIN_GROUPS: Mapping[str, tuple[type, ...]] = _build_client_mixin_layer_groups("typed")


def _flatten_mixins(groups: Mapping[str, tuple[type, ...]]) -> tuple[type, ...]:
    return tuple(mixin for module_mixins in groups.values() for mixin in module_mixins)


CLIENT_RAW_MIXINS = _flatten_mixins(CLIENT_RAW_MIXIN_GROUPS)
CLIENT_TYPED_MIXINS = _flatten_mixins(CLIENT_TYPED_MIXIN_GROUPS)


def client_mixin_layers() -> tuple[ClientMixinLayer, ...]:
    """Return available client mixin layers."""
    return CLIENT_MIXIN_LAYERS


def _client_mixin_groups(layer: ClientMixinLayer) -> Mapping[str, tuple[type, ...]]:
    if layer == "raw":
        return CLIENT_RAW_MIXIN_GROUPS
    if layer == "typed":
        return CLIENT_TYPED_MIXIN_GROUPS
    raise ValueError(f"unsupported client layer: {layer}")


def client_mixin_group_names(layer: ClientMixinLayer = "raw") -> tuple[str, ...]:
    """Return registered client mixin group names."""
    return tuple(_client_mixin_groups(layer))


def client_mixins_in_layer(layer: ClientMixinLayer = "raw") -> tuple[type, ...]:
    """Return flattened mixins for a client layer."""
    return _flatten_mixins(_client_mixin_groups(layer))


def client_mixins_for_group(
    group_name: str,
    *,
    layer: ClientMixinLayer = "raw",
) -> tuple[type, ...]:
    """Return mixins assigned to a client mixin group."""
    groups = _client_mixin_groups(layer)
    return groups[group_name]


class _MetabaseClientRawMixin(
    _MetabaseClientActionsRawMixin,
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
    _MetabaseClientDataStudioRawMixin,
    _MetabaseClientTablesRawMixin,
):
    """Resource-scoped raw mixin."""


class _MetabaseClientTypedMixin(
    _MetabaseClientRawMixin,
    _MetabaseClientActionsTypedMixin,
    _MetabaseClientUsersTypedMixin,
    _MetabaseClientAnalyticsTypedMixin,
    _MetabaseClientAlertsTypedMixin,
    _MetabaseClientApiKeyTypedMixin,
    _MetabaseClientAgentTypedMixin,
    _MetabaseClientActivityTypedMixin,
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
    _MetabaseClientDataStudioTypedMixin,
    _MetabaseClientTablesTypedMixin,
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
