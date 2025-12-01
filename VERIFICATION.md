# Installation Verification

Quick reference for verifying the CLI installation worked correctly.

## Files Installed

### Default (`ai-coding-standards install`)

| File | Purpose |
|------|---------|
| `.editorconfig` | Editor settings |
| `.flake8` | Flake8 linter config |
| `.pylintrc` | Pylint config |
| `pyproject.toml` | Black, isort, mypy, pytest config |
| `.pre-commit-config.yaml` | Pre-commit hooks |
| `.cursorrules` | Cursor IDE rules |

### With `--cursor` Flag

| File | Purpose |
|------|---------|
| `.cursor/rules/function_standards.mdc` | Function limits |
| `.cursor/rules/documentation_standards.mdc` | Docstring rules |
| `.cursor/rules/error_handling.mdc` | Exception patterns |
| `.cursor/rules/naming_conventions.mdc` | Naming rules |
| `.cursor/rules/testing_standards.mdc` | Test requirements |
| `.cursor/rules/code_organization.mdc` | Module structure |

### With `--docs` Flag

| File | Purpose |
|------|---------|
| `docs/standards/CODING_STANDARDS.md` | Full standards |
| `docs/standards/CODING_STANDARDS_QUICK_REF.md` | Quick reference |
| `docs/standards/AI_PROMPT_STANDARDS.md` | Prompt guide |
| `docs/standards/AI_PROMPT_STANDARDS_QUICK_REF.md` | Prompt quick ref |

## Verification Commands

### Check Installation

```bash
ai-coding-standards info
```

### Verify Files Exist

**macOS/Linux:**

```bash
ls -la .editorconfig .flake8 .pylintrc pyproject.toml .cursorrules
ls -la .cursor/rules/*.mdc          # if --cursor was used
ls -la docs/standards/*.md          # if --docs was used
```

**Windows (PowerShell):**

```powershell
Get-ChildItem .editorconfig, .flake8, .pylintrc, pyproject.toml, .cursorrules -Force
Get-ChildItem .cursor\rules\*.mdc -Force         # if --cursor was used
Get-ChildItem docs\standards\*.md                # if --docs was used
```

### Test Tools Work

```bash
black --version
isort --version
flake8 --version
mypy --version
pytest --version
```

## Summary

**Total files the CLI can install: 16**

- Configuration files: 6
- Cursor rules: 6
- Documentation files: 4
