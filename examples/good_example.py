"""
Example module demonstrating good coding practices.

This module shows examples of code that follows all the coding standards
including proper documentation, type hints, error handling, and structure.
"""

# Standard library imports
from datetime import datetime
from typing import Any, Dict, List, Optional

# Third-party imports
# (None in this example)

# Local imports
# (None in this example)

# Constants
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
DEFAULT_REGION = "us-east-1"


class DataProcessor:
    """Process and validate data according to business rules.

    This class demonstrates proper class structure, documentation,
    and error handling following the coding standards.

    Attributes:
        config: Configuration dictionary for processing settings
        _cache: Internal cache for processed data (private)

    Example:
        >>> processor = DataProcessor({"timeout": 30})
        >>> result = processor.process_items(["item1", "item2"])
        >>> print(result["processed_count"])
        2
    """

    def __init__(self, config: Optional[Dict] = None) -> None:
        """Initialize data processor with optional configuration.

        Args:
            config: Optional configuration dictionary. If not provided,
                default settings will be used.
        """
        self.config = config or {}
        self._cache: Dict[str, Any] = {}

    def process_items(self, items: List[str]) -> Dict[str, Any]:
        """Process a list of items and return results.

        This method demonstrates proper function structure, error handling,
        and return type annotations.

        Args:
            items: List of item identifiers to process

        Returns:
            Dictionary containing processing results with keys:
                - processed_count: Number of successfully processed items
                - failed_count: Number of items that failed processing
                - results: List of processed item data
                - timestamp: ISO format timestamp of processing

        Raises:
            ValueError: If items list is empty or None

        Example:
            >>> processor = DataProcessor()
            >>> result = processor.process_items(["item1", "item2"])
            >>> assert result["processed_count"] == 2
        """
        if not items:
            raise ValueError("Items list cannot be empty")

        if not isinstance(items, list):
            raise TypeError(f"Expected list, got {type(items).__name__}")

        processed_count = 0
        failed_count = 0
        results: List[Dict] = []

        for item in items:
            try:
                processed_item = self._process_single_item(item)
                results.append(processed_item)
                processed_count += 1
            except Exception as e:
                failed_count += 1
                # Log error in real implementation
                print(f"Failed to process item {item}: {e}")

        return {
            "processed_count": processed_count,
            "failed_count": failed_count,
            "results": results,
            "timestamp": datetime.now().isoformat(),
        }

    def _process_single_item(self, item: str) -> Dict[str, Any]:
        """Process a single item (private helper method).

        Args:
            item: Item identifier to process

        Returns:
            Dictionary containing processed item data

        Raises:
            ValueError: If item is invalid
        """
        if not item or not isinstance(item, str):
            raise ValueError(f"Invalid item: {item}")

        # Check cache first
        if item in self._cache:
            return self._cache[item]

        # Process item (simplified example)
        processed = {"id": item, "status": "processed", "data": f"processed_{item}"}

        # Cache result
        self._cache[item] = processed

        return processed


def calculate_total_cost(usage_hours: float, rate_per_hour: float, discount: float = 0.0) -> float:
    """Calculate total cost based on usage and rate.

    This function demonstrates proper function documentation, type hints,
    and simple, focused functionality.

    Args:
        usage_hours: Number of hours used
        rate_per_hour: Cost per hour
        discount: Optional discount percentage (0.0 to 1.0). Defaults to 0.0.

    Returns:
        Total cost after applying discount

    Raises:
        ValueError: If any parameter is negative or discount > 1.0

    Example:
        >>> cost = calculate_total_cost(10.0, 5.0, 0.1)
        >>> assert cost == 45.0
    """
    if usage_hours < 0:
        raise ValueError("Usage hours cannot be negative")

    if rate_per_hour < 0:
        raise ValueError("Rate per hour cannot be negative")

    if discount < 0 or discount > 1.0:
        raise ValueError("Discount must be between 0.0 and 1.0")

    subtotal = usage_hours * rate_per_hour
    total = subtotal * (1.0 - discount)

    return round(total, 2)


def is_user_authenticated(user_id: str, session_token: Optional[str] = None) -> bool:
    """Check if a user is authenticated.

    This function demonstrates boolean naming conventions and
    early return patterns to reduce nesting.

    Args:
        user_id: User identifier to check
        session_token: Optional session token for validation

    Returns:
        True if user is authenticated, False otherwise

    Example:
        >>> is_authenticated = is_user_authenticated("user123", "token456")
        >>> assert isinstance(is_authenticated, bool)
    """
    if not user_id:
        return False

    if not session_token:
        return False

    # Simplified validation logic
    # In real implementation, would validate token against database
    return len(session_token) > 10


def process_data_with_retry(
    data: List[Dict], max_retries: int = MAX_RETRY_ATTEMPTS
) -> Dict[str, Any]:
    """Process data with retry logic on failure.

    This function demonstrates error handling, retry patterns,
    and proper use of constants.

    Args:
        data: List of data dictionaries to process
        max_retries: Maximum number of retry attempts. Defaults to MAX_RETRY_ATTEMPTS.

    Returns:
        Dictionary containing processing results

    Raises:
        ValueError: If data is empty
        RuntimeError: If processing fails after all retries
    """
    if not data:
        raise ValueError("Data cannot be empty")

    last_exception = None

    for attempt in range(max_retries):
        try:
            # Simulate processing
            return {"status": "success", "processed": len(data), "attempt": attempt + 1}
        except Exception as e:
            last_exception = e
            if attempt < max_retries - 1:
                # Would implement exponential backoff here
                continue

    raise RuntimeError(f"Processing failed after {max_retries} attempts") from last_exception


if __name__ == "__main__":
    """Example usage of the module."""
    # Example 1: Using the DataProcessor class
    processor = DataProcessor({"timeout": 30})
    result = processor.process_items(["item1", "item2", "item3"])
    print(f"Processed {result['processed_count']} items")

    # Example 2: Using utility functions
    cost = calculate_total_cost(10.0, 5.0, 0.1)
    print(f"Total cost: ${cost}")

    # Example 3: Boolean function
    authenticated = is_user_authenticated("user123", "valid_token_12345")
    print(f"User authenticated: {authenticated}")
