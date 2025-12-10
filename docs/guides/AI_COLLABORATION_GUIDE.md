# AI Collaboration Guide

A guide for teams collaborating on codebases using AI coding assistants (Cursor, Copilot, etc.).

## Table of Contents

1. [The Challenge](#the-challenge)
2. [Solution Overview](#solution-overview)
3. [Setup for Teams](#setup-for-teams)
4. [Standardized Prompting](#standardized-prompting)
5. [Code Review for AI-Generated Code](#code-review-for-ai-generated-code)
6. [Workflow Best Practices](#workflow-best-practices)
7. [Troubleshooting Inconsistencies](#troubleshooting-inconsistencies)

---

## The Challenge

When multiple developers use AI assistants on the same codebase, inconsistencies arise:

| Problem | Symptom |
|---------|---------|
| Different styles | Mixed formatting, naming conventions |
| Different patterns | Inconsistent error handling, logging |
| Different architectures | Conflicting design decisions |
| Different documentation | Varied docstring formats |

**Root cause**: Each AI assistant operates with different context and instructions.

---

## Solution Overview

Achieve consistency through three layers:

```text
┌─────────────────────────────────────────────────┐
│  Layer 1: INPUT CONSISTENCY                     │
│  Same rules fed to all AI assistants            │
│  (.cursorrules, .cursor/rules/*.mdc)            │
├─────────────────────────────────────────────────┤
│  Layer 2: OUTPUT VALIDATION                     │
│  Automated checks on all generated code         │
│  (pre-commit, CI/CD, linters)                   │
├─────────────────────────────────────────────────┤
│  Layer 3: PROCESS CONSISTENCY                   │
│  Standardized workflows and review practices    │
│  (prompts, reviews, documentation)              │
└─────────────────────────────────────────────────┘
```

---

## Setup for Teams

### Step 1: Repository Setup (Once per Project)

```bash
# Install standards in the shared repository
ai-coding-standards install --cursor --docs --pre-commit --overwrite
```

**Commit these files to version control:**

```bash
git add .cursorrules .cursor/ .editorconfig .flake8 .pylintrc pyproject.toml .pre-commit-config.yaml
git commit -m "Add AI coding standards for team consistency"
git push
```

### Step 2: Developer Setup (Each Team Member)

```bash
# Clone the repository
git clone <your-repo>
cd <your-repo>

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows

# Install dev tools
pip install black isort mypy flake8 pylint pytest pytest-cov pre-commit

# Install pre-commit hooks
pre-commit install
```

### Step 3: Verify Setup

Each developer should verify:

```bash
# Check rules are loaded
cat .cursorrules

# Check tools work
black --version
isort --version
flake8 --version
```

**In Cursor**: Ask "What coding standards should I follow?" - the AI should reference your `.cursorrules`.

---

## Standardized Prompting

### Use Consistent Prompt Patterns

Create a shared prompt library for common tasks. All developers use the same templates:

#### New Feature Template

```text
[Context]
Working on [PROJECT_NAME], a Python [PROJECT_TYPE].
Following our coding standards in .cursorrules.

[Task]
Create [FEATURE_DESCRIPTION]

[Requirements]
- Follow CODING_STANDARDS.md
- Include type hints and docstrings
- Add error handling
- Write tests with 80%+ coverage

[Constraints]
- Max 50 lines per function
- Max 5 parameters per function
- Use existing patterns in the codebase
```

#### Refactoring Template

```text
[Context]
Refactoring [FILE_PATH] to meet coding standards.

[Task]
Refactor to:
- Reduce function length to ≤50 lines
- Reduce complexity to ≤10
- Add missing type hints
- Add missing docstrings

[Constraints]
- Maintain existing API
- No breaking changes
- Follow patterns in .cursorrules
```

#### Bug Fix Template

```text
[Error]
[ERROR_MESSAGE]

[File]
[FILE_PATH]

[Expected Behavior]
[WHAT_SHOULD_HAPPEN]

[Actual Behavior]
[WHAT_HAPPENS]

[Request]
Fix following our coding standards. Include tests to prevent regression.
```

### Prompt Best Practices

| ✅ Do | ❌ Don't |
|-------|----------|
| Reference `.cursorrules` | Assume AI knows your standards |
| Specify constraints clearly | Leave requirements ambiguous |
| Include existing patterns | Let AI invent new patterns |
| Request tests | Skip testing requirements |
| Break large tasks into steps | Ask for entire features at once |

---

## Code Review for AI-Generated Code

### Review Checklist

When reviewing AI-generated code, verify:

#### Consistency Checks
- [ ] Matches existing code patterns in the codebase
- [ ] Uses same naming conventions as surrounding code
- [ ] Follows same error handling patterns
- [ ] Uses existing utilities/helpers (not reinventing)

#### Quality Checks
- [ ] Functions ≤50 lines
- [ ] Complexity ≤10
- [ ] Type hints present
- [ ] Docstrings present (Google-style)
- [ ] Tests included

#### Integration Checks
- [ ] Imports organized correctly
- [ ] No duplicate functionality
- [ ] Uses existing abstractions
- [ ] Consistent with module structure

### Review Comments

When requesting changes, reference standards:

**Good:**
```
This function exceeds 50 lines (CODING_STANDARDS.md §4.1).
Please extract helper functions for validation and transformation.
```

**Bad:**
```
Function too long, please fix.
```

---

## Workflow Best Practices

### 1. Always Pull Latest Rules

Before starting work:

```bash
git pull origin main
```

This ensures you have the latest `.cursorrules` and configurations.

### 2. Verify AI Understands Context

Start sessions by asking:

```text
What coding standards and patterns should I follow in this project?
```

The AI should reference your `.cursorrules` and `CODING_STANDARDS.md`.

### 3. Review Before Committing

```bash
# Run all checks before committing
black .
isort .
flake8 .
mypy .
pytest

# Or use pre-commit
pre-commit run --all-files
```

### 4. Commit with Context

Include context in commit messages:

```bash
git commit -m "Add user authentication module

- AI-assisted implementation using Cursor
- Follows CODING_STANDARDS.md patterns
- Includes tests (92% coverage)"
```

### 5. Document Decisions

When AI suggests multiple approaches, document why you chose one:

```python
# Using factory pattern here (not builder) because:
# - Simpler for our use case
# - Matches existing patterns in src/services/
# - Recommended by team lead in PR #123
```

---

## Troubleshooting Inconsistencies

### Problem: AI Ignores Rules

**Symptoms**: Generated code doesn't follow `.cursorrules`

**Solutions**:
1. Restart Cursor/IDE to reload rules
2. Explicitly reference rules in prompts: "Follow .cursorrules"
3. Verify `.cursorrules` is in project root
4. Check file isn't too large (keep under 50KB)

### Problem: Different Developers Get Different Outputs

**Symptoms**: Same prompt produces different code for different developers

**Solutions**:
1. Ensure all developers have pulled latest rules
2. Use shared prompt templates (not ad-hoc prompts)
3. Include more context in prompts
4. Reference specific files/patterns to follow

### Problem: AI Invents New Patterns

**Symptoms**: AI creates new utilities instead of using existing ones

**Solutions**:
1. Reference existing code: "Use the pattern from src/utils/helpers.py"
2. List available utilities in prompts
3. Add codebase context: "We already have X, Y, Z utilities"
4. Review for duplication before merging

### Problem: Inconsistent Between Sessions

**Symptoms**: Same developer gets different outputs across sessions

**Solutions**:
1. Use consistent prompt templates
2. Start sessions with context-setting prompts
3. Keep `.cursorrules` as the source of truth
4. Document decisions for future reference

---

## Team Agreements

Consider establishing these team agreements:

### 1. Rule Ownership

- **Who can modify `.cursorrules`?** (e.g., team lead approval required)
- **How are rule changes communicated?** (e.g., PR with team review)
- **How often are rules reviewed?** (e.g., quarterly)

### 2. Prompt Sharing

- **Where are shared prompts stored?** (e.g., `docs/prompts/`)
- **Who maintains prompt templates?** (e.g., rotating responsibility)
- **How are new prompts added?** (e.g., PR with examples)

### 3. Review Standards

- **What requires human review?** (e.g., all AI-generated code)
- **Who reviews AI code?** (e.g., someone who didn't generate it)
- **What's the review checklist?** (e.g., `CODING_STANDARDS.md` checklist)

### 4. Documentation

- **How is AI usage documented?** (e.g., commit messages)
- **What decisions need documentation?** (e.g., architecture choices)
- **Where is documentation stored?** (e.g., ADRs in `docs/decisions/`)

---

## Quick Reference

### Daily Workflow

```bash
# Start of day
git pull origin main

# Before coding
# Ask AI: "What standards should I follow?"

# While coding
# Use shared prompt templates
# Reference existing patterns

# Before committing
pre-commit run --all-files

# Commit
git commit -m "Description (AI-assisted)"
```

### Key Files for Consistency

| File | Purpose | Synced Via |
|------|---------|------------|
| `.cursorrules` | AI behavior rules | Git |
| `.cursor/rules/*.mdc` | Detailed AI rules | Git |
| `pyproject.toml` | Tool configs | Git |
| `.pre-commit-config.yaml` | Pre-commit hooks | Git |
| `CODING_STANDARDS.md` | Human reference | Git |

### Consistency Checklist

Before merging any AI-generated code:

- [ ] Ran `pre-commit run --all-files`
- [ ] Code matches existing patterns
- [ ] No duplicate functionality
- [ ] Tests pass with adequate coverage
- [ ] Peer reviewed by another developer

---

**Remember**: AI assistants are powerful tools, but consistency comes from shared rules, automated checks, and team discipline. The AI follows the rules you give it—make sure everyone gives it the same rules!

---

**Last Updated**: 2025-12-08  
**Version**: 1.0.0

