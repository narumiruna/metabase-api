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
metabaseapi request POST /api/dataset -b '{"query": {"database": 1, "type": "query", "query": {"source-table": 1}}}'
metabaseapi request PUT /api/card/1 -b '{"name":"Updated card"}'
metabaseapi request DELETE /api/card/1
metabaseapi request DELETE /api/cache -b '{"model":"question","model_id":[1]}'
metabaseapi invoke GET /api/user/current
```

### 便利命令

```bash
metabaseapi current-user
metabaseapi list-databases
metabaseapi create-database my_db postgres --details '{"host":"localhost","port":5432}'
metabaseapi get-database 1
metabaseapi list-cards
metabaseapi create-question Orders '{"database":1,"type":"query","query":{"source-table":2}}'
metabaseapi create-card Orders '{"database":1,"type":"query","query":{"source-table":2}}' --type question
metabaseapi get-card 2
metabaseapi list-dashboards
metabaseapi get-dashboard 1
metabaseapi list-users
metabaseapi get-user 4
metabaseapi list-collections
metabaseapi get-collection root
metabaseapi list-tables
metabaseapi get-table 8
metabaseapi list-fields
metabaseapi get-field 9
```

所有輸出都會以可讀 JSON（縮排、排序）輸出，便於 AI / 腳本處理。Metabase 文件中的所有 endpoints 都可用 `request` 或 `invoke` 指定 HTTP method、path、query 與 JSON body 呼叫；便利命令則維持手寫、逐步補齊高價值路徑。

## Live test

`.env` 設好 `METABASE_URL` 與 `METABASE_API_KEY` 後，可以執行低風險唯讀 live checks：

```bash
just live-test
```

此命令只檢查 current-user 的 raw、convenience、typed 路徑，輸出欄位名稱與狀態，不輸出 API key。
