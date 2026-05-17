## Goal
將 CLI 命令按 domain module 拆分到 `cli_commands`，`metabaseapi.cli_commands` 提供穩定的命令註冊 seam，讓新增 endpoint 的操作盡量只需觸碰一個對應 domain module，維持現有 CLI 行為與測試。

## Architecture
- **Module**：`src/metabaseapi/cli/__init__.py`、`src/metabaseapi/cli_commands/*.py`、`tests/test_cli*.py`。
- **Interface**：保持目前指令名稱與參數不變。
- **Seam**：`metabaseapi.cli` 僅做 app 建立、setting 與 command 註冊；命令行為分散到各 domain module `src/metabaseapi/cli_commands/<domain>_commands.py`，由 `__init__.py` 收斂到 `COMMAND_MODULES`。

## Current domain modules
- `actions_commands`, `automagic_commands`, `api_key_commands`, `agent_commands`
- `alerts_comments_commands`, `analytics_commands`, `catalog_commands`
- `platform_bug_reporting_commands`（bug reporting）
- `platform_cache_commands`（cache）
- `platform_channel_commands`（channel）
- `platform_cloud_migration_commands`（cloud migration）
- `data_studio_commands`（data studio）
- `dashboard_commands`（cards / dashboards / collections / users / tables / db 交叉資料）

## Plan
- [x] 建立 `src/metabaseapi/cli_commands/` 套件與 `__init__.py`，設計 `register_commands()` 入口； verify with: 目錄與入口可 import。
- [x] 將舊 `cli_commands_core.py` 命令依資源切到 `src/metabaseapi/cli_commands/*.py`（如 actions/cards/collections/...）； verify with: `grep` 檢視每個 endpoint 命令在對應檔案。
- [x] 將舊 `cli_commands_dashboard.py` 命令轉入同套件下 `dashboard_commands.py`；保持選項名稱與回傳格式； verify with: `metabaseapi --help` contains 主要 dashboard 指令。
- [x] 重構 `src/metabaseapi/cli/__init__.py`，以 `from metabaseapi.cli_commands import register_commands; register_commands()` 進行註冊； verify with: import/啟動測試正常。
- [x] 調整 `tests/test_cli.py` / `tests/test_cli_core.py` / `tests/test_cli_misc.py` 的 import 與命令覆蓋目標（保持測試內容可維持）； verify with: `uv run pytest tests/test_cli*.py -q`。
- [x] 全域驗證：`uv run ruff check`, `ty check`, `pytest -q`； verify all pass.

## Risks
- 變更註冊路徑時可能影響 `_register_commands` 執行順序與 help 顯示順序。
- 命令與測試的 import path 依賴可能短暫破壞。

## Completion Checklist
- [x] CLI 指令與參數集與現行行為一致（`uv run metabaseapi --help` 包含既有命令）； verify with `uv run metabaseapi --help`。
- [x] `tests/test_cli.py`、`tests/test_cli_core.py`、`tests/test_cli_misc.py` 全數通過； verify with `uv run pytest tests/test_cli*.py -q`。
- [x] 所有 CLI 入口檔案與命令模組符合 1000 行限制； verify with `python - <<'PY'` 逐檔掃描。
