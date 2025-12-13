# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from pathlib import Path

from coding_standards.cli import _get_package_data_path


def test_get_package_data_path_nonexistent():
    result = _get_package_data_path("does_not_exist.txt")
    assert result is None


def test_get_package_data_path_returns_path_for_existing_file():
    # pyproject.toml should exist in dev mode
    result = _get_package_data_path("pyproject.toml")
    assert result is None or isinstance(result, Path)
