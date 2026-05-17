# CLI 命令模組映射（2026-05-17）

## 目標
- 把命令實作與 domain 對齊，讓新增或修改 endpoint 時，先找對應 `metabaseapi.cli_commands` 模組。
- 保持 CLI 對外命令名稱不變，僅調整 module 邊界與命名清晰度。

## Domain Modules
- `actions_commands`（14）：`list-actions`, `create-action`, `list-public-actions`, `get-action`, `delete-action`, `update-action`, `create-action-public-link` 等。
- `automagic_commands`（12）：`automagic-database-candidates`, `automagic-model-index-primary-key`, `automagic-entity`, `automagic-entity-cell`, `automagic-entity-rule` 等。
- `api_key_commands`（6）：`create-api-key`, `list-api-keys`, `count-api-keys`, `update-api-key`, `delete-api-key`, `regenerate-api-key`。
- `agent_commands`（9）：`agent-execute`, `agent-ping`, `agent-search`, `get-agent-table`, `agent-construct-query`, `agent-query` 等。
- `alerts_comments_commands`（9）：`list-alerts`, `get-alert`, `delete-alert-subscription`, `get-comment`, `create-comment`, `delete-comment` 等。
- `analytics_commands`（9）：`analyze-chart`, `anonymous-stats`, `most-recently-viewed-dashboard`, `list-popular-items`, `current-user` 等。
- `catalog_commands`（7）：`list-databases`, `list-cards`, `list-dashboards`, `list-users`, `get-database` 等。
- `dashboard_commands`（69）：卡片/儀表板/收藏/資料表/資料集合 API，包含 `create-card`, `query-card`, `get-dashboard`, `create-dashboard`, `get-user`, `create-collection`, `get-table` 等。
- `data_studio_commands`（5）：`data-studio-table-discard-values`, `data-studio-table-edit`, `data-studio-table-rescan-values`, `data-studio-table-selection`, `data-studio-table-sync-schema`。
- `platform_bug_reporting_commands`（2）：`bug-reporting-connection-pool-details`, `bug-reporting-details`。
- `platform_cache_commands`（4）：`get-cache`, `put-cache`, `delete-cache`, `invalidate-cache`。
- `platform_channel_commands`（5）：`list-channels`, `create-channel`, `test-channel`, `get-channel`, `update-channel`。
- `platform_cloud_migration_commands`（3）：`create-cloud-migration`, `get-cloud-migration`, `cancel-cloud-migration`。

## 註冊接點
- `src/metabaseapi/cli_commands/__init__.py` 的 `COMMAND_MODULES` 定義唯一註冊清單，`register_commands()` 僅從此清單匯入模組。
- `tests/test_import_contracts.py` 驗證 module 清單與實際 import 行為一致，並保留 legacy shim 不再可 import 的契約。
