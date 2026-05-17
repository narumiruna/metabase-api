# Context

## package/module structure
- `metabaseapi.cli` owns Typer app lifecycle (app, global options, client wiring, error adapters).
- `metabaseapi.cli_commands` is the command registration package; each module inside owns command implementations for related API surface.
- `metabaseapi.client` exports canonical client symbols and re-exports from `metabaseapi.client.http`.
- `metabaseapi.client.http` is the canonical concrete implementation, owning async HTTP transport and mixin assembly.
- `metabaseapi.client.raw` 和 `metabaseapi.client.typed` 保留為 domain-sliced mixin 構件，供 `client/http.py` 組裝；Data Studio client methods live in `data_studio.py`, not a generic `misc.py`.
- `metabaseapi.client.http` 同時提供分群介面：`client_mixin_layers()`、`client_mixin_group_names()`、`client_mixins_in_layer()`、`client_mixins_for_group()`，讓 raw/typed mixin seam 可讀且可稽核。
- `metabaseapi.client.http` 也集中維護 `CLIENT_MIXIN_SEAM_REGISTRY`，每個 domain 同步定義 raw/typed seam，由 registry 產生 `CLIENT_RAW_MIXIN_GROUPS` 與 `CLIENT_TYPED_MIXIN_GROUPS`。
- `metabaseapi.cli_commands` 下的 `actions_commands.py`、`activity_commands.py`、`automagic_commands.py`、`api_key_commands.py`、`agent_commands.py`、`alert_commands.py`、`comment_commands.py`、`analytics_commands.py`、`platform_bug_reporting_commands.py`、`platform_cache_commands.py`、`platform_channel_commands.py`、`platform_cloud_migration_commands.py`、`data_studio_commands.py`、`database_commands.py`、`collection_commands.py`、`card_commands.py`、`card_query_commands.py`、`dashboard_commands.py`、`dashboard_query_commands.py`、`schema_commands.py`、`user_commands.py` 提供命令實作，legacy root-level shim 已移除。
- 其中 `CARD_COMMAND_MODULE` / `DASHBOARD_COMMAND_MODULE` 是資源生命週期命令；`CARD_QUERY_COMMAND_MODULE` / `DASHBOARD_QUERY_COMMAND_MODULE` 是查詢與執行命令；`platform_*_commands` 是平台維運命令且都屬於 `PLATFORM_OPERATIONS_MODULES`；分群邏輯可透過 `metabaseapi.cli_commands` 的 `COMMAND_MODULE_GROUP_REGISTRY`（`COMMAND_MODULE_GROUPS` 為公開別名）、`CORE_RESOURCE_MODULES`、`ASSET_AUTHORING_MODULES`、`QUERY_AND_EXECUTION_MODULES`、`PLATFORM_OPERATIONS_MODULES` 查核。
- 命令域對應清單同步維護於 `docs/plans/2026-05-17_cli-command-domain-map.md`。

## migration rules
- 新增命令邏輯要放在 `metabaseapi.cli_commands` 底下，透過 `src/metabaseapi/cli_commands/__init__.py` 匯入註冊。
- CLI 套件直接匯入 `metabaseapi.cli_commands` 套件下對應 module 的實作，不保留 legacy root-level shim。
- Client 新功能要走 `metabaseapi.client.http` 的型別/實作路徑；`raw`/`typed` 只保留 domain 切面實作。

## import contract
- 對外入口（public entry）：
  - `metabaseapi.cli`（app 與命令註冊進入點）
  - `metabaseapi.client`（`MetabaseClient`、`_MetabaseClientRawMixin`、`_MetabaseClientTypedMixin`）
- 內部實作入口（implementation）：
  - `metabaseapi.client.http`（client 實作集中點）
- 回歸規則：
  - 每次 module 命名或匯入邊界變更都要同步更新 `tests/test_import_contracts.py`。

## verification notes
- Import-time smoke 建議至少包含：
  - `import metabaseapi.cli`
  - `import metabaseapi.cli_commands`
  - `from metabaseapi.cli_commands import *`
  - `import metabaseapi.cli_commands.actions_commands, metabaseapi.cli_commands.automagic_commands, metabaseapi.cli_commands.api_key_commands`
  - `from metabaseapi.client import MetabaseClient`
  - `from metabaseapi.client import _MetabaseClientRawMixin, _MetabaseClientTypedMixin`
- 重要設計調整要同步更新 `docs/plans/*.md`。
