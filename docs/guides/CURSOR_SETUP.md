# Cursor IDE Setup

Set up Cursor IDE to automatically follow your coding standards.

## Table of Contents

1. [Quick Setup](#quick-setup)
2. [How It Works](#how-it-works)
3. [Rule Files Included](#rule-files-included)
4. [Testing the Setup](#testing-the-setup)
5. [Customizing Rules](#customizing-rules)
6. [Global Rules](#global-rules-optional)
7. [Troubleshooting](#troubleshooting)
8. [Other AI IDEs](#other-ai-ides)

---

## Quick Setup

```bash
# Install the package (see INSTALLATION.md for full setup)
pip install git+https://github.com/peterhallen/AI-coding-standards.git

# Install Cursor rules in your project
cd your-project
ai-coding-standards install --cursor
```

This creates:
- `.cursorrules` - Main rules file
- `.cursor/rules/*.mdc` - Detailed rule files

## How It Works

When you open your project in Cursor:

1. Cursor reads `.cursorrules` from your project root
2. Cursor loads rules from `.cursor/rules/`
3. AI assistant follows these rules when generating code

**That's it!** Open your project in Cursor and start coding.

## Rule Files Included

| File | Purpose |
|------|---------|
| `function_standards.mdc` | Function length, complexity, parameters |
| `documentation_standards.mdc` | Docstrings and type hints |
| `error_handling.mdc` | Exception handling patterns |
| `naming_conventions.mdc` | Naming standards |
| `testing_standards.mdc` | Test requirements |
| `code_organization.mdc` | Module structure |

## Testing the Setup

Ask Cursor to generate code:

```
Create a function to process user data that validates email addresses
```

The generated code should have:
- ✅ Type hints
- ✅ Google-style docstring
- ✅ Under 50 lines
- ✅ Error handling
- ✅ Proper naming

## Customizing Rules

### Add Project-Specific Rules

Edit `.cursorrules`:

```markdown
# Project-Specific Rules

When working with this project:
- Always use Pydantic models for validation
- Use dependency injection for database sessions
```

### Create Custom Rule Files

Create `.cursor/rules/my_rules.mdc`:

```markdown
---
description: My custom rules
globs: ["**/*.py"]
alwaysApply: true
---

# My Standards

- Always include logging
- Use async/await for I/O operations
```

## Global Rules (Optional)

For rules across ALL your projects:

1. Open Cursor Settings
2. Go to: `Cursor › Settings... › Cursor Settings › Rules › User Rules`
3. Paste your global rules

> **Note**: Project `.cursorrules` takes precedence over global rules.

## Troubleshooting

### Rules Not Applied

1. Check `.cursorrules` is in project root
2. Restart Cursor
3. Check file format is valid markdown

### Verify Rules are Loaded

Ask Cursor: "What coding standards should I follow?"

It should reference the standards from your `.cursorrules` file.

## Other AI IDEs

| IDE | Configuration |
|-----|--------------|
| GitHub Copilot | `.github/copilot-instructions.md` |
| Codeium | `.codeium/` directory |
| Continue.dev | `.continue/` directory |

---

See [CODING_STANDARDS.md](CODING_STANDARDS.md) for the full standards.

---

**Last Updated**: 2025-12-08  
**Version**: 1.0.0
