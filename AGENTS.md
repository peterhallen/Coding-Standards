# AGENTS.md

**Purpose:** Authoritative instructions for agentic coding tools (opencode, Cursor, Copilot) operating in this repository.

**Authority & Rules:** This file is the primary entry point. Follow the most specific rule first. User/system instructions override all. Normative sources:
- `.cursorrules`
- `.cursor/rules/*.mdc`
- `docs/guides/*` (AI_COLLABORATION, PROMPT_STANDARDS, CODE_COMPLIANCE, VERIFICATION)

**Agent Principles**
- Be precise and minimal; fix root causes only.
- Preserve existing architecture and patterns.
- Avoid unrelated refactors, renames, or stylistic churn.
- Do not add comments, dependencies, or features unless asked.

**Build / Lint / Test**
- Install dev deps: `pip install -r requirements-dev.txt`
- Lint: `flake8` and `pylint src`
- Tests: `pytest`
- Single test: `pytest tests/test_file.py::test_name`
- Pre-commit (if needed): `pre-commit run --all-files`

**Code Style**
- Imports: standard lib → third-party → local; no unused imports.
- Formatting: respect `.editorconfig`; no auto-format unless requested.
- Types: add hints only where patterns exist; don’t introduce new schemes.
- Naming: match surrounding conventions; don’t change public APIs.
- Errors: follow existing error-handling patterns only.

**Testing, Docs & Security**
- Run the narrowest relevant tests; don’t fix unrelated failures.
- Update docs only when behavior changes; follow Markdown standards.
- Never add secrets; respect sensitive-data hooks. Stop and notify on detection.
