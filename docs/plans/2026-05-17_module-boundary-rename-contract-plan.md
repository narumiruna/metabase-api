# Module boundary rename + import contract plan (completed)

## Goal
- keep CLI command implementations in `metabaseapi.cli_commands` modules;
- remove migration shims from root command modules; keep command implementations in package modules;
- keep `metabaseapi.client.http` as the concrete client implementation and keep module slices explicit.

## Decisions
- Public CLI entrypoint remains `metabaseapi.cli` (package), discovered via `uv run metabaseapi --help`.
- Public client exports stay in `metabaseapi.client`.
- Internal canonical concrete client implementation is `metabaseapi.client.http`.
- Migration boundary:
  - `metabaseapi.client.raw`
  - `metabaseapi.client.typed`
  - `metabaseapi.cli_commands.actions_commands`
  - `metabaseapi.cli_commands.automagic_commands`
  - `metabaseapi.cli_commands.api_key_commands`
  - `metabaseapi.cli_commands.agent_commands`
  - `metabaseapi.cli_commands.alerts_comments_commands`
  - `metabaseapi.cli_commands.analytics_commands`
  - `metabaseapi.cli_commands.catalog_commands`
  - `metabaseapi.cli_commands.platform_bug_reporting_commands`
  - `metabaseapi.cli_commands.platform_cache_commands`
  - `metabaseapi.cli_commands.platform_channel_commands`
  - `metabaseapi.cli_commands.platform_cloud_migration_commands`
  - `metabaseapi.cli_commands.data_studio_commands`
  - `metabaseapi.cli_commands.dashboard_commands`

## Verification
- `metabaseapi.cli_commands_core`/`cli_commands_dashboard` 已刪除，不再保留 legacy imports.
- `tests/test_import_contracts.py` asserts public import paths and internal implementation aliases are aligned to the same objects.
- `UV_CACHE_DIR=/tmp/uv-cache uv run pytest tests/test_import_contracts.py -q` returns green.
- `UV_CACHE_DIR=/tmp/uv-cache uv run metabaseapi --help` succeeds and prints commands from package modules.
