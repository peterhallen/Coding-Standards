# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name
from pathlib import Path

from coding_standards import debug_paths


def test_repo_root_exists():
    root = debug_paths.get_repo_root()
    assert root is None or isinstance(root, Path)


def test_is_running_from_repo_returns_bool():
    result = debug_paths.is_running_from_repo()
    assert isinstance(result, bool)
