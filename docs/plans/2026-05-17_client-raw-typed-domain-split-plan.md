## Goal
將 `MetabaseClient` 的 raw/typed 呼叫由目前兩個大檔維度，改為「依資源（resource）」切分的模組群，降低單檔複雜度、提升 localizability 與可測試性；在不改變現有 API 介面（含 `*_typed` 及 raw 同名方法）與測試結果的前提下完成。

## Architecture
- **Module**：`src/metabaseapi/client_raw.py`、`src/metabaseapi/client_typed.py`、`src/metabaseapi/client_transport.py`。
- **Interface**：延續目前 `MetabaseClient` 的公開方法名稱與行為。
- **Seam**：在 `client.py` 保留 class 聚合，子模組以 import 組裝。
  目標是把 endpoint 實作群組在 `src/metabaseapi/client/raw/`、`src/metabaseapi/client/typed/` 下的資源模組，`client_transport` 保持 transport+通用 helper 不變。

## Plan
- [x] 建立 `src/metabaseapi/client/raw/` 與 `src/metabaseapi/client/typed/`（含 `__init__.py`）；把 raw/typed module 的目前 `_*` mixin 切出「action/card/dashboard/...」資源群； verify with: `test -d src/metabaseapi/client/raw src/metabaseapi/client/typed`。
- [x] 在 `src/metabaseapi/client/raw/__init__.py` 匯出 `_MetabaseClientRawMixin` 並在其中聚合子模組 mixin；同理建立 `src/metabaseapi/client/typed/__init__.py`； verify with: `python -m py_compile` 目標檔可解析。
- [x] 逐一遷移 `client_raw.py` 現有方法到對應資源模組，並保持方法簽名不變（例如 `list_actions`, `create_card`, `get_dashboard`）； verify with: `git diff` 檢視原方法名完全保留。
- [x] 逐一遷移 `client_typed.py` 內 `*_typed` 方法到對應資源模組，保留 `run()` 與 `list_actions_typed` 等既有行為順序； verify with: `ruff check src/metabaseapi/client/**/*.py`。
- [x] 重寫 `client.py` 只保留 `MetabaseClient(_MetabaseClientRawMixin)` 並修正 imports 指向新的 `client/raw` 聚合入口； verify with: `uv run python -m compileall src/metabaseapi/client.py`。
- [x] 更新測試 import（若有）及最小化維持 `tests/test_client.py` 相關斷言； verify with: `uv run pytest tests/test_client.py -q`。
- [x] 執行完整回歸：`ruff check`、`ty check`、`pytest`； verify with all pass.

## Risks
- method 分群時漏轉接導致某些 endpoint 重複定義或遺漏。
- resource 名稱不一致造成 import 循環。
- 仍保留 `run`/`from_settings` seam 行為可能因重組順序變更。

## Completion Checklist
- [x] raw/typed 實作檔重構為資源模組後 `pytest -q` 仍為 `171 passed`； verify with `uv run pytest -q`。
- [x] 所有現有 raw API 與 `*_typed` API 呼叫在單元測試與 `metabaseapi --help` 命令測試中行為不變； verify with regression tests + `uv run metabaseapi --help | head`。
- [x] `client.py` 可讀性與行數壓縮，且可在每個 1000 行規則內； verify with `wc -l src/metabaseapi/client.py src/metabaseapi/client_raw.py ...`。
