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
```

### 便利命令

```bash
metabaseapi current-user
metabaseapi list-databases
metabaseapi get-dashboard 1
metabaseapi get-card 2
```

所有輸出都會以可讀 JSON（縮排、排序）輸出，便於 AI / 腳本處理。
