"""
Example module demonstrating code that violates coding standards.

⚠️ WARNING: This file contains intentionally bad code for educational purposes.
Do NOT use this as a reference for writing code.

This module shows common anti-patterns and violations of coding standards
to help developers understand what to avoid.
"""

# Bad: No organization, mixed imports
import json
import os
import sys
from datetime import datetime

import boto3


# Bad: No constants, magic numbers everywhere
def calc(x, y, z):
    # Bad: No docstring, unclear variable names, no type hints
    # Bad: Too many parameters (should use dataclass)
    # Bad: No error handling
    return x * y * (1 - z)


# Bad: No docstring, no type hints, unclear name
def proc(data):
    # Bad: Deep nesting (4+ levels)
    # Bad: Too complex (high cyclomatic complexity)
    # Bad: Too long function (>50 lines)
    if data:
        if len(data) > 0:
            result = []
            for item in data:
                if item:
                    if "id" in item:
                        if item["id"]:
                            if isinstance(item["id"], str):
                                result.append(item)
            if result:
                if len(result) > 0:
                    return result
    return []


# Bad: No docstring, no type hints, unclear return type
def check(u, t):
    # Bad: Returns multiple types without Union
    # Bad: No error handling
    if not u:
        return None
    if not t:
        return False
    return True


# Bad: No docstring, no type hints, too many parameters
def process(
    account_id, region, include_cost, timeout, retry_count, output_format, verbose, dry_run
):
    # Bad: 8 parameters (max should be 5, prefer 3)
    # Bad: No validation
    # Bad: No error handling
    pass


# Bad: No docstring, no type hints, suppresses all errors
def fetch_data(account_id):
    try:
        # Bad: No validation of input
        client = boto3.client("sts")
        response = client.get_caller_identity()
        return response
    except:  # Bad: Bare except, suppresses all errors
        return {}  # Bad: Returns empty dict, hiding error


# Bad: No docstring, no type hints, obvious comments
def process_items(items):
    # Bad: Commenting the obvious
    result = []  # Create empty list
    for item in items:  # Loop through items
        # Bad: Commenting what code does, not why
        processed = item.upper()  # Convert to uppercase
        result.append(processed)  # Add to result
    return result  # Return result


# Bad: No docstring, no type hints, high complexity
def validate_user(user):
    # Bad: High cyclomatic complexity (>10)
    if user:
        if user.is_active:
            if user.has_permission:
                if user.subscription_valid:
                    if user.account_balance > 0:
                        if user.email_verified:
                            if user.phone_verified:
                                if user.two_factor_enabled:
                                    if user.last_login_recent:
                                        if user.no_suspicious_activity:
                                            return True
    return False


# Bad: No docstring, no type hints, wrong data structure
def check_membership(user_id, user_list):
    # Bad: Using list for membership test (O(n) instead of O(1) with set)
    if user_id in user_list:
        return True
    return False


# Bad: No docstring, no type hints, no error handling
def divide(a, b):
    # Bad: No validation, will crash on division by zero
    return a / b


# Bad: No docstring, no type hints, returns multiple types
def get_value(key, data):
    # Bad: Returns different types without Union
    if key not in data:
        return None
    if isinstance(data[key], dict):
        return {}
    return data[key]
