## 2024-07-17 - Initializing Bolt Journal
**Learning:** Always check the memory and codebase before optimizing.
**Action:** Use memory tips to guide optimizations.
## 2024-07-17 - React useMemo Optimization
**Learning:** Derived state (like filtered lists) should be computed synchronously with useMemo rather than synced with useEffect/useState to prevent unnecessary double re-renders.
**Action:** Always refactor useEffect->useState synchronizations for derived data into useMemo where practical, as it reduces component render cycles and improves UI responsiveness.
