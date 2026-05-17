from __future__ import annotations

from typing import ClassVar
from typing import Literal

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.revision import RevertRevisionResponse
from metabaseapi.endpoints.responses.revision import RevisionsResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue

RevisionEntity = Literal["card", "dashboard"]


class GetRevisionsRequest(EndpointRequest[RevisionsResponse]):
    entity: RevisionEntity
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/revision"
    response_model = RevisionsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return {"entity": self.entity, "id": self.id}


class RevertRevisionRequest(EndpointRequest[RevertRevisionResponse]):
    entity: RevisionEntity
    id: int | str
    revision_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/revision/revert"
    response_model = RevertRevisionResponse

    def request_body(self) -> JSONValue:
        return {"entity": self.entity, "id": self.id, "revision_id": self.revision_id}


class GetEntityRevisionsRequest(EndpointRequest[RevisionsResponse]):
    entity: str
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/revision/{entity}/{id}"
    response_model = RevisionsResponse
