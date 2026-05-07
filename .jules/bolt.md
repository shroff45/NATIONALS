## 2025-05-18 - ESLint Flat Config Crash
**Learning:** Running `eslint` directly with `npx eslint` crashes due to missing `@eslint/js` when there is an `eslint.config.js` file, likely because of version 9 changes.
**Action:** Stick to the project's `npm run lint` script.
