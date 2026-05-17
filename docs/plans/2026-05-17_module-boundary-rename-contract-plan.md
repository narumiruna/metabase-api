# Module boundary rename + import contract plan (completed)

## Goal
- keep CLI command implementations in `metabaseapi.cli_commands` modules;
- keep command root modules (`cli_commands_core.py`, `cli_commands_dashboard.py`) as thin migration shims;
- keep `metabaseapi.client.http` as the concrete client implementation and keep module slices explicit.

## Decisions
- Public CLI entrypoint remains `metabaseapi.cli` (package), discovered via `uv run metabaseapi --help`.
- Public client exports stay in `metabaseapi.client`.
- Internal canonical concrete client implementation is `metabaseapi.client.http`.
- Migration module layer:
  - `metabaseapi.client.raw`
  - `metabaseapi.client.typed`
  - `metabaseapi.cli_commands_core`
  - `metabaseapi.cli_commands_dashboard`

## Verification
- `metabaseapi.cli_commands_core`/`cli_commands_dashboard` contain only legacy imports.
- `tests/test_import_contracts.py` asserts public import paths and internal implementation aliases are aligned to the same objects.
- `UV_CACHE_DIR=/tmp/uv-cache uv run pytest tests/test_import_contracts.py -q` returns green.
- `UV_CACHE_DIR=/tmp/uv-cache uv run metabaseapi --help` succeeds and prints commands from package modules.
