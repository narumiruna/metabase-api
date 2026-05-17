from __future__ import annotations

from metabaseapi.client._legacy import _MetabaseClientRawMixin as _MetabaseClientLegacyRawMixin


class _MetabaseClientRawMixin(_MetabaseClientLegacyRawMixin):
    """Resource-scoped raw mixin façade."""


__all__ = ["_MetabaseClientRawMixin"]
