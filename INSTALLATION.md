# Installation Guide

This guide explains how to install and use the AI Coding Standards package in your projects.

## Installation Methods

### Method 1: Install from GitHub (Recommended)

Install directly from the GitHub repository:

```bash
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

Or install with development dependencies:

```bash
pip install "git+https://github.com/peterhallen/AI-coding-standards.git#egg=ai-coding-standards[dev]"
```

### Method 2: Install from Local Source

If you've cloned the repository:

```bash
cd AI-coding-standards
pip install -e .
```

Or with development dependencies:

```bash
pip install -e ".[dev]"
```

### Method 3: Install from PyPI (When Published)

```bash
pip install ai-coding-standards
```

Or with development dependencies:

```bash
pip install ai-coding-standards[dev]
```

## Quick Start

### 1. Install the Package

```bash
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

### 2. Install Standards in Your Project

Navigate to your project directory and run:

```bash
ai-coding-standards install
```

This will:
- Copy configuration files (`.editorconfig`, `.flake8`, `.pylintrc`, `pyproject.toml`)
- Optionally install documentation files
- Optionally set up pre-commit hooks

### 3. Install with Options

```bash
# Install and overwrite existing configs
ai-coding-standards install --overwrite

# Install configs and documentation
ai-coding-standards install --docs

# Install configs and set up pre-commit hooks
ai-coding-standards install --pre-commit

# Install everything non-interactively
ai-coding-standards install --overwrite --docs --pre-commit --no-interactive
```

### 4. Set Up Pre-commit Hooks (Optional but Recommended)

If you installed with `--pre-commit`, hooks are already set up. Otherwise:

```bash
pre-commit install
```

## CLI Usage

### Install Command

```bash
ai-coding-standards install [TARGET_DIR] [OPTIONS]
```

**Options:**
- `--overwrite`: Overwrite existing configuration files
- `--no-interactive`: Don't prompt for confirmation
- `--docs`: Also install documentation files to `docs/standards/`
- `--pre-commit`: Set up pre-commit hooks

**Examples:**
```bash
# Install in current directory
ai-coding-standards install

# Install in specific directory
ai-coding-standards install /path/to/project

# Install with all options
ai-coding-standards install --overwrite --docs --pre-commit
```

### Info Command

Show package information:

```bash
ai-coding-standards info
```

## Manual Installation

If you prefer to install files manually:

### 1. Copy Configuration Files

Copy these files to your project root:
- `.editorconfig`
- `.flake8`
- `.pylintrc`
- `pyproject.toml` (merge with existing or replace)
- `.pre-commit-config.yaml`

### 2. Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

Or install individually:
```bash
pip install black isort mypy flake8 pylint pytest pytest-cov pre-commit
```

### 3. Set Up Pre-commit Hooks

```bash
pre-commit install
```

## Integration with Existing Projects

### Merging pyproject.toml

If your project already has a `pyproject.toml`, you'll need to merge configurations:

1. Copy relevant sections from the standards `pyproject.toml`:
   - `[tool.black]`
   - `[tool.isort]`
   - `[tool.mypy]`
   - `[tool.pytest.ini_options]`
   - `[tool.coverage.run]`
   - `[tool.coverage.report]`

2. Merge with your existing configuration, resolving any conflicts.

### Project Structure

After installation, your project should have:

```
your-project/
├── .editorconfig
├── .flake8
├── .pylintrc
├── .pre-commit-config.yaml
├── pyproject.toml
├── docs/
│   └── standards/
│       ├── CODING_STANDARDS.md
│       ├── CODING_STANDARDS_QUICK_REF.md
│       └── AI_PROMPT_STANDARDS.md
└── ...
```

## Verification

### Check Installation

```bash
ai-coding-standards info
```

### Verify Configuration Files

```bash
# Check if config files exist
ls -la .editorconfig .flake8 .pylintrc pyproject.toml

# Test formatters
black --check .
isort --check-only .

# Test linters
flake8 .
pylint your_module/

# Test type checking
mypy your_module/

# Run tests
pytest --cov
```

## Updating Standards

To update to the latest version:

```bash
pip install --upgrade git+https://github.com/peterhallen/AI-coding-standards.git
```

Then reinstall configs if needed:

```bash
ai-coding-standards install --overwrite
```

## Troubleshooting

### Permission Errors

If you get permission errors, install with `--user`:

```bash
pip install --user git+https://github.com/peterhallen/AI-coding-standards.git
```

### Config File Conflicts

If config files conflict with existing ones:

1. Review the differences
2. Merge manually, or
3. Use `--overwrite` to replace (backup first!)

### Pre-commit Not Working

Ensure pre-commit is installed:

```bash
pip install pre-commit
pre-commit install
```

### Import Errors

If you get import errors, ensure the package is installed:

```bash
pip install -e .
```

## Next Steps

1. **Read the Standards**: Review `CODING_STANDARDS.md` and `AI_PROMPT_STANDARDS.md`
2. **Configure Your IDE**: Set up your editor to use the standards
3. **Set Up CI/CD**: Add linting and testing to your CI pipeline
4. **Train Your Team**: Share the standards with your development team

## Support

For issues or questions:
- Open an issue on GitHub
- Check the documentation in the repository
- Review the examples in the `examples/` directory

