# SKILL: Development Rules

## Role
You are the implementation agent. Follow PLAN.md exactly.
Do not extend scope.

## Core Principles (in priority order)
1. Follow PLAN.md strictly.
2. Prefer simple code over abstractions.
3. Use clear names over clever code.
4. Keep functions short and focused.
5. Do not introduce additional frameworks.

## Architecture Rules
- routers.py: HTTP layer only
- services.py: business logic only
- models/db: persistence only
- No cross-layer shortcuts

## API Rules
- Validate input with Pydantic schemas
- Return 404 for missing resources
- PATCH updates only provided fields
- Keep error responses consistent

## Data Rules
- Title must be non-empty and ≤200 chars
- completed defaults to false
- created_at set once
- updated_at updated on modification

## Testing Rules
Must include tests for:
- /health endpoint
- Full CRUD flow
- 404 on missing ID
- Validation failure for empty title

Tests must be deterministic.

## Git Rules
- Small, logical commits
- Clear commit messages
- Before PR: run tests and confirm success

## Escalation Rules (ask human)
Stop and ask when:
- Requirements are unclear
- A secret/token is needed
- A destructive operation is required
When asking:
- Provide 2–3 options
- Recommend one
- Explain tradeoffs
