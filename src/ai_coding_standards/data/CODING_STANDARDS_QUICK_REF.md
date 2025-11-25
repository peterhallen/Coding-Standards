# Coding Standards - Quick Reference

> One-page reference guide for coding standards. See `CODING_STANDARDS.md` for full documentation.

## Function Limits

| Metric | Maximum | Preferred |
|--------|---------|-----------|
| Function length | 50 lines | 30 lines |
| Function parameters | 5 | 3 |
| Cyclomatic complexity | 10 | 5 |
| Nesting depth | 3 levels | 2 levels |
| Class length | 300 lines | - |
| Module length | 500 lines | - |
| Line length | 120 chars (hard) | 100 chars (soft) |

## Naming Conventions

| Type | Style | Example |
|------|-------|---------|
| Functions | `snake_case` | `calculate_total_cost()` |
| Variables | `snake_case` | `user_account_id` |
| Classes | `PascalCase` | `SecurityAssessment` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES` |
| Private | `_leading_underscore` | `_internal_method()` |
| Boolean | `is_`, `has_`, `can_` | `is_active`, `has_permission` |

## Documentation Requirements

- ✅ **All public functions** require docstrings (Google-style)
- ✅ **Type hints** required for all function parameters and returns
- ✅ **Module docstrings** for all modules
- ✅ **Class docstrings** for all classes
- ❌ **No obvious comments** - code should be self-documenting

## Code Organization

```
module/
├── Module docstring
├── Standard library imports
├── Third-party imports
├── Local imports
├── Constants
├── Classes (public → private)
├── Functions (public → private)
└── if __name__ == "__main__"
```

## Error Handling

- ✅ Catch **specific exceptions**, not bare `except:`
- ✅ **Fail fast** - validate inputs early
- ✅ **Provide context** in error messages
- ✅ Use **custom exceptions** for domain errors
- ❌ **Don't suppress** exceptions silently

## Type Hints

```python
from typing import List, Dict, Optional, Union

def process_data(
    items: List[str],
    config: Optional[Dict] = None
) -> Dict[str, int]:
    """Process items and return results."""
    pass
```

## Import Organization

```python
# 1. Standard library
import json
from datetime import datetime

# 2. Third-party
import boto3
from botocore.exceptions import ClientError

# 3. Local
from .config import load_config
```

## Performance Guidelines

- ✅ **Measure first** - profile before optimizing
- ✅ Use **appropriate data structures** (set for membership, dict for lookups)
- ✅ **Cache** expensive computations
- ✅ Use **async/await** for I/O-bound operations
- ❌ **Avoid premature optimization**

## Testing Standards

- ✅ **80%+ coverage** target
- ✅ **Arrange-Act-Assert** pattern
- ✅ **Descriptive test names**: `test_function_scenario_expected_result()`
- ✅ **Mock external dependencies**
- ✅ Test **edge cases** and **error conditions**

## AI Coder Checklist

When generating code, always:
- [ ] Include docstrings for all public functions
- [ ] Use type hints consistently
- [ ] Follow existing code patterns
- [ ] Keep functions ≤50 lines
- [ ] Handle errors appropriately
- [ ] Use meaningful variable names
- [ ] Document complex logic

## Common Patterns

### Early Returns (Reduce Nesting)
```python
# Good
def process(data):
    if not data:
        return []
    if not validate(data):
        return []
    return transform(data)
```

### Dataclasses for Many Parameters
```python
# Good
@dataclass
class Config:
    account_id: str
    regions: List[str]
    timeout: int = 30

def process(config: Config):
    pass
```

### List Comprehensions
```python
# Simple transformations
squared = [x**2 for x in range(10) if x % 2 == 0]

# Complex logic - use loop
results = []
for item in data:
    if complex_condition(item):
        results.append(process(item))
```

## Code Review Checklist

- [ ] Functions ≤50 lines, complexity ≤10
- [ ] All public functions have docstrings
- [ ] Type hints present and correct
- [ ] Error handling appropriate
- [ ] No security vulnerabilities
- [ ] Tests included for new code
- [ ] Follows naming conventions
- [ ] No code duplication
- [ ] Imports organized correctly

---

**Full Documentation**: See `CODING_STANDARDS.md` for comprehensive guidelines.


