# Context

## package/module structure
- `metabaseapi.cli` owns Typer app lifecycle (app, global options, client wiring, error adapters).
- `metabaseapi.cli.runtime` owns the Typer app object, CLI parsing helpers, output/error execution helpers, and callback configuration; command modules import runtime helpers from this Module, not from the `metabaseapi.cli` package facade.
- `metabaseapi.cli.commands` is the command registration package; each module inside owns command implementations for related API surface.
- `metabaseapi.client` exports exactly one public client symbol: `MetabaseClient` from `metabaseapi.client.http`.
- `metabaseapi.wire` owns cross-layer HTTP wire types (`JSONValue`, query params, raw API request/response wrappers); it is not a domain model module.
- `metabaseapi.client.http` is the canonical concrete client implementation, owns async HTTP transport, and exports only `MetabaseClient`.
- `metabaseapi.client.raw` 和 `metabaseapi.client.typed` 保留為 domain-sliced internal function modules，module stem 使用 singular/domain 名稱（例如 `card.py`、`dashboard.py`、`cloud_migration.py`、`schema.py`），由 `client/http.py` 的 `MetabaseClient` 明確 wrapper method 轉呼叫；Data Studio client methods live in `data_studio.py`, not a generic `misc.py`.
- `metabaseapi.client.raw` / `metabaseapi.client.typed` package `__init__` 不 re-export endpoint functions；public caller interface 只能是 `MetabaseClient`。
- `metabaseapi.client.typed.<domain>` 直接匯入對應的 `metabaseapi.endpoints.requests.<domain>` request models，並直接從 `metabaseapi.endpoints.entities` / `metabaseapi.endpoints.responses` 匯入 endpoint types；不要透過 `metabaseapi.endpoints` public facade 匯入內部 endpoint symbols。
- `metabaseapi.cli.commands` 下的 module stem 使用 domain/action 名稱，不重複 `_commands` suffix；例如 `action.py`、`activity.py`、`card.py`、`card_query.py`、`dashboard.py`、`dashboard_query.py`、`data_studio.py`、`bug_reporting.py`、`cache.py`、`channel.py`、`cloud_migration.py`。legacy root-level shim 與 legacy `*_commands.py` module name 已移除。
- `metabaseapi.endpoints` 是 public package facade，只暴露 `entities`、`execution`、`requests`、`responses` submodules；不要在 top-level 重匯出每個 endpoint symbol。
- `metabaseapi.endpoints.execution` owns the request execution interface (`MetabaseRequestClient`) and shared request base implementation; `metabaseapi.endpoints.requests` is the request model package, owns the `REQUEST_MODULES` registry, and its package `__init__` does not re-export request classes.
- 其中 `CARD_COMMAND_MODULE` / `DASHBOARD_COMMAND_MODULE` 是資源生命週期命令；`CARD_QUERY_COMMAND_MODULE` / `DASHBOARD_QUERY_COMMAND_MODULE` 是查詢與執行命令；`bug_reporting`、`cache`、`channel`、`cloud_migration` 是平台維運命令且都屬於 `PLATFORM_OPERATIONS_MODULES`；分群邏輯可透過 `metabaseapi.cli.commands` 的 `COMMAND_MODULE_GROUP_REGISTRY`（`COMMAND_MODULE_GROUPS` 為公開別名）、`CORE_RESOURCE_MODULES`、`ASSET_AUTHORING_MODULES`、`QUERY_AND_EXECUTION_MODULES`、`PLATFORM_OPERATIONS_MODULES` 查核。
- 命令域對應以 `metabaseapi.cli.commands.COMMAND_MODULE_GROUP_REGISTRY` 為 source of truth，並由 `tests/test_import_contracts.py` 稽核 package files、分群、命令唯一性。

## migration rules
- 新增命令邏輯要放在 `metabaseapi.cli.commands` 底下，透過 `src/metabaseapi/cli/commands/__init__.py` 匯入註冊。
- CLI 套件直接匯入 `metabaseapi.cli.commands` 套件下對應 module 的實作，不保留 legacy root-level shim；command modules 只能從 `metabaseapi.cli.runtime` 匯入 shared CLI helpers。
- Client 新功能要走 `metabaseapi.client.http` 的型別/實作路徑；`raw`/`typed` 只保留 domain 切面實作。
- 新增 endpoint request model 要放在 `metabaseapi.endpoints.requests.<domain>`，並同步更新 `tests/test_import_contracts.py` 的 `REQUEST_MODULE_CONTRACTS`。

## import contract
- 對外入口（public entry）：
  - `metabaseapi.cli`（app 與命令註冊進入點）
  - `metabaseapi.client`（`MetabaseClient`）
  - `metabaseapi.endpoints`（typed endpoint submodule facade）
- 內部實作入口（implementation）：
  - `metabaseapi.client.http`（client 實作集中點）
- 回歸規則：
  - 每次 module 命名或匯入邊界變更都要同步更新 `tests/test_import_contracts.py`。

## verification notes
- Import-time smoke 建議至少包含：
  - `import metabaseapi.cli`
  - `import metabaseapi.cli.commands`
  - `from metabaseapi.cli.commands import *`
  - `import metabaseapi.cli.commands.action, metabaseapi.cli.commands.automagic, metabaseapi.cli.commands.api_key`
  - `from metabaseapi.client import MetabaseClient`
- 重要設計調整要同步更新本檔與 `tests/test_import_contracts.py`，讓命名邊界有文件與 executable contract 雙重保護。
