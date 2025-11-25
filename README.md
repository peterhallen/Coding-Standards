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

1. Clone this repository:
```bash
git clone <repository-url>
cd AI-coding-standards
```

2. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Verify installation:
```bash
black --version
isort --version
mypy --version
pytest --version
```

### Using the Standards in Your Project

1. Copy the configuration files to your project:
   - `pyproject.toml` - Tooling configuration
   - `.editorconfig` - Editor settings
   - `.flake8` - Flake8 linter config
   - `.pylintrc` - Pylint config

2. Install the development dependencies in your project:
```bash
pip install -r requirements-dev.txt
```

3. Run code quality checks:
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

## 📚 Documentation

### Full Documentation

See [`CODING_STANDARDS.md`](CODING_STANDARDS.md) for comprehensive guidelines covering:

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

### Quick Reference

See [`CODING_STANDARDS_QUICK_REF.md`](CODING_STANDARDS_QUICK_REF.md) for a condensed one-page reference guide.

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
