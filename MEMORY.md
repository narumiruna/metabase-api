# MEMORY.md

## GOTCHA
- Symptom: `uv run ...` can panic in sandbox with `Attempted to create a NULL object`. Cause: macOS system configuration access is unavailable in the sandbox. Fix: retry the same `UV_CACHE_DIR=/tmp/uv-cache uv run ...` command outside the sandbox.

## TASTE
- Keep public package facades small: `metabaseapi.endpoints` exposes submodules only, and request classes live in `metabaseapi.endpoints.requests.<domain>`.
- Prefer endpoint response models in `metabaseapi.endpoints.responses.<domain>` modules; avoid re-exporting response classes from `metabaseapi.endpoints.responses`.
