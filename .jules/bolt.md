## 2024-05-22 - Regex IgnoreCase Performance Trap
**Learning:** `re.IGNORECASE` is significantly slower (10-15x) than lowercasing the text once and running a case-sensitive regex, especially for large texts. Even replacing simple substring searches (`in` operator) with regexes can be a performance regression if not careful.
**Action:** When validating large documents, pay the upfront cost of `text.lower()` and use case-sensitive regexes/string searches instead of relying on `re.IGNORECASE`.
