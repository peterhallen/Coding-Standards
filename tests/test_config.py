# pylint: disable=missing-module-docstring,missing-function-docstring
# pylint: disable=invalid-name,wrong-import-order
from pathlib import Path

import pytest
import tempfile

from coding_standards.config import (
    PROFILES,
    Config,
    GoConfig,
    JavaScriptConfig,
    PlatformConfig,
    PythonConfig,
    get_profile_defaults,
    load_config,
    load_config_from_file,
    merge_configs,
)


class TestGetProfileDefaults:
    """Tests for get_profile_defaults function."""

    def test_get_profile_defaults_strict(self):
        defaults = get_profile_defaults("strict")
        assert defaults["python"]["line_length"] == 88
        assert defaults["python"]["max_complexity"] == 5
        assert defaults["python"]["max_args"] == 4
        assert defaults["python"]["coverage_threshold"] == 90

    def test_get_profile_defaults_standard(self):
        defaults = get_profile_defaults("standard")
        assert defaults["python"]["line_length"] == 100
        assert defaults["python"]["max_complexity"] == 10
        assert defaults["python"]["max_args"] == 5
        assert defaults["python"]["coverage_threshold"] == 80

    def test_get_profile_defaults_lenient(self):
        defaults = get_profile_defaults("lenient")
        assert defaults["python"]["line_length"] == 120
        assert defaults["python"]["max_complexity"] == 15
        assert defaults["python"]["max_args"] == 7
        assert defaults["python"]["coverage_threshold"] == 60

    def test_get_profile_defaults_invalid_profile_raises_error(self):
        with pytest.raises(ValueError, match="Invalid profile 'invalid'"):
            get_profile_defaults("invalid")


class TestMergeConfigs:
    """Tests for merge_configs function."""

    def test_merge_configs_simple(self):
        base = {"a": 1, "b": 2}
        override = {"b": 3, "c": 4}
        result = merge_configs(base, override)
        assert result == {"a": 1, "b": 3, "c": 4}

    def test_merge_configs_nested(self):
        base = {"python": {"line_length": 100, "max_args": 5}}
        override = {"python": {"line_length": 88}}
        result = merge_configs(base, override)
        assert result == {"python": {"line_length": 88, "max_args": 5}}

    def test_merge_configs_deep_nested(self):
        base = {"a": {"b": {"c": 1, "d": 2}}}
        override = {"a": {"b": {"c": 3}}}
        result = merge_configs(base, override)
        assert result == {"a": {"b": {"c": 3, "d": 2}}}


class TestLoadConfig:
    """Tests for load_config function."""

    def test_load_config_missing_file_returns_defaults(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config = load_config(Path(tmpdir))
            assert config.profile == "standard"
            assert config.python.line_length == 100
            assert config.python.max_complexity == 10

    def test_load_config_from_coding_standards_toml(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "strict"

[python]
line_length = 88
max_complexity = 5
"""
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert config.profile == "strict"
            assert config.python.line_length == 88
            assert config.python.max_complexity == 5

    def test_load_config_from_pyproject_toml(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
[build-system]
requires = ["setuptools"]

[tool.coding-standards]
profile = "lenient"

[tool.coding-standards.python]
line_length = 120
coverage_threshold = 60
"""
            config_file = Path(tmpdir) / "pyproject.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert config.profile == "lenient"
            assert config.python.line_length == 120
            assert config.python.coverage_threshold == 60

    def test_load_config_coding_standards_toml_takes_precedence(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create both files
            coding_standards_content = """
profile = "strict"
[python]
line_length = 88
"""
            pyproject_content = """
[tool.coding-standards]
profile = "lenient"
[tool.coding-standards.python]
line_length = 120
"""
            (Path(tmpdir) / ".coding-standards.toml").write_text(coding_standards_content)
            (Path(tmpdir) / "pyproject.toml").write_text(pyproject_content)

            config = load_config(Path(tmpdir))
            # .coding-standards.toml should take precedence
            assert config.profile == "strict"
            assert config.python.line_length == 88

    def test_load_config_profile_inheritance(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "strict"
# Only override one value, rest should come from profile
[python]
coverage_threshold = 95
"""
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert config.profile == "strict"
            # From strict profile
            assert config.python.line_length == 88
            assert config.python.max_complexity == 5
            # Overridden value
            assert config.python.coverage_threshold == 95

    def test_load_config_invalid_toml_raises_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = "invalid toml content [[[["
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            with pytest.raises(ValueError, match="Invalid TOML"):
                load_config(Path(tmpdir))

    def test_load_config_invalid_profile_raises_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = 'profile = "nonexistent"'
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            with pytest.raises(ValueError, match="Invalid profile"):
                load_config(Path(tmpdir))

    def test_load_config_with_exclude_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "standard"
exclude = ["legacy/", "vendor/", "migrations/"]
"""
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert "legacy/" in config.exclude
            assert "vendor/" in config.exclude
            assert "migrations/" in config.exclude

    def test_load_config_with_platforms(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "standard"

[platforms]
cursor = true
copilot = false
claude_code = true
antigravity = false
"""
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert config.platforms.cursor is True
            assert config.platforms.copilot is False
            assert config.platforms.claude_code is True
            assert config.platforms.antigravity is False

    def test_load_config_javascript_settings(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "standard"

[javascript]
enabled = false
indent_size = 4
"""
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert config.javascript.enabled is False
            assert config.javascript.indent_size == 4

    def test_load_config_go_settings(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "standard"

[go]
enabled = false
"""
            config_file = Path(tmpdir) / ".coding-standards.toml"
            config_file.write_text(config_content)

            config = load_config(Path(tmpdir))
            assert config.go.enabled is False


class TestLoadConfigFromFile:
    """Tests for load_config_from_file function."""

    def test_load_config_from_file_success(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
profile = "strict"
[python]
line_length = 88
"""
            config_file = Path(tmpdir) / "custom-config.toml"
            config_file.write_text(config_content)

            config = load_config_from_file(config_file)
            assert config.profile == "strict"
            assert config.python.line_length == 88

    def test_load_config_from_file_not_found_raises_error(self):
        with pytest.raises(FileNotFoundError):
            load_config_from_file(Path("/nonexistent/config.toml"))

    def test_load_config_from_file_pyproject_with_section(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
[build-system]
requires = ["setuptools"]

[tool.coding-standards]
profile = "lenient"
"""
            config_file = Path(tmpdir) / "pyproject.toml"
            config_file.write_text(config_content)

            config = load_config_from_file(config_file)
            assert config.profile == "lenient"

    def test_load_config_from_file_pyproject_without_section(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config_content = """
[build-system]
requires = ["setuptools"]
"""
            config_file = Path(tmpdir) / "pyproject.toml"
            config_file.write_text(config_content)

            config = load_config_from_file(config_file)
            # Should return defaults when no [tool.coding-standards] section
            assert config.profile == "standard"


class TestConfigDataclasses:
    """Tests for Config dataclasses."""

    def test_config_defaults(self):
        config = Config()
        assert config.profile == "standard"
        assert isinstance(config.python, PythonConfig)
        assert isinstance(config.javascript, JavaScriptConfig)
        assert isinstance(config.go, GoConfig)
        assert isinstance(config.platforms, PlatformConfig)
        assert config.exclude == []

    def test_python_config_defaults(self):
        python_config = PythonConfig()
        assert python_config.line_length == 100
        assert python_config.max_complexity == 10
        assert python_config.max_args == 5
        assert python_config.coverage_threshold == 80

    def test_javascript_config_defaults(self):
        js_config = JavaScriptConfig()
        assert js_config.enabled is True
        assert js_config.indent_size == 2

    def test_go_config_defaults(self):
        go_config = GoConfig()
        assert go_config.enabled is True

    def test_platform_config_defaults(self):
        platform_config = PlatformConfig()
        assert platform_config.cursor is True
        assert platform_config.copilot is True
        assert platform_config.claude_code is False
        assert platform_config.antigravity is False
        assert platform_config.agent_os is False
        assert platform_config.chatgpt is False


class TestProfiles:
    """Tests for profile definitions."""

    def test_profiles_contain_expected_keys(self):
        for profile_name in ["strict", "standard", "lenient"]:
            profile = PROFILES[profile_name]
            assert "python" in profile
            assert "javascript" in profile
            assert "go" in profile

    def test_profiles_python_settings(self):
        for profile_name in ["strict", "standard", "lenient"]:
            profile = PROFILES[profile_name]
            python = profile["python"]
            assert "line_length" in python
            assert "max_complexity" in python
            assert "max_args" in python
            assert "coverage_threshold" in python

    def test_strict_is_most_restrictive(self):
        strict = PROFILES["strict"]["python"]
        standard = PROFILES["standard"]["python"]
        lenient = PROFILES["lenient"]["python"]

        # Line length: strict < standard < lenient
        assert strict["line_length"] < standard["line_length"] < lenient["line_length"]

        # Complexity: strict < standard < lenient
        assert strict["max_complexity"] < standard["max_complexity"] < lenient["max_complexity"]

        # Max args: strict < standard < lenient
        assert strict["max_args"] < standard["max_args"] < lenient["max_args"]

        # Coverage: strict > standard > lenient
        assert strict["coverage_threshold"] > standard["coverage_threshold"]
        assert standard["coverage_threshold"] > lenient["coverage_threshold"]
