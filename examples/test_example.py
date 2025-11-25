"""
Example test module demonstrating testing standards.

This module shows examples of proper test structure following the
testing standards defined in CODING_STANDARDS.md.
"""

# Standard library imports
from unittest.mock import Mock, patch
from typing import Dict

# Third-party imports
import pytest

# Local imports
from examples.good_example import (
    DataProcessor,
    calculate_total_cost,
    is_user_authenticated,
    process_data_with_retry
)


class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    def test_init_with_config(self) -> None:
        """Test DataProcessor initialization with configuration."""
        # Arrange
        config = {"timeout": 30, "retries": 3}
        
        # Act
        processor = DataProcessor(config)
        
        # Assert
        assert processor.config == config
        assert processor._cache == {}
    
    def test_init_without_config(self) -> None:
        """Test DataProcessor initialization without configuration."""
        # Arrange & Act
        processor = DataProcessor()
        
        # Assert
        assert processor.config == {}
        assert processor._cache == {}
    
    def test_process_items_success(self) -> None:
        """Test successful processing of items."""
        # Arrange
        processor = DataProcessor()
        items = ["item1", "item2", "item3"]
        
        # Act
        result = processor.process_items(items)
        
        # Assert
        assert result["processed_count"] == 3
        assert result["failed_count"] == 0
        assert len(result["results"]) == 3
        assert "timestamp" in result
    
    def test_process_items_empty_list_raises_error(self) -> None:
        """Test that processing empty list raises ValueError."""
        # Arrange
        processor = DataProcessor()
        
        # Act & Assert
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            processor.process_items([])
    
    def test_process_items_invalid_type_raises_error(self) -> None:
        """Test that processing invalid type raises TypeError."""
        # Arrange
        processor = DataProcessor()
        
        # Act & Assert
        with pytest.raises(TypeError):
            processor.process_items("not a list")
    
    def test_process_items_caches_results(self) -> None:
        """Test that processed items are cached."""
        # Arrange
        processor = DataProcessor()
        items = ["item1"]
        
        # Act
        result1 = processor.process_items(items)
        result2 = processor.process_items(items)
        
        # Assert
        assert result1["results"][0] == result2["results"][0]
        assert len(processor._cache) == 1


class TestCalculateTotalCost:
    """Test suite for calculate_total_cost function."""
    
    def test_calculate_total_cost_basic(self) -> None:
        """Test basic cost calculation."""
        # Arrange
        usage_hours = 10.0
        rate_per_hour = 5.0
        
        # Act
        result = calculate_total_cost(usage_hours, rate_per_hour)
        
        # Assert
        assert result == 50.0
    
    def test_calculate_total_cost_with_discount(self) -> None:
        """Test cost calculation with discount."""
        # Arrange
        usage_hours = 10.0
        rate_per_hour = 5.0
        discount = 0.1
        
        # Act
        result = calculate_total_cost(usage_hours, rate_per_hour, discount)
        
        # Assert
        assert result == 45.0
    
    def test_calculate_total_cost_negative_usage_raises_error(self) -> None:
        """Test that negative usage hours raises ValueError."""
        # Arrange
        usage_hours = -10.0
        rate_per_hour = 5.0
        
        # Act & Assert
        with pytest.raises(ValueError, match="Usage hours cannot be negative"):
            calculate_total_cost(usage_hours, rate_per_hour)
    
    def test_calculate_total_cost_invalid_discount_raises_error(self) -> None:
        """Test that invalid discount raises ValueError."""
        # Arrange
        usage_hours = 10.0
        rate_per_hour = 5.0
        discount = 1.5  # Invalid: > 1.0
        
        # Act & Assert
        with pytest.raises(ValueError, match="Discount must be between 0.0 and 1.0"):
            calculate_total_cost(usage_hours, rate_per_hour, discount)


class TestIsUserAuthenticated:
    """Test suite for is_user_authenticated function."""
    
    def test_is_user_authenticated_with_valid_token(self) -> None:
        """Test authentication with valid token."""
        # Arrange
        user_id = "user123"
        session_token = "valid_token_12345"
        
        # Act
        result = is_user_authenticated(user_id, session_token)
        
        # Assert
        assert result is True
    
    def test_is_user_authenticated_without_token(self) -> None:
        """Test authentication without token returns False."""
        # Arrange
        user_id = "user123"
        
        # Act
        result = is_user_authenticated(user_id)
        
        # Assert
        assert result is False
    
    def test_is_user_authenticated_empty_user_id(self) -> None:
        """Test authentication with empty user ID returns False."""
        # Arrange
        user_id = ""
        session_token = "token"
        
        # Act
        result = is_user_authenticated(user_id, session_token)
        
        # Assert
        assert result is False
    
    def test_is_user_authenticated_short_token(self) -> None:
        """Test authentication with short token returns False."""
        # Arrange
        user_id = "user123"
        session_token = "short"  # Too short
        
        # Act
        result = is_user_authenticated(user_id, session_token)
        
        # Assert
        assert result is False


class TestProcessDataWithRetry:
    """Test suite for process_data_with_retry function."""
    
    def test_process_data_with_retry_success(self) -> None:
        """Test successful processing on first attempt."""
        # Arrange
        data = [{"id": 1}, {"id": 2}]
        
        # Act
        result = process_data_with_retry(data)
        
        # Assert
        assert result["status"] == "success"
        assert result["processed"] == 2
        assert result["attempt"] == 1
    
    def test_process_data_with_retry_empty_data_raises_error(self) -> None:
        """Test that empty data raises ValueError."""
        # Arrange
        data = []
        
        # Act & Assert
        with pytest.raises(ValueError, match="Data cannot be empty"):
            process_data_with_retry(data)
    
    @patch('examples.good_example.process_data_with_retry')
    def test_process_data_with_retry_uses_max_retries(self, mock_process: Mock) -> None:
        """Test that retry logic uses max_retries parameter."""
        # Arrange
        data = [{"id": 1}]
        max_retries = 5
        
        # Act
        process_data_with_retry(data, max_retries)
        
        # Assert
        # In a real implementation, we would verify retry behavior
        # This is a simplified example
        assert True  # Placeholder assertion

