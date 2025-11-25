# AI Prompt Standards - Quick Reference

> One-page reference guide for writing effective AI prompts. See `AI_PROMPT_STANDARDS.md` for full documentation.

## Prompt Structure

```
[Context]
[Background information about project/codebase]

[Task]
[Specific task to accomplish]

[Constraints]
[Requirements, limitations, preferences]

[Output Format]
[Expected format of response]
```

## Best Practices

### ✅ DO

- **Be specific**: "Create a function `process_users` that validates email addresses"
- **Provide context**: Include project type, tech stack, architecture
- **Specify constraints**: Max function length, error handling, testing requirements
- **Reference standards**: "Follow CODING_STANDARDS.md"
- **Include examples**: Show expected input/output
- **Break down tasks**: Split complex tasks into steps

### ❌ DON'T

- **Vague requests**: "Make it better", "Fix the code"
- **Missing context**: "Add authentication" (without details)
- **Unrealistic scope**: "Write the entire application"
- **No standards**: Don't reference coding standards
- **Ambiguous requirements**: "Do the user stuff"

## Common Patterns

### New Feature

```
[Context]
Python FastAPI app using SQLAlchemy

[Task]
Create `/api/users/{id}` endpoint

[Requirements]
- Type hints and docstrings
- Error handling for 404
- Tests with 80%+ coverage
- Max 50 lines per function

[Standards]
Follow CODING_STANDARDS.md
```

### Code Review

```
Review `src/services/user_service.py`:
- Function length (max 50 lines)
- Type hints present
- Docstrings present
- Error handling appropriate
- Test coverage adequate
```

### Refactoring

```
Refactor `process_data` to:
- Extract helper functions
- Reduce complexity < 10
- Add type hints
- Keep functions < 50 lines
- Maintain existing API
```

### Bug Fix

```
[Error]
KeyError: 'user_id' in `get_user_by_id`

[Expected]
Return None if user not found

[Actual]
Raises KeyError

[Request]
Fix with proper error handling per CODING_STANDARDS.md
```

## Quick Checklist

- [ ] Clear, specific task
- [ ] Sufficient context
- [ ] Constraints listed
- [ ] Standards referenced
- [ ] Output format specified
- [ ] Examples included (if helpful)
- [ ] Error handling specified
- [ ] Testing requirements mentioned

---

**Full Documentation**: See `AI_PROMPT_STANDARDS.md`

