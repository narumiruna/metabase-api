from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.embed_theme import DeleteEmbedThemeResponse
from metabaseapi.endpoints.responses.embed_theme import EmbedTheme
from metabaseapi.endpoints.responses.embed_theme import ListEmbedThemesResponse
from metabaseapi.endpoints.responses.embed_theme import SeedDefaultEmbedThemesResponse


class ListEmbedThemesRequest(EndpointRequest[ListEmbedThemesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed-theme"
    response_model = ListEmbedThemesResponse


class CreateEmbedThemeRequest(EndpointRequest[EmbedTheme]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/embed-theme"
    response_model = EmbedTheme


class SeedDefaultEmbedThemesRequest(EndpointRequest[SeedDefaultEmbedThemesResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/embed-theme/seed-defaults"
    response_model = SeedDefaultEmbedThemesResponse


class GetEmbedThemeRequest(EndpointRequest[EmbedTheme]):
    embed_theme_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/embed-theme/{embed_theme_id}"
    response_model = EmbedTheme


class UpdateEmbedThemeRequest(EndpointRequest[EmbedTheme]):
    embed_theme_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/embed-theme/{embed_theme_id}"
    response_model = EmbedTheme


class DeleteEmbedThemeRequest(EndpointRequest[DeleteEmbedThemeResponse]):
    embed_theme_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/embed-theme/{embed_theme_id}"
    response_model = DeleteEmbedThemeResponse


class CopyEmbedThemeRequest(EndpointRequest[EmbedTheme]):
    embed_theme_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/embed-theme/{embed_theme_id}/copy"
    response_model = EmbedTheme
