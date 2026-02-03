# Naming Conventions

All code MUST follow these naming standards:

## Python Naming

| Type | Convention | Example |
|------|------------|---------|
| Variables | snake_case | `user_count`, `total_amount` |
| Functions | snake_case | `calculate_total()`, `get_user()` |
| Classes | PascalCase | `UserAccount`, `DataProcessor` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES`, `API_TIMEOUT` |
| Private | Leading underscore | `_internal_method()`, `_cache` |
| Module | snake_case | `data_processor.py` |

## Naming Guidelines

### Be Descriptive
```python
# Good
user_authentication_token = get_token()
total_monthly_revenue = calculate_revenue()

# Bad
x = get_token()
tmr = calculate_revenue()
```

### Use Meaningful Prefixes
```python
# Booleans: is_, has_, can_, should_
is_authenticated = True
has_permission = check_permission()
can_edit = user.role == "admin"

# Counts: num_, count_, total_
num_retries = 3
total_users = len(users)
```

### Avoid Abbreviations
```python
# Good
customer_address = get_address()
maximum_connections = 100

# Bad
cust_addr = get_address()
max_conn = 100
```

## File Naming

- Use snake_case for Python files: `user_service.py`
- Use snake_case for test files: `test_user_service.py`
- Group related files in packages with `__init__.py`
