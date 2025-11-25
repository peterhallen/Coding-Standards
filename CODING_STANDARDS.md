# Coding Standards and Best Practices

## Table of Contents

1. [Introduction](#introduction)
2. [General Principles](#general-principles)
3. [Code Organization](#code-organization)
4. [Function and Method Guidelines](#function-and-method-guidelines)
5. [Naming Conventions](#naming-conventions)
6. [Documentation Standards](#documentation-standards)
7. [Error Handling](#error-handling)
8. [Performance Best Practices](#performance-best-practices)
9. [Python-Specific Standards](#python-specific-standards)
10. [Testing Standards](#testing-standards)
11. [AI Coder Collaboration Guidelines](#ai-coder-collaboration-guidelines)
12. [Code Review Checklist](#code-review-checklist)

---

## Introduction

### Purpose

This document establishes coding standards and best practices to ensure consistency, readability, maintainability, and performance across all codebases. These standards are designed to be followed by both human developers and AI coding assistants to maintain a uniform code style and quality level.

### Scope

These standards apply to all code written for this organization, with a primary focus on Python development. The guidelines emphasize:

- **Readability**: Code should be self-documenting and easy to understand
- **Maintainability**: Code should be easy to modify and extend
- **Performance**: Code should be efficient without premature optimization
- **Shareability**: Code should be portable and consistent across developers

### Enforcement

While these standards are guidelines, adherence is expected. Automated tooling (linters, formatters) can help enforce many of these rules. Code reviews should verify compliance with these standards.

---

## General Principles

### 1. Readability First

Code is read more often than it is written. Prioritize clarity over cleverness.

**Good:**
```python
def calculate_monthly_cost(usage_hours: float, rate_per_hour: float) -> float:
    """Calculate monthly cost based on usage hours and hourly rate."""
    return usage_hours * rate_per_hour
```

**Bad:**
```python
def calc(u, r): return u*r  # Unclear variable names, no documentation
```

### 2. DRY (Don't Repeat Yourself)

Avoid code duplication. Extract common functionality into reusable functions or classes.

### 3. KISS (Keep It Simple, Stupid)

Prefer simple, straightforward solutions over complex ones. Complexity should only be introduced when necessary.

### 4. YAGNI (You Aren't Gonna Need It)

Don't add functionality until it's actually needed. Avoid over-engineering.

### 5. Single Responsibility Principle

Each function, class, or module should have one clear purpose.

---

## Code Organization

### Module Structure

1. **Module docstring** - Describe the module's purpose
2. **Imports** - Organized by standard library, third-party, local
3. **Constants** - Module-level constants
4. **Classes** - Public classes first, then private
5. **Functions** - Public functions first, then private
6. **Main execution** - `if __name__ == "__main__":` block

**Example:**
```python
"""
Module for AWS security assessment operations.

This module provides functions for analyzing AWS account security
configurations and compliance with CIS benchmarks.
"""

# Standard library imports
import json
from datetime import datetime
from typing import Dict, List

# Third-party imports
import boto3
from botocore.exceptions import ClientError

# Local imports
from .config import load_config
from .utils import format_timestamp

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Classes
class SecurityAssessment:
    """Main class for security assessments."""
    pass

# Functions
def assess_account(account_id: str) -> Dict:
    """Assess security configuration for an account."""
    pass

# Private functions
def _validate_config(config: Dict) -> bool:
    """Validate configuration dictionary."""
    pass
```

### File and Module Limits

- **Maximum module length**: 500 lines
  - If a module exceeds this, consider splitting into multiple modules
  - Group related functionality together

- **Maximum class length**: 300 lines
  - If a class exceeds this, consider composition or splitting into multiple classes

### Directory Structure

Organize code into logical directories:

```
project/
├── src/
│   ├── core/          # Core business logic
│   ├── utils/         # Utility functions
│   ├── config/        # Configuration management
│   └── tests/         # Test files
├── docs/              # Documentation
├── scripts/           # Utility scripts
└── requirements.txt   # Dependencies
```

---

## Function and Method Guidelines

### Function Length

- **Maximum**: 50 lines per function
- **Preferred**: 30 lines or fewer
- **Rationale**: Shorter functions are easier to understand, test, and maintain

If a function exceeds 50 lines, consider:
- Extracting helper functions
- Breaking into smaller, focused functions
- Using composition instead of a single large function

### Function Parameters

- **Maximum**: 5 parameters per function
- **Preferred**: 3 or fewer parameters

For functions requiring more than 5 parameters, use:
- **Dataclasses** (Python 3.7+)
- **TypedDict** for structured dictionaries
- **Configuration objects** for complex setups

**Good:**
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class AssessmentConfig:
    """Configuration for security assessment."""
    account_id: str
    regions: List[str]
    include_cost_analysis: bool = True
    timeout: int = 30
    retry_count: int = 3

def run_assessment(config: AssessmentConfig) -> Dict:
    """Run security assessment with given configuration."""
    pass
```

**Bad:**
```python
def run_assessment(account_id, regions, include_cost, timeout, retry_count, 
                   output_format, verbose, dry_run):
    """Too many parameters - hard to remember order and purpose."""
    pass
```

### Cyclomatic Complexity

- **Maximum**: 10 per function
- **Preferred**: 5 or lower

Cyclomatic complexity measures the number of linearly independent paths through code. High complexity makes code harder to test and understand.

**Reducing complexity:**
- Extract complex conditions into well-named functions
- Use early returns to reduce nesting
- Replace nested conditionals with guard clauses
- Consider strategy pattern for complex branching

**Example:**
```python
# High complexity (bad)
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

# Lower complexity (good)
def process_user(user):
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

### Nesting Depth

- **Maximum**: 3 levels of nesting
- **Preferred**: 2 levels or fewer

Deep nesting makes code hard to follow. Use early returns and extract functions to reduce nesting.

**Good:**
```python
def process_data(data: List[Dict]) -> List[Dict]:
    """Process data with validation."""
    if not data:
        return []
    
    validated = _validate_data(data)
    if not validated:
        return []
    
    return _transform_data(validated)
```

**Bad:**
```python
def process_data(data):
    if data:
        if len(data) > 0:
            validated = []
            for item in data:
                if item:
                    if 'id' in item:
                        validated.append(item)
            if validated:
                return transform(validated)
    return []
```

### Function Return Values

- Functions should have a single, clear return type
- Use `Optional[Type]` or `Union[Type, None]` when a function may return None
- Avoid returning multiple types unless using `Union` with proper type hints
- Prefer returning meaningful values over None when possible

---

## Naming Conventions

### Functions and Variables

- **Style**: `snake_case`
- **Function names**: Use verbs that describe what the function does
- **Variable names**: Use nouns that describe what the variable represents
- **Boolean variables**: Use `is_`, `has_`, `can_`, `should_` prefixes

**Examples:**
```python
# Functions
def calculate_total_cost() -> float:
    pass

def is_user_authenticated(user: User) -> bool:
    pass

def has_permission(user: User, resource: str) -> bool:
    pass

# Variables
user_account_id = "123456789"
is_active = True
has_admin_access = False
monthly_cost = 150.50
```

### Classes

- **Style**: `PascalCase`
- **Names**: Use nouns that describe what the class represents
- **Avoid abbreviations** unless they're widely understood

**Examples:**
```python
class SecurityAssessment:
    pass

class CostAnalyzer:
    pass

class UserAccountManager:
    pass
```

### Constants

- **Style**: `UPPER_SNAKE_CASE`
- **Place**: Module level or class level
- **Use**: For values that don't change during program execution

**Examples:**
```python
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
AWS_REGION_US_EAST_1 = "us-east-1"
```

### Private Members

- **Style**: Leading underscore `_private_method`
- **Use**: For methods, functions, or variables that are internal to a module or class
- **Double underscore**: Avoid `__private` (name mangling) unless necessary

**Examples:**
```python
class SecurityAssessment:
    def __init__(self):
        self._internal_cache = {}
        self._config = self._load_config()
    
    def _load_config(self) -> Dict:
        """Private method - internal implementation detail."""
        pass
    
    def assess_account(self) -> Dict:
        """Public method - part of the API."""
        return self._perform_assessment()
```

### Module Names

- **Style**: `snake_case`
- **Short and descriptive**: `security_assessment.py` not `sec_assess.py`
- **Avoid**: Single letters, abbreviations, generic names like `utils.py` (be more specific)

### Type Variables

- **Style**: `PascalCase` for generic type variables
- **Examples**: `T`, `KeyType`, `ValueType`

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    def get(self) -> T:
        pass
```

---

## Documentation Standards

### Docstrings

All public functions, classes, and modules must have docstrings. Use Google-style docstrings for consistency.

#### Module Docstrings

```python
"""
Module for AWS security assessment operations.

This module provides comprehensive security assessment capabilities including
CIS benchmark compliance checking, threat intelligence analysis, and resource
inventory management.

Example:
    >>> from security_assessment import SecurityAssessment
    >>> assessor = SecurityAssessment()
    >>> results = assessor.assess_account("123456789012")
"""

__version__ = "1.0.0"
__author__ = "Security Team"
```

#### Class Docstrings

```python
class SecurityAssessment:
    """Security assessment tool for AWS accounts.
    
    This class provides methods to assess AWS account security configurations,
    check compliance with CIS benchmarks, and generate detailed reports.
    
    Attributes:
        account_id: AWS account ID being assessed
        regions: List of AWS regions to assess
        config: Configuration dictionary for assessment settings
    
    Example:
        >>> assessor = SecurityAssessment(
        ...     account_id="123456789012",
        ...     regions=["us-east-1", "us-west-2"]
        ... )
        >>> results = assessor.run_full_assessment()
    """
    
    def __init__(self, account_id: str, regions: List[str]):
        """Initialize security assessment.
        
        Args:
            account_id: AWS account ID to assess
            regions: List of AWS regions to include in assessment
        """
        pass
```

#### Function Docstrings

```python
def assess_cis_compliance(
    account_id: str,
    region: str,
    benchmark_version: str = "1.4.0"
) -> Dict[str, Any]:
    """Assess CIS benchmark compliance for an AWS account.
    
    This function checks the specified AWS account against CIS AWS Foundations
    Benchmark requirements and returns a detailed compliance report.
    
    Args:
        account_id: AWS account ID to assess
        region: AWS region to check (e.g., "us-east-1")
        benchmark_version: CIS benchmark version to use. Defaults to "1.4.0".
    
    Returns:
        Dictionary containing compliance results with the following keys:
            - compliant: Boolean indicating overall compliance status
            - checks: List of individual check results
            - score: Compliance score as a float between 0.0 and 1.0
            - timestamp: ISO format timestamp of assessment
    
    Raises:
        ValueError: If account_id or region is invalid
        ClientError: If AWS API call fails
        TimeoutError: If assessment exceeds timeout limit
    
    Example:
        >>> results = assess_cis_compliance(
        ...     account_id="123456789012",
        ...     region="us-east-1"
        ... )
        >>> print(f"Compliance: {results['score']:.2%}")
        Compliance: 85.50%
    """
    pass
```

### Comments

- **Document why, not what**: Code should be self-explanatory
- **Explain complex logic**: If an algorithm or business rule is non-obvious, explain it
- **Avoid obvious comments**: Don't comment what the code clearly shows

**Good:**
```python
# Use binary search because the list is sorted and we need O(log n) performance
index = bisect.bisect_left(sorted_list, target_value)

# AWS API rate limits: 5 requests/second for this endpoint
time.sleep(0.2)  # Ensure we don't exceed rate limit
```

**Bad:**
```python
# Set x to 5
x = 5

# Loop through items
for item in items:
    # Process item
    process(item)
```

### Type Hints

Use type hints for all function parameters and return values. This improves code clarity and enables static type checking.

**Required:**
- All public function signatures
- Class attributes (where applicable)
- Return types for all functions

**Examples:**
```python
from typing import List, Dict, Optional, Union, Any

def process_accounts(
    account_ids: List[str],
    region: str = "us-east-1",
    include_cost: bool = True
) -> Dict[str, Any]:
    """Process multiple AWS accounts."""
    pass

def get_user_by_id(user_id: str) -> Optional[User]:
    """Get user by ID, returns None if not found."""
    pass

def calculate_cost(
    usage: Union[int, float],
    rate: float
) -> float:
    """Calculate cost from usage and rate."""
    pass
```

---

## Error Handling

### Exception Handling Principles

1. **Be specific**: Catch specific exceptions, not bare `except:`
2. **Fail fast**: Validate inputs early and raise exceptions immediately
3. **Provide context**: Include meaningful error messages
4. **Don't suppress**: Only catch exceptions you can handle
5. **Log appropriately**: Log errors at appropriate levels

### Exception Types

Use built-in exceptions when appropriate, or create custom exceptions for domain-specific errors.

**Built-in exceptions:**
- `ValueError`: Invalid value passed to function
- `TypeError`: Wrong type passed to function
- `KeyError`: Missing dictionary key
- `AttributeError`: Missing object attribute
- `FileNotFoundError`: File doesn't exist
- `TimeoutError`: Operation timed out

**Custom exceptions:**
```python
class SecurityAssessmentError(Exception):
    """Base exception for security assessment errors."""
    pass

class InvalidAccountError(SecurityAssessmentError):
    """Raised when account ID is invalid."""
    pass

class AssessmentTimeoutError(SecurityAssessmentError):
    """Raised when assessment exceeds timeout."""
    pass
```

### Error Handling Patterns

**Good:**
```python
def fetch_account_data(account_id: str) -> Dict:
    """Fetch account data from AWS."""
    if not account_id or not account_id.isdigit():
        raise ValueError(f"Invalid account ID: {account_id}")
    
    try:
        sts_client = boto3.client('sts')
        response = sts_client.get_caller_identity()
        return response
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'InvalidClientTokenId':
            raise InvalidAccountError(f"Invalid credentials for account {account_id}") from e
        raise SecurityAssessmentError(f"AWS API error: {error_code}") from e
    except Exception as e:
        raise SecurityAssessmentError(f"Unexpected error: {e}") from e
```

**Bad:**
```python
def fetch_account_data(account_id):
    try:
        # No validation
        sts_client = boto3.client('sts')
        response = sts_client.get_caller_identity()
        return response
    except:  # Too broad, suppresses all errors
        return {}  # Hides the error
```

### Retry Logic

For transient failures, implement retry logic with exponential backoff:

```python
import time
from typing import Callable, TypeVar

T = TypeVar('T')

def retry_with_backoff(
    func: Callable[[], T],
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0
) -> T:
    """Retry function with exponential backoff.
    
    Args:
        func: Function to retry
        max_retries: Maximum number of retry attempts
        initial_delay: Initial delay in seconds
        backoff_factor: Multiplier for delay after each retry
    
    Returns:
        Result of function call
    
    Raises:
        Last exception if all retries fail
    """
    delay = initial_delay
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            return func()
        except (ClientError, TimeoutError) as e:
            last_exception = e
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= backoff_factor
            else:
                raise
    
    raise last_exception
```

---

## Performance Best Practices

### General Principles

1. **Measure first**: Profile code before optimizing
2. **Optimize bottlenecks**: Focus on code that runs frequently or takes significant time
3. **Avoid premature optimization**: Write clear code first, optimize when needed
4. **Use appropriate data structures**: Choose the right tool for the job

### Data Structure Selection

- **Lists**: Use for ordered sequences, when you need indexing
- **Sets**: Use for membership testing, deduplication
- **Dictionaries**: Use for key-value lookups, caching
- **Tuples**: Use for immutable sequences, return multiple values

**Example:**
```python
# Bad: Using list for membership testing (O(n))
if user_id in user_list:  # Slow for large lists
    pass

# Good: Using set for membership testing (O(1))
if user_id in user_set:  # Fast lookup
    pass
```

### Caching

Use caching for expensive computations or API calls:

```python
from functools import lru_cache
from typing import Dict

@lru_cache(maxsize=128)
def expensive_computation(input_value: str) -> Dict:
    """Expensive computation that benefits from caching."""
    # Complex calculation
    return result

# For class methods
class DataProcessor:
    def __init__(self):
        self._cache: Dict[str, Any] = {}
    
    def get_processed_data(self, key: str) -> Any:
        """Get processed data with caching."""
        if key not in self._cache:
            self._cache[key] = self._process_data(key)
        return self._cache[key]
```

### Async Operations

Use async/await for I/O-bound operations:

```python
import asyncio
import aiohttp
from typing import List

async def fetch_account_data(account_id: str) -> Dict:
    """Fetch account data asynchronously."""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/accounts/{account_id}") as response:
            return await response.json()

async def fetch_multiple_accounts(account_ids: List[str]) -> List[Dict]:
    """Fetch multiple accounts concurrently."""
    tasks = [fetch_account_data(account_id) for account_id in account_ids]
    return await asyncio.gather(*tasks)
```

### List Comprehensions vs Loops

Prefer list comprehensions for simple transformations, but use loops for complex logic:

**Good:**
```python
# Simple transformation - use comprehension
squared = [x**2 for x in range(10) if x % 2 == 0]

# Complex logic - use loop
results = []
for item in data:
    processed = complex_processing(item)
    if should_include(processed):
        results.append(processed)
        if len(results) >= limit:
            break
```

### Generator Expressions

Use generators for large datasets to save memory:

```python
# Bad: Creates entire list in memory
large_list = [process(x) for x in huge_dataset]

# Good: Processes one item at a time
large_generator = (process(x) for x in huge_dataset)
for item in large_generator:
    process_item(item)
```

---

## Python-Specific Standards

### PEP 8 Compliance

Follow PEP 8 style guide with the following modifications:

- **Line length**: 100 characters (soft limit), 120 characters (hard limit)
- **Indentation**: 4 spaces (no tabs)
- **Blank lines**: 2 blank lines between top-level definitions, 1 blank line between methods

### Import Organization

Organize imports in this order:

1. Standard library imports
2. Related third-party imports
3. Local application/library imports

Separate each group with a blank line.

```python
# Standard library
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

# Third-party
import boto3
from botocore.exceptions import ClientError

# Local
from .config import load_config
from .utils import format_timestamp
```

### Type Hints

- Use type hints for all function signatures
- Use `typing` module for complex types
- Use `Optional[T]` instead of `Union[T, None]`
- Use `List[T]`, `Dict[K, V]` instead of `list`, `dict` in type hints (Python < 3.9)
- Use built-in types in Python 3.9+: `list[str]`, `dict[str, int]`

```python
from typing import List, Dict, Optional, Union

# Python 3.8 and earlier
def process_items(items: List[str]) -> Dict[str, int]:
    pass

# Python 3.9+
def process_items(items: list[str]) -> dict[str, int]:
    pass
```

### String Formatting

Prefer f-strings (Python 3.6+) for string formatting:

```python
# Good
name = "Alice"
message = f"Hello, {name}!"

# Also acceptable for complex formatting
message = "Hello, {}!".format(name)

# Avoid
message = "Hello, %s!" % name
```

### Exception Handling

- Use specific exception types
- Chain exceptions with `from` when appropriate
- Include context in error messages

```python
try:
    result = risky_operation()
except SpecificError as e:
    raise CustomError(f"Operation failed: {e}") from e
```

### Context Managers

Use context managers for resource management:

```python
# Good
with open('file.txt', 'r') as f:
    content = f.read()

# Also for custom resources
with database_connection() as conn:
    conn.execute(query)
```

### Dataclasses

Use dataclasses for simple data containers (Python 3.7+):

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class AssessmentResult:
    """Result of a security assessment."""
    account_id: str
    score: float
    findings: List[str]
    timestamp: Optional[datetime] = None
    
    def __post_init__(self):
        """Initialize default values after dataclass init."""
        if self.timestamp is None:
            self.timestamp = datetime.now()
```

### Async/Await

- Use `async def` for async functions
- Use `await` for async operations
- Use `asyncio.gather()` for concurrent operations
- Handle async exceptions properly

```python
import asyncio
from typing import List

async def fetch_data(url: str) -> Dict:
    """Fetch data asynchronously."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_multiple(urls: List[str]) -> List[Dict]:
    """Fetch multiple URLs concurrently."""
    tasks = [fetch_data(url) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)
```

---

## Testing Standards

### Test Organization

- Place tests in a `tests/` directory
- Mirror source structure: `tests/core/test_assessment.py` for `src/core/assessment.py`
- Use descriptive test names: `test_assess_account_with_invalid_id_raises_error()`

### Test Coverage

- Aim for 80%+ code coverage
- Focus on critical paths and business logic
- Test edge cases and error conditions
- Don't test implementation details, test behavior

### Test Structure

Use the Arrange-Act-Assert pattern:

```python
import pytest
from unittest.mock import Mock, patch

def test_assess_account_success():
    """Test successful account assessment."""
    # Arrange
    account_id = "123456789012"
    mock_session = Mock()
    expected_result = {"status": "success"}
    
    # Act
    result = assess_account(account_id, session=mock_session)
    
    # Assert
    assert result["status"] == "success"
    assert "account_id" in result
    mock_session.client.assert_called_once()
```

### Test Types

- **Unit tests**: Test individual functions/methods in isolation
- **Integration tests**: Test interactions between components
- **End-to-end tests**: Test complete workflows

### Mocking

Use mocks for external dependencies:

```python
from unittest.mock import Mock, patch, MagicMock

@patch('boto3.client')
def test_fetch_account_data(mock_boto_client):
    """Test fetching account data with mocked AWS client."""
    # Arrange
    mock_sts = Mock()
    mock_sts.get_caller_identity.return_value = {"Account": "123456789012"}
    mock_boto_client.return_value = mock_sts
    
    # Act
    result = fetch_account_data("123456789012")
    
    # Assert
    assert result["Account"] == "123456789012"
    mock_boto_client.assert_called_once_with('sts')
```

---

## AI Coder Collaboration Guidelines

### Code Generation Standards

When AI coders generate code, they must:

1. **Always include docstrings** for all public functions and classes
2. **Use type hints consistently** for all function signatures
3. **Follow existing code patterns** in the codebase
4. **Document design decisions** in comments when non-obvious
5. **Keep functions focused and testable** - single responsibility
6. **Use meaningful variable names** - avoid abbreviations unless standard
7. **Include error handling** for all external API calls
8. **Add type hints** even for internal functions

### Code Review for AI-Generated Code

When reviewing AI-generated code, verify:

- [ ] All functions have docstrings
- [ ] Type hints are present and correct
- [ ] Error handling is appropriate
- [ ] Code follows existing patterns
- [ ] Function length is within limits
- [ ] Complexity is reasonable
- [ ] Tests are included for new functionality
- [ ] No hardcoded values (use constants or config)
- [ ] No security vulnerabilities (secrets, SQL injection, etc.)

### Consistency Checks

AI coders should:

- **Match existing style**: Follow the same patterns as existing code
- **Use same libraries**: Don't introduce new dependencies without justification
- **Follow naming conventions**: Use the same naming style as the codebase
- **Maintain structure**: Follow the same module/class organization

### Documentation Requirements

AI coders must document:

- **Why, not what**: Explain design decisions and business logic
- **Complex algorithms**: Document non-obvious logic
- **API changes**: Document any breaking changes
- **Dependencies**: Document new dependencies and why they're needed

### Example AI Coder Output

**Good AI-generated code:**
```python
def assess_iam_security(session: boto3.Session) -> Dict[str, Any]:
    """Assess IAM security configuration for an AWS account.
    
    This function checks IAM configurations against security best practices
    including password policies, MFA requirements, and access key rotation.
    
    Args:
        session: Boto3 session for AWS API calls
    
    Returns:
        Dictionary containing IAM security assessment results with keys:
            - password_policy: Password policy compliance status
            - mfa_enabled: MFA configuration status
            - access_keys: Access key security analysis
            - risk_score: Overall IAM risk score (0.0-10.0)
    
    Raises:
        ClientError: If AWS IAM API calls fail
        ValueError: If session is invalid
    """
    if not session:
        raise ValueError("Session cannot be None")
    
    try:
        iam_client = session.client('iam')
        # Assessment logic here
        return assessment_results
    except ClientError as e:
        raise SecurityAssessmentError(f"IAM assessment failed: {e}") from e
```

**Bad AI-generated code:**
```python
def check_iam(s):
    # Check IAM
    c = s.client('iam')
    r = {}
    # ... lots of code without documentation
    return r
```

---

## Code Review Checklist

Use this checklist when reviewing code (human or AI-generated):

### Functionality
- [ ] Code works as intended
- [ ] Edge cases are handled
- [ ] Error handling is appropriate
- [ ] No security vulnerabilities
- [ ] Performance is acceptable

### Code Quality
- [ ] Functions are within length limits (≤50 lines)
- [ ] Cyclomatic complexity is reasonable (≤10)
- [ ] Nesting depth is acceptable (≤3 levels)
- [ ] No code duplication
- [ ] Single responsibility principle followed

### Documentation
- [ ] All public functions have docstrings
- [ ] Type hints are present and correct
- [ ] Complex logic is commented
- [ ] README/docs updated if needed

### Style
- [ ] Follows naming conventions
- [ ] Follows PEP 8 (with project modifications)
- [ ] Imports are organized correctly
- [ ] Consistent formatting

### Testing
- [ ] Tests are included for new functionality
- [ ] Tests cover edge cases
- [ ] Test coverage is adequate
- [ ] Tests are readable and maintainable

### Organization
- [ ] Code is in the right location
- [ ] Module/class length is within limits
- [ ] Dependencies are justified
- [ ] No unused imports or code

---

## Quick Reference

See `CODING_STANDARDS_QUICK_REF.md` for a condensed one-page reference guide.

---

## Additional Resources

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
- [Real Python - Best Practices](https://realpython.com/python-code-quality/)

---

**Last Updated**: 2025-01-19  
**Version**: 1.0.0

