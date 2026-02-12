# PLAN: Minimal TODO REST API

## Objective
Build a small TODO management REST API to test an AI-driven workflow:
- Implementation by Claude Code
- Code review by Codex via GitHub PR

## Functional Requirements

### Health Check
- GET /health
- Response: { "status": "ok" }

### Todo CRUD
Model fields:
- id: integer (primary key)
- title: string (1–200 chars, required)
- completed: boolean (default false)
- created_at: datetime (auto-set)
- updated_at: datetime (auto-updated)

Endpoints:
- POST /todos → create
- GET /todos → list all
- GET /todos/{id} → get one
- PATCH /todos/{id} → partial update
- DELETE /todos/{id} → delete

## Explicit Non-Goals
Do NOT implement:
- Authentication or authorization
- Pagination, filtering, or search
- Background jobs, queues, or caching
- Frontend UI
- Production deployment setup

## Tech Stack (fixed)
- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- SQLite file database
- pytest for testing

## Project Structure Target
app/
  main.py
  db.py
  models.py
  schemas.py
  services.py
  routers.py

tests/
  test_health.py
  test_todos.py

## Non-Functional Priorities
1. Correct behavior
2. Test coverage
3. Readable code
4. Simplicity over extensibility

## Definition of Done
- All tests pass with `pytest`
- Server runs with `uvicorn app.main:app`
- Basic README with run/test instructions
- GitHub PR created
