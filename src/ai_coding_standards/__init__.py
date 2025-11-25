"""
AI Coding Standards Package.

This package provides coding standards, configuration files, and tools
for maintaining code quality across Python projects.
"""

__version__ = "1.0.0"
__author__ = "AI Coding Standards Team"

from pathlib import Path

# Package root directory
PACKAGE_ROOT = Path(__file__).parent.parent.parent

# Standards documents
STANDARDS_DIR = PACKAGE_ROOT / "docs"
CONFIG_DIR = PACKAGE_ROOT / "config"
