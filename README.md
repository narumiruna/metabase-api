# Metabase API

A small async-first Python client and Typer CLI for the Metabase API.

## 安裝

```bash
uv sync
```

## 環境變數

- `METABASE_URL`：Metabase 服務網址（預設 `http://localhost:3000`）
- `METABASE_API_KEY`：Metabase API 金鑰（API Key authentication）
- `METABASE_TIMEOUT_SECONDS`：請求逾時秒數（預設 `30.0`）
- `METABASE_VERIFY_SSL`：是否驗證 TLS 憑證（預設 `true`）

## 使用方式

```bash
export METABASE_URL=https://your-metabase.example
export METABASE_API_KEY=your-api-key
```

### 一般請求

```bash
metabaseapi request GET /api/user/current
metabaseapi request GET /api/card/1 -q dashboard=1 -q archived=false
metabaseapi request POST /api/dataset -b '{"query": {"database": 1, "type": "query", "query": {"source-table": 1}}'
metabaseapi invoke GET /api/user/current
```

### 便利命令

```bash
metabaseapi current-user
metabaseapi list-databases
metabaseapi get-dashboard 1
metabaseapi get-card 2
metabaseapi get-user 4
metabaseapi get-table 8
metabaseapi get-database 1
metabaseapi list-databases
metabaseapi list-cards
metabaseapi list-users
metabaseapi list-collections
metabaseapi create-database my_db postgres --details '{"host":"localhost","port":5432}'
```

所有輸出都會以可讀 JSON（縮排、排序）輸出，便於 AI / 腳本處理。

## Live Test（實際打 API）

使用 fixtures 中的 endpoint 清單做 smoke test（預設只測 `GET`）：

```bash
# 測所有 GET endpoint（依 OpenAPI fixture）
just live-test GET

# 只測前 50 筆
just live-test GET 50

# 測指定方法（例如 GET,POST）
just live-test GET,POST
```

若要放寬失敗門檻，可用 `--max-failures`、`--strict`，例如：

```bash
uv run python scripts/live_endpoint_smoke_test.py --methods GET --strict --max-failures 0
```
