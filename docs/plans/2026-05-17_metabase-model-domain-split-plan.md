## Goal
將 `metabase` 模型層從目前 `requests_part_a/b/c.py` 的尺寸切分方式，改為依資源的 domain module 重組（`requests`/`responses`/`entities`），提升導覽深度與維運 locality，並維持既有 `MetabaseClient` 與 `MetabaseRequestClient` 介面。

## Architecture
- **Module**：`src/metabaseapi/metabase/requests*.py`、`metabase/responses.py`、`metabase/entities.py`、`metabase/__init__.py`。
- **Interface**：維持目前在 `metabase` 套件對外 `__all__` 的 hand-written model/export 概念。
- **Design**：拆分為 `src/metabaseapi/metabase/endpoints/<resource>.py`（例如 `actions.py`, `cards.py`, `collections.py`），每個 module 管理該資源的 request/response entities。

## Plan
- [ ] 建立 `src/metabaseapi/metabase/endpoints/` 與 `__init__.py`，規劃資源對映（如 action/card/dashboard/collection/database/automagic/...）； verify with: 目錄存在且命名完整。
- [ ] 將 `requests_part_a.py`～`requests_part_c.py` 的內容依 `endpoint` 分組搬入 resource module； verify with: `grep` 比對 `*Request` class 名稱在新模組中完整存在。
- [ ] 將 `metabase/responses.py`、`metabase/entities.py` 中可對應到單一資源的型別一併搬到對應 endpoint module（或保留共享核心 entity），並維持匯出； verify with: `python -m compileall src/metabaseapi/metabase/endpoints`。
- [ ] 重寫 `src/metabaseapi/metabase/requests.py` 成為 aggregator（明確 `__all__`），避免 `*` 聚合； verify with: ruff 無 `F403/F405`。
- [ ] 更新 `src/metabaseapi/metabase/__init__.py` 匯入路徑與可見名單，維持原有公開 API； verify with: `python - <<'PY'` 匯入 smoke test，確認 `from metabaseapi.metabase import <核心類別>` 成功。
- [ ] 執行型別與測試：`uv run ty check`、`uv run pytest -q`； verify with 全通。

## Completion Checklist
- [ ] `metabase` 套件無任何 Python 檔超過 1000 行（含 `requests_part` 已移除或縮小）； verify with `python - <<'PY'` 扫描 `Path.rglob('*.py')`。
- [ ] 所有現有 endpoint request/response 仍可由 `metabase` 套件匯入（測試與 client 呼叫可通過）； verify with `uv run pytest tests/test_endpoints.py tests/test_metabase_models.py -q`。
- [ ] `uv run pytest tests/test_endpoints.py tests/test_metabase_models.py -q` 全數通過； verify with 該命令執行結果。
