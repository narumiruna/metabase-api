# Context

## package/module structure
- `metabaseapi.cli` owns Typer app lifecycle (app, global options, client wiring, error adapters).
- `metabaseapi.cli_commands` is the command registration package; each module inside owns command implementations for related API surface.
- `metabaseapi.cli_commands_core.py` and `metabaseapi.cli_commands_dashboard.py` are migration shims kept as thin module-level imports.
- `metabaseapi.client` exports canonical client symbols and re-exports from `metabaseapi.client.http`.
- `metabaseapi.client.http` is the canonical concrete implementation, owning async HTTP transport and mixin assembly.
- `metabaseapi.client.raw` 和 `metabaseapi.client.typed` 保留為 domain-sliced mixin 構件，供 `client/http.py` 組裝。

## migration rules
- 新增命令邏輯要放在 `metabaseapi.cli_commands` 底下，透過 `src/metabaseapi/cli_commands/__init__.py` 匯入註冊。
- CLI 套件不要從 `metabaseapi.cli_commands_core` / `metabaseapi.cli_commands_dashboard` 匯入實作。
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
  - `import metabaseapi.cli_commands.core`
  - `import metabaseapi.cli_commands.dashboard`
  - `from metabaseapi.client import MetabaseClient`
  - `from metabaseapi.client import _MetabaseClientRawMixin, _MetabaseClientTypedMixin`
- 重要設計調整要同步更新 `docs/plans/*.md`。
