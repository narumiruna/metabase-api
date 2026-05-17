from __future__ import annotations

import asyncio
import sys

from metabaseapi.client import MetabaseClient
from metabaseapi.errors import MetabaseError
from metabaseapi.models import JSONValue
from metabaseapi.settings import Settings

IDENTITY_KEYS = frozenset({"common_name", "email", "id"})


def _summarize_payload(payload: JSONValue | None) -> str:
    if payload is None:
        return "null"
    if isinstance(payload, dict):
        keys = ", ".join(sorted(payload))
        if not keys:
            return "empty object"
        return f"object keys=[{keys}]"
    if isinstance(payload, list):
        return f"list length={len(payload)}"
    return type(payload).__name__


def _has_identity_hint(payload: JSONValue | None) -> bool:
    if not isinstance(payload, dict):
        return False
    return any(payload.get(key) is not None for key in IDENTITY_KEYS)


def _print_payload_check(label: str, payload: JSONValue | None) -> None:
    identity_hint = _has_identity_hint(payload)
    print(f"{label}: ok; {_summarize_payload(payload)}; identity_hint={identity_hint}")


async def run_live_test() -> None:
    settings = Settings()
    settings.requires_api_key()

    async with MetabaseClient.from_settings(settings) as client:
        raw_current_user = await client.request("GET", "/api/user/current")
        _print_payload_check("raw GET /api/user/current", raw_current_user)

        current_user = await client.current_user()
        _print_payload_check("convenience current-user", current_user)

        typed_current_user = await client.current_user_typed()
        fields = ", ".join(sorted(typed_current_user.model_fields_set))
        identity_hint = any(
            value is not None
            for value in (
                typed_current_user.common_name,
                typed_current_user.email,
                typed_current_user.id,
            )
        )
        print(f"typed current_user_typed: ok; fields_set=[{fields}]; identity_hint={identity_hint}")

    print("live-test: ok")


def main() -> None:
    try:
        asyncio.run(run_live_test())
    except (MetabaseError, ValueError) as exc:
        print(f"live-test: failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
