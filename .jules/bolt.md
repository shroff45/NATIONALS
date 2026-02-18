## 2025-02-18 - [Database Indexing Strategy]
**Learning:** In projects without active migration tools (like Alembic) configured for auto-migrations, modifying the model definition (`index=True`) is the correct 'code change', but it doesn't automatically apply to existing databases.
**Action:** Always verify model changes using `sqlalchemy` inspection in tests to ensure the *code* is correct, even if the runtime DB migration is out of scope for the immediate code change task.
