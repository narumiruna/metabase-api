from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ldap import LdapSettingsResponse


class UpdateLdapSettingsRequest(EndpointRequest[LdapSettingsResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ldap/settings"
    response_model = LdapSettingsResponse
