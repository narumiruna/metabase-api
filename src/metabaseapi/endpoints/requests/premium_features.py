from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.premium_features import PremiumFeaturesTokenStatusResponse
from metabaseapi.endpoints.responses.premium_features import RefreshPremiumFeaturesTokenResponse


class RefreshPremiumFeaturesTokenRequest(EndpointRequest[RefreshPremiumFeaturesTokenResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/premium-features/token/refresh"
    response_model = RefreshPremiumFeaturesTokenResponse


class GetPremiumFeaturesTokenStatusRequest(EndpointRequest[PremiumFeaturesTokenStatusResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/premium-features/token/status"
    response_model = PremiumFeaturesTokenStatusResponse
