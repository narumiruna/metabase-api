from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.collection import CollectionGraphResponse


class GetCollectionGraphRequest(EndpointRequest[CollectionGraphResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/graph"
    response_model = CollectionGraphResponse


class PutCollectionGraphRequest(EndpointRequest[CollectionGraphResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/collection/graph"
    response_model = CollectionGraphResponse
