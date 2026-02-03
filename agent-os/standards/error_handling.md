# Error Handling Standards

All code MUST follow these error handling patterns:

## Exception Handling

### Catch Specific Exceptions
```python
# Good
try:
    result = api_client.fetch_data()
except ConnectionError as e:
    logger.error(f"Network error: {e}")
    raise
except TimeoutError as e:
    logger.error(f"Request timed out: {e}")
    return None

# Bad
try:
    result = api_client.fetch_data()
except Exception:
    pass  # Never silently swallow exceptions
```

### Use Custom Exceptions
```python
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

class ResourceNotFoundError(Exception):
    """Raised when a requested resource doesn't exist."""
    pass

def get_user(user_id: str) -> User:
    user = db.find_user(user_id)
    if not user:
        raise ResourceNotFoundError(f"User {user_id} not found")
    return user
```

## Logging

### Log at Appropriate Levels
```python
import logging

logger = logging.getLogger(__name__)

# DEBUG: Detailed diagnostic information
logger.debug(f"Processing item {item_id}")

# INFO: General operational events
logger.info(f"User {user_id} logged in successfully")

# WARNING: Something unexpected but recoverable
logger.warning(f"Rate limit approaching: {current_rate}/{max_rate}")

# ERROR: Something failed
logger.error(f"Failed to process payment: {error}")

# CRITICAL: System is unusable
logger.critical(f"Database connection lost: {error}")
```

## Error Messages

### Be Specific and Actionable
```python
# Good
raise ValueError(
    f"Invalid discount value: {discount}. "
    f"Must be between 0.0 and 1.0"
)

# Bad
raise ValueError("Invalid value")
```

## Return Values vs Exceptions

- Use exceptions for exceptional conditions
- Use return values for expected outcomes
- Never use exceptions for flow control

```python
# Good - return None for "not found" cases
def find_user(user_id: str) -> Optional[User]:
    return db.query(User).filter_by(id=user_id).first()

# Good - raise exception for invalid input
def get_user(user_id: str) -> User:
    if not user_id:
        raise ValueError("user_id cannot be empty")
    user = find_user(user_id)
    if not user:
        raise ResourceNotFoundError(f"User {user_id} not found")
    return user
```
