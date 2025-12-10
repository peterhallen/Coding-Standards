# Installation Guide

Choose your operating system for step-by-step installation instructions.

## Table of Contents

- [Windows](#windows)
- [macOS](#macos)
- [Linux / WSL](#linux--wsl)
- [After Installation](#after-installation)
- [Troubleshooting](#troubleshooting)

---

## Windows

### Step 1: Install Python

**Option A: Download from python.org (Recommended)**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11 or 3.12
3. Run the installer
4. ⚠️ **IMPORTANT**: Check ✅ "Add Python to PATH" at the bottom of the installer
5. Click "Install Now"

**Option B: Using winget (Windows Package Manager)**

Open PowerShell and run:

```powershell
winget install Python.Python.3.12
```

### Step 2: Verify Python Installation

Open a **new** PowerShell window and run:

```powershell
python --version
pip --version
```

You should see version numbers. If not, try one of these:

**Option A**: Restart your computer (simplest)

**Option B**: Refresh PATH in current terminal:
```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```

### Step 3: Set Execution Policy (Required Once)

PowerShell blocks scripts by default. Run this once to allow virtual environment activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

### Step 4: Create a Virtual Environment

Navigate to your project folder:

```powershell
cd C:\path\to\your\project

# Remove any existing venv (if retrying)
Remove-Item -Recurse -Force .venv -ErrorAction SilentlyContinue

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

You should see `(.venv)` appear at the start of your prompt.

### Step 5: Install the Package

```powershell
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

### Step 6: Install Standards in Your Project

```powershell
ai-coding-standards install --cursor --docs --pre-commit
```

### Step 7: Install Development Tools

```powershell
pip install black isort mypy flake8 pylint pytest pytest-cov pre-commit
```

---

## macOS

### Step 1: Install Python

**Option A: Using Homebrew (Recommended)**

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.12
```

**Option B: Download from python.org**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the macOS installer
3. Run and follow the installation steps

### Step 2: Verify Python Installation

```bash
python3 --version
pip3 --version
```

### Step 3: Create a Virtual Environment

```bash
cd /path/to/your/project

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```

### Step 4: Install the Package

```bash
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

### Step 5: Install Standards in Your Project

```bash
ai-coding-standards install --cursor --docs --pre-commit
```

### Step 6: Install Development Tools

```bash
pip install black isort mypy flake8 pylint pytest pytest-cov pre-commit
```

---

## Linux / WSL

### Step 1: Install Python

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv python3-full
```

**Fedora:**

```bash
sudo dnf install python3 python3-pip
```

**Arch Linux:**

```bash
sudo pacman -S python python-pip
```

### Step 2: Verify Python Installation

```bash
python3 --version
pip3 --version
```

### Step 3: Create a Virtual Environment

> **Required on Ubuntu 23.04+ / Debian 12+**: Modern systems require virtual environments (PEP 668).

```bash
cd /path/to/your/project

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate
```

### Step 4: Install the Package

```bash
pip install git+https://github.com/peterhallen/AI-coding-standards.git
```

### Step 5: Install Standards in Your Project

```bash
ai-coding-standards install --cursor --docs --pre-commit
```

### Step 6: Install Development Tools

```bash
pip install black isort mypy flake8 pylint pytest pytest-cov pre-commit
```

---

## After Installation

### What Gets Installed

The `ai-coding-standards install` command creates these files in your project:

| File | Purpose |
|------|---------|
| `.editorconfig` | Editor settings (indentation, line endings) |
| `.flake8` | Flake8 linter configuration |
| `.pylintrc` | Pylint configuration |
| `pyproject.toml` | Black, isort, mypy, pytest settings |
| `.pre-commit-config.yaml` | Pre-commit hooks |
| `.cursorrules` | Cursor IDE rules |
| `.cursor/rules/*.mdc` | Detailed Cursor rules (with `--cursor`) |
| `.antigravity/rules/*.mdc` | Detailed Antigravity rules (with `--antigravity`) |
| `docs/standards/*.md` | Documentation files (with `--docs`) |

### Verify Installation

**Windows (PowerShell):**

```powershell
ai-coding-standards info
Get-ChildItem .editorconfig, .flake8, .pylintrc, pyproject.toml -Force
```

**macOS/Linux:**

```bash
ai-coding-standards info
ls -la .editorconfig .flake8 .pylintrc pyproject.toml
```

### Test the Tools

```bash
# Format code
black --check .

# Sort imports
isort --check-only .

# Lint
flake8 .

# Type check
mypy .
```

---

## CLI Reference

```bash
# Show package info
ai-coding-standards info

# Install standards (basic)
ai-coding-standards install

# Install with all options
ai-coding-standards install --overwrite --docs --pre-commit --cursor

# Install to specific directory
ai-coding-standards install /path/to/project

# Check compliance
ai-coding-standards check-compliance

# Auto-fix issues
ai-coding-standards fix-compliance
```

### Install Options

| Option | Description |
|--------|-------------|
| `--overwrite` | Replace existing config files |
| `--no-interactive` | Don't prompt for confirmation |
| `--docs` | Install documentation to `docs/standards/` |
| `--pre-commit` | Set up pre-commit hooks |
| `--cursor` | Install Cursor IDE rules |
| `--antigravity` | Install Antigravity IDE rules |

---

## Troubleshooting

### Windows: "python is not recognized"

Python is not in your PATH. Solutions:

1. **Reinstall Python** and check "Add Python to PATH"
2. **Or use the py launcher**: `py -m pip install ...`
3. **Or add Python to PATH manually**:
   - Search "Environment Variables" in Start Menu
   - Edit PATH and add: `C:\Users\YourName\AppData\Local\Programs\Python\Python312\`

### Windows: "Execution policy" error

Run this in PowerShell as Administrator:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Linux: "externally-managed-environment" error

Modern Debian/Ubuntu requires virtual environments. Always use:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### macOS: "command not found: pip"

Use `pip3` instead of `pip`:

```bash
pip3 install git+https://github.com/peterhallen/AI-coding-standards.git
```

### All Systems: Permission denied

Install with `--user` flag:

```bash
pip install --user git+https://github.com/peterhallen/AI-coding-standards.git
```

### Git not installed

Install Git first:

- **Windows**: [git-scm.com](https://git-scm.com/download/win)
- **macOS**: `brew install git` or `xcode-select --install`
- **Linux**: `sudo apt install git`

---

## Next Steps

1. **Read the standards**: [CODING_STANDARDS_QUICK_REF.md](CODING_STANDARDS_QUICK_REF.md)
2. **Set up your IDE**: [CURSOR_SETUP.md](CURSOR_SETUP.md)
3. **New to the team?**: [ONBOARDING.md](ONBOARDING.md)

---

**Last Updated**: 2025-12-08  
**Version**: 1.0.0