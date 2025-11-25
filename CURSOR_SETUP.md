# Cursor IDE Setup Guide

This guide explains how to use the AI Coding Standards with Cursor IDE and other agentic IDEs.

## What is Cursor?

Cursor is an AI-powered code editor that uses AI to help write, edit, and understand code. It can read and follow project-specific rules to ensure generated code follows your standards.

## Installation Methods

### Method 1: Using the CLI Tool (Recommended)

Install the standards package and use the CLI to set up Cursor:

```bash
# Install the package
pip install git+https://github.com/peterhallen/AI-coding-standards.git

# Install standards with Cursor support
ai-coding-standards install --cursor
```

This will install:
- `.cursorrules` file in your project root
- `.cursor/rules/` directory with detailed rule files

### Method 2: Manual Installation

1. Copy `.cursorrules` to your project root
2. Copy the `.cursor/rules/` directory to your project root

## How Cursor Uses These Rules

### 1. `.cursorrules` File

Cursor automatically reads the `.cursorrules` file in your project root. This file contains:
- Core coding principles
- Function and method guidelines
- Documentation requirements
- Error handling patterns
- Testing standards
- Code quality metrics

The AI assistant in Cursor will follow these rules when:
- Generating new code
- Refactoring existing code
- Suggesting improvements
- Answering questions about code

### 2. `.cursor/rules/` Directory

Cursor also supports more granular rules in `.cursor/rules/*.mdc` files. These files:
- Can target specific file patterns (via `globs`)
- Have priorities and descriptions
- Are automatically loaded by Cursor

Our package includes these rule files:
- `function_standards.mdc` - Function length, complexity, parameters
- `documentation_standards.mdc` - Docstrings and type hints
- `error_handling.mdc` - Exception handling patterns
- `naming_conventions.mdc` - Naming standards
- `testing_standards.mdc` - Test requirements
- `code_organization.mdc` - Module structure

## Using Cursor with the Standards

### 1. Open Your Project

Simply open your project in Cursor. Cursor will automatically:
- Read `.cursorrules` from the project root
- Load rules from `.cursor/rules/` directory
- Apply these rules to all AI interactions

### 2. Generate Code

When you ask Cursor to generate code, it will automatically follow the standards:

**Example Prompt:**
```
Create a function to process user data that validates email addresses
```

**Cursor will generate code that:**
- ✅ Has type hints
- ✅ Has a Google-style docstring
- ✅ Is under 50 lines
- ✅ Has proper error handling
- ✅ Follows naming conventions

### 3. Refactor Code

When refactoring, Cursor will maintain standards:

**Example Prompt:**
```
Refactor this function to reduce complexity
```

**Cursor will:**
- ✅ Extract helper functions if needed
- ✅ Reduce nesting depth
- ✅ Maintain documentation
- ✅ Keep type hints

### 4. Code Review

Cursor can review code against the standards:

**Example Prompt:**
```
Review this code against our coding standards
```

**Cursor will check:**
- Function length and complexity
- Documentation completeness
- Error handling
- Naming conventions
- Test coverage

## Global User Rules (Optional)

For rules that should apply across ALL projects in Cursor:

1. Open Cursor Settings
2. Navigate to: `Cursor › Settings... › Cursor Settings › Rules › User Rules`
3. Paste the contents of `.cursorrules` or key standards
4. These rules will apply to all projects

**Note**: Project-specific `.cursorrules` files take precedence over global rules.

## Customizing Rules

### Modify `.cursorrules`

Edit `.cursorrules` to add project-specific rules:

```markdown
# Project-Specific Rules

When working with this FastAPI project:
- Always use Pydantic models for request/response validation
- Use dependency injection for database sessions
- Follow our API versioning pattern: /api/v1/...
```

### Add Custom Rule Files

Create new `.mdc` files in `.cursor/rules/`:

```markdown
---
description: FastAPI-specific patterns
globs: ["**/api/**/*.py"]
alwaysApply: true
priority: high
---

# FastAPI Standards

[CRITICAL] All API endpoints MUST:
- Use Pydantic models for validation
- Include OpenAPI tags
- Have proper error responses
```

## Verification

### Check if Rules are Loaded

1. Open Cursor
2. Open any Python file
3. Ask Cursor: "What coding standards should I follow?"
4. Cursor should reference the standards from `.cursorrules`

### Test Code Generation

Try generating code and verify it follows standards:

**Prompt:**
```
Create a function to calculate the total cost of items in a shopping cart
```

**Verify the generated code has:**
- Type hints
- Docstring
- Error handling
- Proper naming

## Troubleshooting

### Rules Not Being Applied

1. **Check file location**: `.cursorrules` must be in project root
2. **Restart Cursor**: Sometimes Cursor needs a restart to load new rules
3. **Check file format**: Ensure `.cursorrules` is valid markdown
4. **Check rule files**: Ensure `.cursor/rules/*.mdc` files are properly formatted

### Rules Too Strict

If rules are too strict for certain files:

1. Add exceptions in `.cursorrules`:
   ```markdown
   ## Exceptions
   - Legacy files in `legacy/` directory may not follow all standards
   ```

2. Create a rule file with lower priority:
   ```markdown
   ---
   priority: low
   ---
   ```

### Conflicting Rules

If you have multiple rule sources:
1. Project `.cursorrules` takes highest priority
2. `.cursor/rules/*.mdc` files are applied based on `globs` and `priority`
3. Global user rules are applied last

## Other Agentic IDEs

### GitHub Copilot

GitHub Copilot can use similar rules:
1. Create `.github/copilot-instructions.md` with standards
2. Or add comments in code files

### Codeium

Codeium supports:
1. `.codeium/` directory with configuration
2. Project-specific settings

### Continue.dev

Continue.dev can use:
1. `.continue/` directory with config
2. Custom instructions in settings

## Best Practices

1. **Keep rules updated**: Update `.cursorrules` as standards evolve
2. **Be specific**: More specific rules lead to better code generation
3. **Test regularly**: Verify generated code follows standards
4. **Iterate**: Refine rules based on what works best for your team
5. **Document exceptions**: Clearly document when rules don't apply

## Example Workflow

```bash
# 1. Install standards
pip install git+https://github.com/peterhallen/AI-coding-standards.git

# 2. Set up project
cd my-project
ai-coding-standards install --cursor --docs

# 3. Open in Cursor
cursor .

# 4. Start coding with AI assistance
# Cursor will automatically follow the standards!
```

## Additional Resources

- [Cursor Documentation](https://docs.cursor.com/)
- [CODING_STANDARDS.md](CODING_STANDARDS.md) - Full coding standards
- [AI_PROMPT_STANDARDS.md](AI_PROMPT_STANDARDS.md) - Prompt writing guide
- [INSTALLATION.md](INSTALLATION.md) - General installation guide

---

**Last Updated**: 2025-01-19  
**Version**: 1.0.0

