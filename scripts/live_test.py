from __future__ import annotations

import asyncio
import sys
from typing import cast

from metabaseapi.client import MetabaseClient
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.errors import MetabaseError
from metabaseapi.settings import Settings
from metabaseapi.wire import JSONValue

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
        current_user = await client.run(CurrentUserRequest())
        current_user_payload = cast(JSONValue, current_user.model_dump(mode="json", exclude_none=True))
        _print_payload_check("endpoint current-user", current_user_payload)

        fields = ", ".join(sorted(current_user.model_fields_set))
        identity_hint = any(
            value is not None
            for value in (
                current_user.common_name,
                current_user.email,
                current_user.id,
            )
        )
        print(f"typed CurrentUserRequest: ok; fields_set=[{fields}]; identity_hint={identity_hint}")

    print("live-test: ok")


def main() -> None:
    try:
        asyncio.run(run_live_test())
    except (MetabaseError, ValueError) as exc:
        print(f"live-test: failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
