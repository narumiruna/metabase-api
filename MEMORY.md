# MEMORY.md

## GOTCHA
- Current refactor contract intentionally breaks legacy imports: use `metabaseapi.cli.commands`, `metabaseapi.endpoints`, and `metabaseapi.wire`; do not restore `metabaseapi.cli_commands`, `metabaseapi.metabase`, or `metabaseapi.models`.
- `metabaseapi.client.typed` was removed as a shallow pass-through seam; typed calls should use `MetabaseClient.run(...)` with `metabaseapi.endpoints.requests.<domain>` request models.
- Symptom: `uv run ...` can panic in sandbox with `Attempted to create a NULL object`. Cause: macOS system configuration access is unavailable in the sandbox. Fix: retry the same `UV_CACHE_DIR=/tmp/uv-cache uv run ...` command outside the sandbox.

## TASTE
- Keep public package facades small: `metabaseapi.endpoints` exposes submodules only, and request classes live in `metabaseapi.endpoints.requests.<domain>`.
- Prefer endpoint response models in `metabaseapi.endpoints.responses.<domain>` modules; avoid re-exporting response classes from `metabaseapi.endpoints.responses`.
