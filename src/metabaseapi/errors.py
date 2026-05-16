from __future__ import annotations


class MetabaseError(RuntimeError):
    """Base error for Metabase API client failures."""


class MetabaseNetworkError(MetabaseError):
    """Raised for transport and timeout problems."""


class MetabaseHTTPStatusError(MetabaseError):
    """Raised when Metabase returns a non-successful HTTP status."""

    def __init__(self, status_code: int, body: object | None = None) -> None:
        self.status_code = status_code
        self.body = body
        super().__init__(f"Metabase API returned HTTP {status_code}: {body!r}")


class MetabaseDecodeError(MetabaseError):
    """Raised when a response claims JSON but cannot be decoded."""
