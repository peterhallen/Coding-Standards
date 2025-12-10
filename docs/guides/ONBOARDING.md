# Developer Onboarding Guide

Welcome! This guide gets you set up with the AI Coding Standards in 5 minutes.

## Table of Contents

1. [Quick Setup](#quick-setup)
2. [Key Standards to Know](#key-standards-to-know)
3. [Daily Workflow](#daily-workflow)
4. [IDE Setup](#ide-setup)
5. [Documentation](#documentation)
6. [Checklist](#checklist)
7. [Common Questions](#common-questions)

---

## Quick Setup

### 1. Install Python & Package

Follow [INSTALLATION.md](INSTALLATION.md) for your OS (Windows, macOS, or Linux).

**TL;DR** (if Python is already installed):

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\Activate.ps1  # Windows

# Install package
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

### 2. Set Up Your Project

```bash
cd your-project
ai-coding-standards install --cursor --docs --pre-commit
```

### 3. Install Dev Tools

```bash
pip install black isort mypy flake8 pylint pytest pytest-cov pre-commit
```

### 4. Verify Setup

```bash
black --version
isort --version
flake8 --version
mypy --version
```

---

## Key Standards to Know

### Function Limits

| Metric | Maximum | Preferred |
|--------|---------|-----------|
| Lines per function | 50 | 30 |
| Parameters | 5 | 3 |
| Complexity | 10 | 5 |
| Nesting depth | 3 | 2 |

### Naming Conventions

- **Functions/variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Booleans**: `is_`, `has_`, `can_` prefixes

### Documentation

- All public functions need docstrings (Google-style)
- All functions need type hints

**Example:**

```python
def process_user(user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Process user data and return results.
    
    Args:
        user_id: Unique identifier for the user
        data: Dictionary containing user data
    
    Returns:
        Dictionary with processed results
    
    Raises:
        ValueError: If user_id is empty
    """
    if not user_id:
        raise ValueError("user_id cannot be empty")
    return {"status": "processed", "user_id": user_id}
```

---

## Daily Workflow

### While Coding

```bash
# Format as you go
black .
isort .

# Check specific files
mypy your_file.py
flake8 your_file.py
```

### Before Committing

```bash
black .           # Format
isort .           # Sort imports
flake8 .          # Lint
mypy .            # Type check
pytest --cov      # Test
```

> **Tip**: If pre-commit hooks are installed, this runs automatically.

---

## IDE Setup

### Cursor (Recommended)

If you ran `ai-coding-standards install --cursor`:
1. Open your project in Cursor
2. Done! Cursor reads `.cursorrules` automatically

### VS Code

Install extensions:
- Python
- Black Formatter
- Pylint

### PyCharm

1. Settings → Editor → Code Style
2. Import from `.editorconfig`

---

## Documentation

| Document | Purpose |
|----------|---------|
| [CODING_STANDARDS_QUICK_REF.md](CODING_STANDARDS_QUICK_REF.md) | One-page cheat sheet |
| [CODING_STANDARDS.md](CODING_STANDARDS.md) | Full standards |
| [AI_PROMPT_STANDARDS.md](AI_PROMPT_STANDARDS.md) | Writing prompts for AI |
| [CURSOR_SETUP.md](CURSOR_SETUP.md) | Cursor IDE details |
| [CODE_COMPLIANCE.md](CODE_COMPLIANCE.md) | Fixing legacy code |

---

## Checklist

- [ ] Python & virtual environment set up
- [ ] Package installed
- [ ] Standards installed in project
- [ ] Dev tools installed (black, isort, etc.)
- [ ] IDE configured
- [ ] Read quick reference guide
- [ ] Pre-commit hooks working

---

## Common Questions

**Q: Function is 55 lines, what do I do?**  
A: Extract helper functions for logical sections.

**Q: Need 6+ parameters?**  
A: Use a dataclass or TypedDict to group them.

**Q: Do private functions need docstrings?**  
A: Only if the logic is non-obvious.

---

**Questions?** Check the documentation above or ask your team lead.

---

**Last Updated**: 2025-12-08  
**Version**: 1.0.0
