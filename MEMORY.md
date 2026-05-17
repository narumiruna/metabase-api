# MEMORY.md

## GOTCHA
- Current refactor contract intentionally breaks legacy imports: use `metabaseapi.cli.commands`, `metabaseapi.endpoints`, and `metabaseapi.wire`; do not restore `metabaseapi.cli_commands`, `metabaseapi.metabase`, or `metabaseapi.models`.

## TASTE
- Keep public package facades small: `metabaseapi.endpoints` exposes submodules only, and request classes live in `metabaseapi.endpoints.requests.<domain>`.
