## 2024-05-22 - Memory Leak in JudgmentValidatorService
**Learning:** The `JudgmentValidatorService` was storing every validation result in an unbounded dictionary `self.reports`, causing a memory leak.
**Action:** Always check service classes for stateful storage that grows unbounded. Use stateless services or proper caching (e.g., Redis) with TTL.
