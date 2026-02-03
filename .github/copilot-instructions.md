# GitHub Copilot Instructions

These coding standards guide GitHub Copilot's suggestions for this project.

## Function Standards

- Maximum 50 lines per function, prefer 30 or fewer
- Maximum 5 parameters per function, prefer 3 or fewer
- Maximum cyclomatic complexity of 10, prefer 5 or lower
- Maximum 3 levels of nesting, prefer 2 or fewer
- Use early returns to reduce nesting and complexity

## Documentation Standards

- All public functions require Google-style docstrings
- Include Args, Returns, and Raises sections in docstrings
- Type hints are required for all function parameters and returns
- Use `Optional[T]` instead of `Union[T, None]`
- Comments should explain "why", not "what"

## Naming Conventions

- Variables and functions: snake_case (e.g., `user_count`, `get_user()`)
- Classes: PascalCase (e.g., `UserAccount`, `DataProcessor`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_RETRIES`, `API_TIMEOUT`)
- Private members: _leading_underscore (e.g., `_internal_method()`)
- Boolean variables: use is_, has_, can_, should_ prefixes

## Error Handling

- Catch specific exceptions, never use bare `except:`
- Never silently swallow exceptions with `pass`
- Create custom exception classes for domain-specific errors
- Log errors at appropriate levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Provide specific, actionable error messages

## Testing Standards

- Target 80%+ code coverage
- Use Arrange-Act-Assert (AAA) pattern
- Name tests as: test_function_scenario_expected_result()
- Mock external dependencies (APIs, databases, file system)
- Test edge cases and error conditions

## Code Organization

- Maximum 500 lines per file, prefer 300 or fewer
- Import order: standard library, third-party, local application
- Keep business logic separate from I/O operations
- Use dependency injection for testability
- Avoid circular imports

## Python-Specific

```python
# Good example
def process_user_data(
    user_id: str,
    data: Dict[str, Any],
    validate: bool = True
) -> ProcessingResult:
    """Process user data with optional validation.

    Args:
        user_id: Unique identifier for the user
        data: Dictionary containing user data to process
        validate: Whether to validate data before processing

    Returns:
        ProcessingResult with status and processed data

    Raises:
        ValidationError: If validate=True and data is invalid
        UserNotFoundError: If user_id doesn't exist
    """
    if not user_id:
        raise ValueError("user_id cannot be empty")

    if validate:
        _validate_user_data(data)

    user = _get_user(user_id)
    return _process_data(user, data)
```

## JavaScript/TypeScript-Specific

- Use TypeScript for type safety when possible
- Prefer `const` over `let`, avoid `var`
- Use async/await over raw Promises
- Use optional chaining (`?.`) and nullish coalescing (`??`)

## Testing Example

```python
def test_process_user_data_with_valid_input():
    """Test successful data processing with valid input."""
    # Arrange
    user_id = "user123"
    data = {"name": "Test User", "email": "test@example.com"}
    mock_user = Mock(id=user_id)

    # Act
    with patch("module._get_user", return_value=mock_user):
        result = process_user_data(user_id, data)

    # Assert
    assert result.status == "success"
    assert result.user_id == user_id
```
