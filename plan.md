1. **Fix `npm run lint` failure in `nyayasahayak-main-main`:**
   - Modified `package.json` to remove `--ext ts,tsx` from the `lint` script. (Already done)

2. **Fix Pytest failure in `backend/test_endpoints.py`:**
   - Renamed `test_endpoint` to `verify_endpoint` and wrapped top-level execution with `if __name__ == "__main__":`. (Already done)
   - Wait, `backend/test_auth.py` and `backend/test_auth_comprehensive.py` and `backend/scripts/test_api_endpoints.py` might also be failing during Pytest collection for the same reason if they have `test_*` functions without fixtures or top-level executions. Let's fix them too.

3. **Complete pre commit steps:**
   - Ensure the fixes address the CI failures.

4. Submit the changes.
