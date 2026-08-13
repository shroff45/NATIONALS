1. **Explore File & State Usage**
    - Both `src/features/nationals/components/CaseIntakeTriage.tsx` and `src/features/main/components/CaseIntakeTriage.tsx` have the same anti-pattern: using `useState` and `useEffect` to manage a derived array (`filteredCases`).

2. **Refactor React Logic**
    - Use `replace_with_git_merge_diff` on both files to change `useState` for `filteredCases` to `useMemo`.
    - Ensure `useMemo` is imported from React in both files.

3. **Verify and Pre-commit Instructions**
    - Verify changes with frontend types & linting using `run_in_bash_session`.
    - Retrieve and follow `pre_commit_instructions`.

4. **Submit**
    - Create journal entry in `.jules/bolt.md`.
    - Call `submit`.
