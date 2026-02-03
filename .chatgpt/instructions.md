# ChatGPT Coding Standards Instructions

Copy and paste these instructions into ChatGPT's Custom Instructions to ensure consistent code quality.

---

## Custom Instructions for ChatGPT

When helping with code, follow these standards:

### Function Standards
- Maximum 50 lines per function (prefer 30 or fewer)
- Maximum 5 parameters (prefer 3 or fewer)
- Maximum cyclomatic complexity of 10 (prefer 5 or lower)
- Maximum 3 levels of nesting (prefer 2)
- Use early returns to reduce nesting

### Documentation
- All public functions need Google-style docstrings with Args, Returns, and Raises sections
- Include type hints for all function parameters and return values
- Comments should explain "why", not "what"

### Naming Conventions
- Variables and functions: snake_case
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE
- Private members: _leading_underscore
- Boolean variables: is_, has_, can_, should_ prefixes

### Error Handling
- Catch specific exceptions, not bare `except:`
- Never silently swallow exceptions
- Use custom exception classes for domain errors
- Log errors with appropriate levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)

### Testing
- Target 80%+ code coverage
- Use Arrange-Act-Assert pattern
- Name tests: test_function_scenario_expected_result()
- Mock external dependencies

### Code Organization
- Maximum 500 lines per file (prefer 300)
- Import order: standard library, third-party, local
- Keep business logic separate from I/O
- Use dependency injection

### Example Good Code
```python
def calculate_total_cost(
    usage_hours: float,
    rate_per_hour: float,
    discount: float = 0.0
) -> float:
    """Calculate total cost based on usage and rate.

    Args:
        usage_hours: Number of hours used
        rate_per_hour: Cost per hour
        discount: Optional discount percentage (0.0 to 1.0)

    Returns:
        Total cost after applying discount

    Raises:
        ValueError: If any parameter is negative or discount > 1.0
    """
    if usage_hours < 0 or rate_per_hour < 0:
        raise ValueError("Hours and rate must be non-negative")
    if not 0.0 <= discount <= 1.0:
        raise ValueError("Discount must be between 0.0 and 1.0")

    subtotal = usage_hours * rate_per_hour
    return subtotal * (1 - discount)
```
