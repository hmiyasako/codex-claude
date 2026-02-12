# CLAUDE EXECUTION GUIDE

## Mission
Implement PLAN.md using rules from SKILL.md.
Create a GitHub PR and request Codex review.

## Workflow
1. Scaffold project structure
2. Implement database models
3. Implement API routes
4. Implement business logic
5. Write tests
6. Update README

## Local Commands
- Install dependencies
- Run tests: pytest
- Run server: uvicorn app.main:app

## PR Workflow (mandatory)
- Branch name: feat/todo-api
- Commit logically
- Push branch
- Create PR:
    gh pr create --fill
- Request Codex review:
    gh pr comment --body "@codex review"

## When to Stop and Ask
Trigger Notification and wait if:
- Secrets/credentials are required
- Spec not covered in PLAN.md
- A major design change is proposed

When asking, include:
- Problem summary
- Options
- Recommendation
