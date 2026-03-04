## 2024-03-04 - Unbounded in-memory reports dictionaries
**Learning:** Found unbounded dictionaries (`self.reports`) used in several backend services (`BailReckonerService`, `SentencingAssistantService`, `JudgmentValidatorService`). Since these services are often singletons and the Fast API instances run indefinitely, storing each request in an in-memory dictionary causes a memory leak as it grows infinitely.
**Action:** Refactor backend services to be stateless and avoid keeping in-memory dictionaries for unbounded state.
