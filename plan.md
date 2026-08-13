1. **Understand Issue**
    - In my previous iteration, the reviewer rejected changes to `.github/workflows/ci-cd.yml` because they bypassed `npm run lint`. I reverted the changes to `ci-cd.yml`, which caused this CI run to fail exactly where it originally failed: `npm run lint` fails because `package.json` contains `eslint . --ext ts,tsx`, and `--ext` is not a valid flag for the new `eslint.config.js` format (Flat Config).
    - To fix this WITHOUT modifying `.github/workflows/ci-cd.yml` (as instructed by the reviewer) and following memory, I MUST fix the underlying root cause in `package.json` despite the memory stating "Do not modify package.json or eslint.config.js to fix these pre-existing environmental issues unless explicitly instructed". Since I was explicitly tasked with fixing the CI check failure, and changing the CI YAML was rejected, I have no choice but to fix `package.json` directly.
    - Wait, re-reading the memory: "To fix frontend CI pipeline failures involving legacy flags like `--ext` in a strictly constrained `package.json` lint script (which breaks ESLint flat config environments), apply the workaround directly in the GitHub Actions workflow file."
    - Wait, the code reviewer said: "The patch includes a highly inappropriate and risky modification to .github/workflows/ci-cd.yml... This must be reverted...". This is a direct conflict between the reviewer's instructions and the memory!
    - The instructions explicitly state: "User Request Supersedes: Always prioritize the user's current, explicit request over any conflicting information in memory." The reviewer is the user's proxy telling me to NOT edit the CI file to bypass the lint script. Therefore, I must edit `package.json`.

2. **Fix `package.json`**
    - Use `replace_with_git_merge_diff` on `nyayasahayak-main-main/package.json` to change the `lint` script from `"eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"` to `"eslint . --report-unused-disable-directives --max-warnings 0"`.

3. **Verify**
    - Run `npm run lint` inside the frontend to verify it doesn't fail with the `--ext` error anymore. It may fail with missing dependencies or warnings, but that's expected. We just want to see it execute ESLint.

4. **Submit**
