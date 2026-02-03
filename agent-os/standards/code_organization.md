# Code Organization Standards

All code MUST follow these organization patterns:

## Module Structure

```
src/
├── __init__.py
├── core/           # Core business logic
│   ├── __init__.py
│   ├── models.py
│   └── services.py
├── api/            # API layer
│   ├── __init__.py
│   └── routes.py
├── utils/          # Shared utilities
│   ├── __init__.py
│   └── helpers.py
└── config/         # Configuration
    ├── __init__.py
    └── settings.py
```

## Import Organization

Order imports in this sequence:
1. Standard library imports
2. Third-party imports
3. Local application imports

```python
# Standard library
import os
import sys
from pathlib import Path
from typing import List, Dict, Optional

# Third-party
import boto3
import requests
from pydantic import BaseModel

# Local application
from src.core.models import User
from src.utils.helpers import format_date
```

## File Size Limits

- **Maximum**: 500 lines per file
- **Preferred**: 300 lines or fewer
- Split large files into logical modules

## Class Organization

```python
class UserService:
    """Service for user operations."""

    # Class constants
    MAX_LOGIN_ATTEMPTS = 3

    # Initialization
    def __init__(self, db: Database):
        self._db = db
        self._cache = {}

    # Public methods (alphabetical)
    def create_user(self, data: UserCreate) -> User:
        """Create a new user."""
        pass

    def get_user(self, user_id: str) -> User:
        """Get user by ID."""
        pass

    # Private methods (alphabetical)
    def _validate_email(self, email: str) -> bool:
        """Validate email format."""
        pass
```

## Separation of Concerns

- Keep business logic separate from I/O
- Use dependency injection
- Avoid circular imports
