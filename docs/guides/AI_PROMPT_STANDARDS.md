# AI Prompt Standards and Best Practices

## Table of Contents

1. [Introduction](#introduction)
2. [Prompt Structure](#prompt-structure)
3. [Prompt Writing Guidelines](#prompt-writing-guidelines)
4. [Context Management](#context-management)
5. [Task Specification](#task-specification)
6. [Code Generation Prompts](#code-generation-prompts)
7. [Code Review Prompts](#code-review-prompts)
8. [Debugging Prompts](#debugging-prompts)
9. [Documentation Prompts](#documentation-prompts)
10. [Common Patterns](#common-patterns)
11. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
12. [Prompt Templates](#prompt-templates)

---

## Introduction

### Purpose

This document establishes standards for writing effective prompts when collaborating with AI coding assistants. Well-structured prompts lead to better code quality, faster iteration, and more maintainable results.

### Principles

- **Clarity**: Be specific and unambiguous
- **Context**: Provide sufficient background information
- **Constraints**: Clearly state requirements and limitations
- **Consistency**: Use consistent terminology and patterns
- **Iteration**: Start broad, then refine based on results

---

## Prompt Structure

### Standard Prompt Template

A well-structured prompt should include:

1. **Context** - Background information about the project/codebase
2. **Task** - What you want the AI to do
3. **Constraints** - Limitations, requirements, or preferences
4. **Output Format** - Expected format of the response
5. **Examples** - Sample inputs/outputs (when helpful)

### Example Structure

```
[Context]
I'm working on a Python project that follows our coding standards.
The project uses FastAPI for the API layer and SQLAlchemy for database access.

[Task]
Create a new endpoint `/api/users/{user_id}` that returns user information
including their profile and recent activity.

[Constraints]
- Must follow our coding standards (max 50 lines per function)
- Include proper error handling for missing users
- Add type hints and docstrings
- Write tests with 80%+ coverage

[Output Format]
Provide the endpoint function, model definitions, and test file.
```

---

## Prompt Writing Guidelines

### 1. Be Specific

**Bad:**
```
Fix the bug in the user service.
```

**Good:**
```
The `get_user_by_id` function in `src/services/user_service.py` raises
a KeyError when the user_id doesn't exist. Update it to return None
instead and add proper error handling with a custom UserNotFoundError.
```

### 2. Provide Context

**Bad:**
```
Add authentication to the API.
```

**Good:**
```
Add JWT-based authentication to our FastAPI application. The project
already uses `python-jose` for token handling. Create a dependency
function that validates JWT tokens from the Authorization header and
raises HTTPException(401) if invalid. Apply it to all routes under
`/api/protected/*`.
```

### 3. Specify Constraints

**Bad:**
```
Create a function to process data.
```

**Good:**
```
Create a function `process_user_data` that:
- Takes a list of user dictionaries
- Validates each user has required fields: 'id', 'email', 'name'
- Returns a dictionary with 'valid_users' and 'invalid_users' lists
- Handles errors gracefully (no exceptions for invalid data)
- Follows our coding standards (type hints, docstrings, max 50 lines)
- Uses async/await for I/O operations
```

### 4. Include Examples

**Bad:**
```
Write a function to format dates.
```

**Good:**
```
Write a function `format_timestamp` that converts ISO 8601 timestamps
to a human-readable format.

Examples:
- Input: "2024-01-15T10:30:00Z"
  Output: "January 15, 2024 at 10:30 AM"
- Input: "2024-01-15T14:45:30-05:00"
  Output: "January 15, 2024 at 2:45 PM"
```

### 5. Reference Existing Code

**Bad:**
```
Create a new service similar to the user service.
```

**Good:**
```
Create a new `ProductService` class following the same pattern as
`UserService` in `src/services/user_service.py`. It should:
- Use the same database session pattern
- Follow the same error handling approach
- Include similar logging
- Have the same method structure (get_by_id, create, update, delete)
```

---

## Context Management

### When to Provide Context

Always include context when:
- Working with existing codebases
- Referencing project-specific patterns
- Using domain-specific terminology
- Working with complex systems

### Context Elements

1. **Project Type**: Web app, CLI tool, library, etc.
2. **Tech Stack**: Frameworks, libraries, versions
3. **Architecture**: Project structure, design patterns
4. **Standards**: Coding standards, style guides
5. **Dependencies**: Key libraries and their usage

### Example Context Block

```
[Project Context]
- Python 3.9+ FastAPI application
- Uses SQLAlchemy ORM with async sessions
- Follows our coding standards (see CODING_STANDARDS.md)
- Project structure: src/api/, src/models/, src/services/
- Uses Pydantic for request/response validation
- Testing with pytest and 80% coverage requirement
```

---

## Task Specification

### Clear Task Statements

Use action verbs and be specific:

- ✅ "Create a function that..."
- ✅ "Refactor the existing code to..."
- ✅ "Add error handling to..."
- ✅ "Write tests for..."
- ❌ "Make it better"
- ❌ "Fix the thing"
- ❌ "Do the user stuff"

### Task Breakdown

For complex tasks, break them down:

```
[Task]
Implement user authentication with the following steps:

1. Create a User model with email, password_hash, and created_at fields
2. Create a register endpoint that hashes passwords using bcrypt
3. Create a login endpoint that validates credentials and returns JWT
4. Add middleware to protect routes requiring authentication
5. Write tests for all endpoints with 80%+ coverage
```

---

## Code Generation Prompts

### Best Practices

1. **Specify Standards**: Always reference coding standards
2. **Request Documentation**: Ask for docstrings and type hints
3. **Include Tests**: Request tests as part of code generation
4. **Error Handling**: Specify error handling requirements
5. **Performance**: Mention performance considerations if relevant

### Example Code Generation Prompt

```
Generate a function `calculate_monthly_revenue` that:

1. Takes a list of transaction dictionaries with 'amount' and 'date' fields
2. Filters transactions for the current month
3. Sums the amounts
4. Returns the total as a float

Requirements:
- Follow our coding standards (CODING_STANDARDS.md)
- Include Google-style docstring with Args, Returns, Raises
- Add type hints for all parameters and return value
- Handle edge cases (empty list, invalid dates)
- Keep function under 50 lines
- Include error handling with specific exceptions
- Write a pytest test file with Arrange-Act-Assert pattern
```

---

## Code Review Prompts

### Review Checklist Prompts

```
Review the following code against our coding standards:

1. Function length (max 50 lines)
2. Cyclomatic complexity (max 10)
3. Type hints present
4. Docstrings present (Google-style)
5. Error handling appropriate
6. Test coverage adequate
7. No security vulnerabilities
8. Follows naming conventions

[Code to review]
```

### Specific Review Requests

```
Review `src/services/payment_service.py` focusing on:
- Security: Check for SQL injection, XSS, or credential exposure
- Performance: Identify potential bottlenecks
- Error handling: Ensure all exceptions are properly handled
- Test coverage: Verify all code paths are tested
```

---

## Debugging Prompts

### Effective Debugging Prompts

Include:
- Error messages (full traceback)
- Expected behavior
- Actual behavior
- Steps to reproduce
- Environment details

### Example Debugging Prompt

```
[Error]
I'm getting a `KeyError: 'user_id'` in the following code:

```python
def process_user(data: dict) -> dict:
    user_id = data['user_id']
    return {"id": user_id}
```

[Context]
- The function is called from an API endpoint
- The request body is parsed as JSON
- Sometimes the request doesn't include 'user_id'

[Expected Behavior]
Return a 400 error with a clear message if 'user_id' is missing.

[Actual Behavior]
Returns 500 Internal Server Error with KeyError.

Please fix this with proper error handling following our standards.
```

---

## Documentation Prompts

### Documentation Generation

```
Generate documentation for the `UserService` class in `src/services/user_service.py`:

1. Module-level docstring describing the service
2. Class docstring with Attributes section
3. Method docstrings (Args, Returns, Raises)
4. Usage examples in docstrings
5. Update README.md with service overview

Follow Google-style docstring format as per our standards.
```

---

## Common Patterns

### Pattern 1: Refactoring

```
Refactor the `process_data` function in `src/utils/data_processor.py` to:
- Extract helper functions for validation and transformation
- Reduce cyclomatic complexity below 10
- Add type hints and docstrings
- Keep each function under 50 lines
- Maintain existing functionality
- Add tests for new helper functions
```

### Pattern 2: Feature Addition

```
Add a new feature to export user data to CSV:

1. Create `export_users_to_csv` function in `src/services/export_service.py`
2. Use the existing `UserService.get_all_users()` method
3. Handle file I/O errors appropriately
4. Include headers: id, email, name, created_at
5. Follow our coding standards
6. Write tests with mocked file operations
```

### Pattern 3: Bug Fix

```
Fix the memory leak in `src/services/cache_service.py`:

[Issue]
The cache grows indefinitely and never evicts old entries.

[Current Implementation]
Uses a simple dictionary with no size limits.

[Requirements]
- Implement LRU cache with max 1000 entries
- Use `functools.lru_cache` or similar
- Add logging when entries are evicted
- Maintain existing API
- Add tests for cache eviction
```

---

## Anti-Patterns to Avoid

### ❌ Vague Requests

**Bad:**
```
Make it work better.
Fix the code.
Improve performance.
```

**Good:**
```
Optimize the database query in `get_user_posts` to reduce query time
from 500ms to under 100ms by adding proper indexes and using select_related.
```

### ❌ Missing Context

**Bad:**
```
Add authentication.
```

**Good:**
```
Add JWT-based authentication to our FastAPI app. Use `python-jose` library
which is already in requirements.txt. Create a dependency function that
validates tokens and apply it to protected routes.
```

### ❌ Unrealistic Expectations

**Bad:**
```
Write the entire application.
```

**Good:**
```
Create the user authentication module with register, login, and logout
endpoints. We'll integrate it with the rest of the app in the next step.
```

### ❌ No Standards Reference

**Bad:**
```
Create a function to process users.
```

**Good:**
```
Create a function `process_users` following our coding standards
(CODING_STANDARDS.md). Include type hints, docstrings, error handling,
and keep it under 50 lines.
```

---

## Prompt Templates

### Template 1: New Feature

```
[Context]
[Project/Codebase context]

[Task]
[Specific feature to implement]

[Requirements]
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

[Constraints]
- [Constraint 1]
- [Constraint 2]

[Standards]
Follow CODING_STANDARDS.md:
- Type hints required
- Docstrings required
- Max 50 lines per function
- 80%+ test coverage

[Output]
[Expected output format]
```

### Template 2: Code Review

```
Review the following code against our coding standards:

[File]: [path/to/file.py]

[Code]
[Code snippet or reference]

[Focus Areas]
- [Area 1]
- [Area 2]

[Standards Reference]
CODING_STANDARDS.md
```

### Template 3: Refactoring

```
Refactor [component] in [file] to:

[Goals]
- [Goal 1]
- [Goal 2]

[Constraints]
- Maintain existing API
- No breaking changes
- [Other constraints]

[Standards]
- Follow CODING_STANDARDS.md
- Reduce complexity to < 10
- Extract functions < 50 lines
- Add tests for new functions
```

### Template 4: Bug Fix

```
[Issue Description]
[What's wrong]

[Expected Behavior]
[What should happen]

[Actual Behavior]
[What actually happens]

[Error Details]
[Error messages, tracebacks]

[Environment]
- Python version: [version]
- Dependencies: [relevant packages]
- OS: [operating system]

[Code Location]
[File and function/class]

[Request]
Fix the issue following our coding standards and add tests to prevent regression.
```

---

## Integration with Coding Standards

When prompting AI assistants, always reference coding standards:

```
Follow the coding standards in CODING_STANDARDS.md:
- Function length: max 50 lines
- Complexity: max 10
- Type hints: required
- Docstrings: Google-style
- Testing: 80%+ coverage
- Error handling: specific exceptions
```

---

## Quick Reference

### Effective Prompt Checklist

- [ ] Clear, specific task description
- [ ] Sufficient context provided
- [ ] Constraints and requirements listed
- [ ] Coding standards referenced
- [ ] Expected output format specified
- [ ] Examples included (if helpful)
- [ ] Error handling specified
- [ ] Testing requirements mentioned

### Prompt Quality Indicators

**High Quality:**
- Specific and actionable
- Includes context
- References standards
- Clear constraints
- Realistic scope

**Low Quality:**
- Vague or ambiguous
- Missing context
- No standards reference
- Unclear requirements
- Unrealistic scope

---

**Last Updated**: 2025-01-19  
**Version**: 1.0.0

