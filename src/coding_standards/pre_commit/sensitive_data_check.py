#!/usr/bin/env python3
"""
Sensitive Data Checker for Pre-commit Hook
Detects HL7 data, MDS assessments, and PII/PHI markers.
"""

import sys
from pathlib import Path
from typing import List, Pattern

import re

# Compile regex patterns for performance
SENSITIVE_PATTERNS: List[Pattern] = [
    # HL7 Base Pattern: 3 Uppercase letters followed by a pipe (e.g., MSH|, PID|)
    re.compile(r"^[A-Z]{3}\|"),
    # MDS 3.0 Assessment Markers (e.g., A0100., B0100.)
    re.compile(r"^[A-Z]\d{4}\."),
    # Specific Form Headers
    re.compile(r"MINIMUM DATA SET \(MDS\)"),
    re.compile(r"Section [A-Z] - Identification Information"),
    # PHI/PII Keywords (Case insensitive)
    re.compile(r"Social Security Number", re.IGNORECASE),
    re.compile(r"Medicare Number", re.IGNORECASE),
    re.compile(r"Resident Name", re.IGNORECASE),
    re.compile(r"Date of Birth", re.IGNORECASE),
]


def check_file(file_path: str) -> bool:
    """
    Checks a file for sensitive data patterns.
    Returns True if sensitive data is found, False otherwise.
    """
    path = Path(file_path)
    if not path.is_file():
        return False

    found_sensitive_data = False

    try:
        # Try reading as UTF-8 first
        with open(path, "r", encoding="utf-8") as file_handle:
            lines = file_handle.readlines()
    except UnicodeDecodeError:
        # Fallback to binary check if needed, or skip binary files
        # For this hook, let's skip binary files as they are less likely to contain
        # plain text sensitive markers without specialized parsing tools.
        return False

    for i, line in enumerate(lines, 1):
        for pattern in SENSITIVE_PATTERNS:
            if pattern.search(line):
                print(f"[ERROR] Sensitive data pattern found in {file_path} at line {i}:")
                # Truncate long lines to avoid flooding output
                print(f"    Line content: {line.strip()[:100]}...")
                found_sensitive_data = True
                # We want to find all instances, so we don't break here?
                # Or just report file failure? Let's report all lines.

    return found_sensitive_data


def main():
    """Main entry point."""
    files = sys.argv[1:]
    exit_code = 0

    for file_path in files:
        if check_file(file_path):
            exit_code = 1

    if exit_code != 0:
        print("\nCommit rejected: Sensitive data usage detected.")
        print("Please remove the sensitive data before committing.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
