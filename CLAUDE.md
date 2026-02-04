# Claude Code Standards

This project follows strict coding standards. When working on this codebase, adhere to these guidelines.

## Function Standards

- **Maximum 50 lines** per function (prefer 30 or fewer)
- **Maximum 5 parameters** per function (prefer 3 or fewer)
- **Maximum cyclomatic complexity of 10** (prefer 5 or lower)
- **Maximum 3 levels of nesting** (prefer 2 or fewer)
- Use early returns to reduce nesting and complexity

## Documentation Standards

- All public functions require **Google-style docstrings**
- Include `Args`, `Returns`, and `Raises` sections
- **Type hints required** for all function parameters and returns
- Use `Optional[T]` instead of `Union[T, None]`
- Comments should explain "why", not "what"

## Naming Conventions

- Variables and functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: `_leading_underscore`
- Boolean variables: use `is_`, `has_`, `can_`, `should_` prefixes

## Error Handling

- Catch specific exceptions, never use bare `except:`
- Never silently swallow exceptions with `pass`
- Create custom exception classes for domain-specific errors
- Log errors at appropriate levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Provide specific, actionable error messages

## Testing Standards

- Target **80%+ code coverage**
- Use **Arrange-Act-Assert (AAA)** pattern
- Name tests as: `test_function_scenario_expected_result()`
- Mock external dependencies (APIs, databases, file system)
- Test edge cases and error conditions

## Code Organization

- Maximum 500 lines per file (prefer 300 or fewer)
- Import order: standard library, third-party, local application
- Keep business logic separate from I/O operations
- Use dependency injection for testability

## Example

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

## Commit Standards

- Write clear, concise commit messages
- Use imperative mood ("Add feature" not "Added feature")
- Reference issue numbers when applicable
