# AI Coding Standards

A comprehensive set of coding standards and best practices designed for both human developers and AI coding assistants. This repository provides guidelines, tooling configuration, and examples to ensure consistency, readability, maintainability, and performance across Python codebases.

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Tooling Configuration](#tooling-configuration)
- [Standards Summary](#standards-summary)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains:

- **Comprehensive Coding Standards** (`CODING_STANDARDS.md`) - Detailed guidelines covering all aspects of Python development
- **Quick Reference Guide** (`CODING_STANDARDS_QUICK_REF.md`) - One-page reference for common standards
- **Tooling Configuration** - Pre-configured settings for Black, isort, mypy, pytest, flake8, and pylint
- **Example Code** - Demonstrations of standards-compliant code
- **CI/CD Integration** - GitHub Actions workflow for automated validation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

#### Option 1: Install as Package (Recommended)

Install directly from GitHub:

```bash
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

Or with development dependencies:

```bash
pip install "git+https://github.com/peterhallen/AI-coding-standards.git#egg=ai-coding-standards[dev]"
```

Then install standards in your project:

```bash
ai-coding-standards install
```

#### Option 2: Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/peterhallen/AI-coding-standards.git
cd AI-coding-standards
```

2. Install in development mode:
```bash
pip install -e .
```

3. Install standards in your project:
```bash
ai-coding-standards install
```

### Using the Standards in Your Project

After installation, use the CLI tool to set up your project:

```bash
# Basic installation
ai-coding-standards install

# With all options
ai-coding-standards install --overwrite --docs --pre-commit --cursor
```

This will:
- Copy configuration files (`.editorconfig`, `.flake8`, `.pylintrc`, `pyproject.toml`)
- Optionally install documentation files to `docs/standards/`
- Optionally set up pre-commit hooks
- Optionally install Cursor IDE rules (`.cursorrules` and `.cursor/rules/`)

### Running Code Quality Checks

```bash
# Format code
black .

# Sort imports
isort .

# Type checking
mypy .

# Linting
flake8 .
pylint .

# Run tests with coverage
pytest --cov
```

See [INSTALLATION.md](INSTALLATION.md) for detailed installation instructions.

## 📚 Documentation

### Coding Standards

- **[CODING_STANDARDS.md](CODING_STANDARDS.md)** - Comprehensive coding standards covering:
  - General principles (DRY, KISS, YAGNI)
  - Code organization and structure
  - Function and method guidelines
  - Naming conventions
  - Documentation standards
  - Error handling patterns
  - Performance best practices
  - Python-specific standards
  - Testing standards
  - AI coder collaboration guidelines
  - Code review checklist

- **[CODING_STANDARDS_QUICK_REF.md](CODING_STANDARDS_QUICK_REF.md)** - Condensed one-page reference guide

### AI Prompt Standards

- **[AI_PROMPT_STANDARDS.md](AI_PROMPT_STANDARDS.md)** - Comprehensive guide for writing effective prompts when working with AI coding assistants:
  - Prompt structure and best practices
  - Context management
  - Task specification
  - Code generation prompts
  - Code review prompts
  - Debugging prompts
  - Documentation prompts
  - Common patterns and templates
  - Anti-patterns to avoid

This document helps developers write better prompts that lead to higher quality AI-generated code.

## 🛠️ Tooling Configuration

This repository includes pre-configured settings for:

### Code Formatting
- **Black** - Code formatter (100 char line length)
- **isort** - Import sorter (Black-compatible profile)

### Type Checking
- **mypy** - Static type checker (Python 3.8+)

### Linting
- **flake8** - Style guide enforcement (max complexity: 10, line length: 100)
- **pylint** - Code analysis (max complexity: 10, max args: 5)

### Testing
- **pytest** - Testing framework
- **coverage** - Code coverage tool (80% minimum threshold)

### Editor Configuration
- **EditorConfig** - Consistent coding styles across editors

All configurations are aligned with the coding standards defined in `CODING_STANDARDS.md`.

## 📊 Standards Summary

### Key Metrics

| Metric | Maximum | Preferred |
|--------|---------|-----------|
| Function length | 50 lines | 30 lines |
| Function parameters | 5 | 3 |
| Cyclomatic complexity | 10 | 5 |
| Nesting depth | 3 levels | 2 levels |
| Class length | 300 lines | - |
| Module length | 500 lines | - |
| Line length | 120 chars (hard) | 100 chars (soft) |

### Naming Conventions

- **Functions/Variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`
- **Boolean**: `is_`, `has_`, `can_` prefixes

### Documentation Requirements

- ✅ All public functions require docstrings (Google-style)
- ✅ Type hints required for all function parameters and returns
- ✅ Module docstrings for all modules
- ✅ Class docstrings for all classes

## 💡 Examples

See the [`examples/`](examples/) directory for code examples demonstrating:

- Proper function structure and documentation
- Error handling patterns
- Type hints usage
- Testing patterns
- Code organization

## 🛠️ CLI Tool

The package includes a CLI tool for easy installation and compliance checking:

```bash
# Show package information
ai-coding-standards info

# Install standards in current directory
ai-coding-standards install

# Install with options (including Cursor IDE support)
ai-coding-standards install --overwrite --docs --pre-commit --cursor

# Check code compliance
ai-coding-standards check-compliance

# Auto-fix compliance issues
ai-coding-standards fix-compliance

# Install in specific directory
ai-coding-standards install /path/to/project
```

See [INSTALLATION.md](INSTALLATION.md) for complete CLI documentation.

## 👥 For New Developers

**New to the team?** Start here:

1. **Quick Setup** (5 minutes): See [ONBOARDING.md](ONBOARDING.md)
2. **Install Standards**: `ai-coding-standards install --cursor --docs --pre-commit`
3. **Read Quick Reference**: `CODING_STANDARDS_QUICK_REF.md`

## 🔄 Bringing Code Into Compliance

**Have existing code that needs to meet standards?**

1. **Check Compliance**: `ai-coding-standards check-compliance`
2. **Auto-Fix**: `ai-coding-standards fix-compliance`
3. **Full Guide**: See [CODE_COMPLIANCE.md](CODE_COMPLIANCE.md)

The compliance guide covers:
- Automated fixes (formatting, imports)
- Manual refactoring strategies
- Migration approaches (incremental, file-by-file, etc.)
- Common scenarios and solutions

## 🤖 Agentic IDE Integration (Cursor)

The standards are fully integrated with Cursor IDE and other agentic IDEs:

### Quick Setup

```bash
# Install with Cursor support
ai-coding-standards install --cursor
```

This installs:
- `.cursorrules` - Main rules file that Cursor reads automatically
- `.cursor/rules/` - Granular rule files for specific standards

### How It Works

When you open your project in Cursor, it automatically:
- Reads `.cursorrules` from the project root
- Loads rules from `.cursor/rules/` directory
- Applies these standards to all AI-generated code

The AI assistant will automatically follow your coding standards when:
- Generating new code
- Refactoring existing code
- Suggesting improvements
- Answering questions about code

See [CURSOR_SETUP.md](CURSOR_SETUP.md) for detailed setup instructions and examples.

## 🤝 Contributing

Contributions are welcome! When contributing:

1. Follow the coding standards defined in this repository
2. Ensure all code passes linting and type checking
3. Maintain or improve test coverage (80% minimum)
4. Update documentation as needed

### Development Workflow

1. Make your changes
2. Run code quality checks:
   ```bash
   black .
   isort .
   mypy .
   flake8 .
   pytest --cov
   ```
3. Commit with descriptive messages
4. Submit a pull request

## 📄 License

[Add your license here - e.g., MIT, Apache 2.0, etc.]

## 🔗 Additional Resources

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [Real Python - Best Practices](https://realpython.com/python-code-quality/)

---

**Last Updated**: 2025-01-19  
**Version**: 1.0.0
