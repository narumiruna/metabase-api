from __future__ import annotations

from typing import ClassVar
from typing import cast

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_stale import EeStaleResponse
from metabaseapi.wire import QueryParamValue


class GetEeStaleIdRequest(EndpointRequest[EeStaleResponse]):
    stale_id: int | str
    before_date: str | None = None
    limit: int | None = None
    offset: int | None = None
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/stale/{stale_id}"
    response_model = EeStaleResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.params)
        params.update(
            {
                key: cast("QueryParamValue", value)
                for key, value in (
                    ("before_date", self.before_date),
                    ("limit", self.limit),
                    ("offset", self.offset),
                )
                if value is not None
            }
        )
        return params
