# Code Compliance Guide

This guide helps you bring existing code (legacy code, imported code, or new codebases) into compliance with the Coding Standards.

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Step-by-Step Compliance Process](#step-by-step-compliance-process)
4. [Migration Strategies](#migration-strategies)
5. [Tools and Automation](#tools-and-automation)
6. [Common Scenarios](#common-scenarios)
7. [Compliance Checklist](#compliance-checklist)
8. [Getting Help](#getting-help)

---

## Overview

When bringing code into compliance, we follow a systematic approach:

1. **Assess** - Identify non-compliant code
2. **Prioritize** - Determine what to fix first
3. **Automate** - Use tools to fix what can be automated
4. **Refactor** - Manually fix complex issues
5. **Verify** - Ensure code still works and meets standards

## Quick Start

### Automated Compliance Check

Use the CLI tool to check compliance:

```bash
# Check code compliance
coding-standards check-compliance /path/to/code

# Check with detailed report
coding-standards check-compliance /path/to/code --detailed

# Generate compliance report
coding-standards check-compliance /path/to/code --report compliance_report.html
```

### Automated Fixes

Many issues can be fixed automatically:

```bash
# Format code (Black)
black .

# Sort imports (isort)
isort .

# These fix:
# - Code formatting
# - Import organization
# - Line length (where possible)
# - Trailing whitespace
```

## Step-by-Step Compliance Process

### Step 1: Initial Assessment

Run compliance check to see what needs fixing:

```bash
# Install compliance checker (if not already installed)
pip install git+https://github.com/peterhallen/coding-standards.git

# Check compliance
coding-standards check-compliance .
```

This will identify:
- Functions exceeding length limits
- Missing type hints
- Missing docstrings
- High complexity functions
- Deep nesting
- Naming convention violations

### Step 2: Automated Fixes

Start with what can be automated:

```bash
# 1. Format code
black .

# 2. Sort imports
isort .

# 3. Fix basic linting issues
autopep8 --in-place --aggressive --aggressive .

# 4. Run pre-commit hooks (if set up)
pre-commit run --all-files
```

### Step 3: Add Type Hints

Use tools to help add type hints:

```bash
# Install type annotation tools
pip install monkeytype

# Generate type hints from runtime data
monkeytype run your_script.py
monkeytype apply your_module.YourClass

# Or use mypy to identify missing types
mypy --strict your_module.py
```

**Manual approach:**
1. Start with function signatures
2. Add return types
3. Add parameter types
4. Use `Any` for complex types initially, refine later

### Step 4: Add Documentation

Add docstrings systematically:

1. **Start with public functions** - Highest priority
2. **Add class docstrings** - Describe purpose and usage
3. **Add module docstrings** - Describe module purpose
4. **Add private function docstrings** - If logic is complex

**Template:**
```python
def function_name(param1: Type, param2: Type) -> ReturnType:
    """Brief description of what the function does.

    More detailed description if needed. Explain the purpose,
    behavior, and any important details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ExceptionType: When this exception is raised

    Example:
        >>> result = function_name("value1", "value2")
        >>> print(result)
        'expected_output'
    """
    pass
```

### Step 5: Refactor Complex Functions

For functions that exceed limits:

#### Functions Too Long (>50 lines)

**Strategy: Extract Helper Functions**

```python
# Before (60 lines)
def process_user_data(user_data: Dict) -> Dict:
    # Validation (10 lines)
    if not user_data:
        raise ValueError("...")
    # ... more validation

    # Transformation (20 lines)
    transformed = {}
    # ... transformation logic

    # Database operations (20 lines)
    # ... database logic

    # Response formatting (10 lines)
    # ... formatting logic

    return result

# After (split into helpers)
def process_user_data(user_data: Dict) -> Dict:
    """Process user data through validation, transformation, and storage."""
    validated = _validate_user_data(user_data)
    transformed = _transform_user_data(validated)
    stored = _store_user_data(transformed)
    return _format_response(stored)

def _validate_user_data(user_data: Dict) -> Dict:
    """Validate user data."""
    # Validation logic
    pass

def _transform_user_data(user_data: Dict) -> Dict:
    """Transform user data."""
    # Transformation logic
    pass

# ... etc
```

#### Too Many Parameters (>5)

**Strategy: Use Dataclasses**

```python
# Before
def create_user(name, email, age, address, phone, role, department):
    pass

# After
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    email: str
    age: int
    address: str
    phone: str
    role: str
    department: str

def create_user(user_data: UserData) -> User:
    """Create a new user from user data."""
    pass
```

#### High Complexity (>10)

**Strategy: Simplify Logic**

```python
# Before (complex nested conditions)
def process_user(user):
    if user:
        if user.is_active:
            if user.has_permission:
                if user.subscription_valid:
                    return "process"
                else:
                    return "expired"
            else:
                return "no_permission"
        else:
            return "inactive"
    return "invalid"

# After (early returns, guard clauses)
def process_user(user: User) -> str:
    """Process user based on status and permissions."""
    if not user:
        return "invalid"

    if not user.is_active:
        return "inactive"

    if not user.has_permission:
        return "no_permission"

    if not user.subscription_valid:
        return "expired"

    return "process"
```

#### Deep Nesting (>3 levels)

**Strategy: Early Returns and Extract Functions**

```python
# Before (4 levels of nesting)
def process_data(data):
    if data:
        if len(data) > 0:
            for item in data:
                if item:
                    process(item)

# After (2 levels max)
def process_data(data: List[Dict]) -> None:
    """Process list of data items."""
    if not data:
        return

    for item in data:
        _process_item(item)

def _process_item(item: Dict) -> None:
    """Process a single item."""
    if not item:
        return
    # Process item
```

### Step 6: Fix Error Handling

Replace broad exception handling:

```python
# Before
try:
    result = risky_operation()
except:
    return None

# After
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise OperationError(f"Failed to perform operation: {e}") from e
except AnotherError as e:
    # Handle differently
    raise
```

### Step 7: Add Tests

Ensure code has adequate test coverage:

```bash
# Check current coverage
pytest --cov --cov-report=html

# Aim for 80%+ coverage
# Add tests for:
# - Public functions
# - Edge cases
# - Error conditions
# - Complex logic
```

### Step 8: Verify Compliance

Run final checks:

```bash
# Format check
black --check .

# Import check
isort --check-only .

# Linting
flake8 .

# Type checking
mypy .

# Complexity check
pylint --disable=all --enable=too-complex,too-many-arguments,too-many-locals .

# Test coverage
pytest --cov --cov-fail-under=80
```

## Migration Strategies

### Strategy 1: Incremental (Recommended)

Fix code as you work on it:

1. **When modifying a file**: Bring it into compliance
2. **When fixing bugs**: Refactor to meet standards
3. **When adding features**: Write new code to standards
4. **Gradually**: Legacy code improves over time

**Pros:**
- Low risk
- Doesn't block feature work
- Natural refactoring

**Cons:**
- Takes time
- Codebase has mixed compliance

### Strategy 2: File-by-File

Systematically fix files one at a time:

1. **Prioritize**: Start with most-used files
2. **Fix completely**: Bring entire file into compliance
3. **Test thoroughly**: Ensure nothing breaks
4. **Commit**: Commit compliance fixes separately

**Pros:**
- Complete compliance per file
- Clear progress
- Easier to review

**Cons:**
- Time-consuming
- May delay feature work

### Strategy 3: Module-by-Module

Fix entire modules at once:

1. **Identify modules**: Group related files
2. **Fix module**: Bring all files into compliance
3. **Test module**: Ensure module works correctly
4. **Document**: Note any module-specific patterns

**Pros:**
- Consistent within modules
- Good for team coordination
- Clear boundaries

**Cons:**
- Requires planning
- May need module-wide changes

### Strategy 4: New Code Only

Only enforce standards on new code:

1. **Mark legacy**: Add comments or documentation
2. **New code**: Strictly follow standards
3. **Gradual**: Fix legacy when touching it

**Pros:**
- Fast to implement
- No risk to existing code
- Standards improve over time

**Cons:**
- Mixed codebase
- Harder to maintain

## Tools and Automation

### Automated Tools

```bash
# Code formatting
black .

# Import sorting
isort .

# Basic linting fixes
autopep8 --in-place --aggressive .

# Type checking (identifies missing types)
mypy --strict .

# Complexity analysis
pylint --disable=all --enable=too-complex .
```

### Custom Scripts

Create scripts for common tasks:

```python
# scripts/add_type_hints.py
# Script to help add type hints to functions

# scripts/add_docstrings.py
# Script to generate docstring templates

# scripts/check_compliance.py
# Custom compliance checker
```

### Pre-commit Hooks

Set up pre-commit to prevent new violations:

```bash
pre-commit install
```

This runs checks before each commit.

## Common Scenarios

### Scenario 1: Importing External Library

**Challenge**: External code doesn't follow our standards

**Solution**:
1. Wrap external code in adapter layer
2. Your code follows standards
3. Document any deviations

### Scenario 2: Legacy Codebase

**Challenge**: Large codebase with many violations

**Solution**:
1. Use incremental strategy
2. Fix as you touch code
3. Prioritize high-traffic areas
4. Document exceptions

### Scenario 3: Third-Party Code

**Challenge**: Can't modify third-party code

**Solution**:
1. Use type stubs for type hints
2. Wrap in compliant interfaces
3. Document usage patterns

### Scenario 4: Rapid Prototyping

**Challenge**: Need to move fast, standards slow you down

**Solution**:
1. Prototype quickly
2. Refactor before merging
3. Use `# TODO: Refactor` comments
4. Schedule refactoring time

## Compliance Checklist

Use this checklist when bringing code into compliance:

### Formatting
- [ ] Code formatted with Black
- [ ] Imports sorted with isort
- [ ] No trailing whitespace
- [ ] Consistent line endings (LF)

### Documentation
- [ ] All public functions have docstrings
- [ ] All classes have docstrings
- [ ] Module has docstring
- [ ] Docstrings are Google-style
- [ ] Complex logic has comments

### Type Hints
- [ ] All function parameters have types
- [ ] All functions have return types
- [ ] Complex types use `typing` module
- [ ] No `Any` types (or justified)

### Function Quality
- [ ] Functions ≤ 50 lines
- [ ] Functions ≤ 5 parameters
- [ ] Complexity ≤ 10
- [ ] Nesting ≤ 3 levels

### Error Handling
- [ ] Specific exceptions caught
- [ ] Error messages provide context
- [ ] Custom exceptions for domain errors
- [ ] No bare `except:`

### Testing
- [ ] Tests for public functions
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] Coverage ≥ 80%

### Code Quality
- [ ] Follows naming conventions
- [ ] No code duplication
- [ ] Single responsibility
- [ ] Appropriate data structures

## Getting Help

### Resources

- **Standards Documentation**: `CODING_STANDARDS.md`
- **Quick Reference**: `CODING_STANDARDS_QUICK_REF.md`
- **Examples**: `examples/good_example.py`
- **CLI Tool**: `ai-coding-standards check-compliance`

### Team Support

- Ask for code review
- Pair program on complex refactoring
- Share compliance strategies
- Document exceptions

---

**Remember**: Compliance is a journey, not a destination. Focus on continuous improvement!

---

**Last Updated**: 2025-12-08
**Version**: 1.0.0
