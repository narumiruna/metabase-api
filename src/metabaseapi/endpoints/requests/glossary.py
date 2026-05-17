from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.glossary import CreateGlossaryEntryResponse
from metabaseapi.endpoints.responses.glossary import DeleteGlossaryEntryResponse
from metabaseapi.endpoints.responses.glossary import GlossaryEntriesResponse
from metabaseapi.endpoints.responses.glossary import UpdateGlossaryEntryResponse
from metabaseapi.wire import QueryParamValue


class GetGlossaryRequest(EndpointRequest[GlossaryEntriesResponse]):
    search: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/glossary"
    response_model = GlossaryEntriesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.search is None:
            return {}
        return {"search": self.search}


class CreateGlossaryEntryRequest(EndpointRequest[CreateGlossaryEntryResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/glossary"
    response_model = CreateGlossaryEntryResponse


class UpdateGlossaryEntryRequest(EndpointRequest[UpdateGlossaryEntryResponse]):
    id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/glossary/{id}"
    response_model = UpdateGlossaryEntryResponse


class DeleteGlossaryEntryRequest(EndpointRequest[DeleteGlossaryEntryResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/glossary/{id}"
    response_model = DeleteGlossaryEntryResponse
