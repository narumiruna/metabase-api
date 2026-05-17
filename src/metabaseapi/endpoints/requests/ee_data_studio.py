from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_data_studio import EeDataStudioTablePublishResponse


class PostEeDataStudioTablePublishTablesRequest(EndpointRequest[EeDataStudioTablePublishResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/data-studio/table/publish-tables"
    response_model = EeDataStudioTablePublishResponse


class PostEeDataStudioTableUnpublishTablesRequest(EndpointRequest[EeDataStudioTablePublishResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/data-studio/table/unpublish-tables"
    response_model = EeDataStudioTablePublishResponse
