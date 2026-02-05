"""
Configuration file support for coding standards.

Loads configuration from .coding-standards.toml or pyproject.toml.
"""

# pylint: disable=invalid-name

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from dataclasses import dataclass, field

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


# Preset profile defaults
PROFILES: Dict[str, Dict[str, Any]] = {
    "strict": {
        "python": {
            "line_length": 88,
            "max_complexity": 5,
            "max_args": 4,
            "coverage_threshold": 90,
        },
        "javascript": {"enabled": True, "indent_size": 2},
        "go": {"enabled": True},
    },
    "standard": {
        "python": {
            "line_length": 100,
            "max_complexity": 10,
            "max_args": 5,
            "coverage_threshold": 80,
        },
        "javascript": {"enabled": True, "indent_size": 2},
        "go": {"enabled": True},
    },
    "lenient": {
        "python": {
            "line_length": 120,
            "max_complexity": 15,
            "max_args": 7,
            "coverage_threshold": 60,
        },
        "javascript": {"enabled": True, "indent_size": 2},
        "go": {"enabled": True},
    },
}


@dataclass
class PythonConfig:
    """Python-specific configuration settings."""

    line_length: int = 100
    max_complexity: int = 10
    max_args: int = 5
    coverage_threshold: int = 80


@dataclass
class JavaScriptConfig:
    """JavaScript-specific configuration settings."""

    enabled: bool = True
    indent_size: int = 2


@dataclass
class GoConfig:
    """Go-specific configuration settings."""

    enabled: bool = True


@dataclass
class PlatformConfig:
    """AI platform installation defaults."""

    cursor: bool = True
    copilot: bool = True
    claude_code: bool = False
    antigravity: bool = False
    agent_os: bool = False
    chatgpt: bool = False


@dataclass
class Config:
    """Main configuration class."""

    profile: str = "standard"
    python: PythonConfig = field(default_factory=PythonConfig)
    javascript: JavaScriptConfig = field(default_factory=JavaScriptConfig)
    go: GoConfig = field(default_factory=GoConfig)
    exclude: List[str] = field(default_factory=list)
    platforms: PlatformConfig = field(default_factory=PlatformConfig)


def get_profile_defaults(profile: str) -> Dict[str, Any]:
    """Get default settings for a profile.

    Args:
        profile: Profile name (strict, standard, lenient)

    Returns:
        Dictionary of profile defaults

    Raises:
        ValueError: If profile name is invalid
    """
    if profile not in PROFILES:
        valid_profiles = ", ".join(PROFILES.keys())
        raise ValueError(f"Invalid profile '{profile}'. Valid profiles: {valid_profiles}")
    return PROFILES[profile]


def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge two configuration dictionaries.

    Args:
        base: Base configuration dictionary
        override: Override configuration dictionary

    Returns:
        Merged configuration dictionary
    """
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result


def _parse_toml_config(data: Dict[str, Any]) -> Config:
    """Parse TOML data into a Config object.

    Args:
        data: Dictionary from TOML parser

    Returns:
        Config object with parsed values
    """
    profile = data.get("profile", "standard")

    if profile not in PROFILES:
        valid_profiles = ", ".join(PROFILES.keys())
        raise ValueError(f"Invalid profile '{profile}'. Valid profiles: {valid_profiles}")

    profile_defaults = get_profile_defaults(profile)
    merged = merge_configs(profile_defaults, data)

    python_data = merged.get("python", {})
    python_config = PythonConfig(
        line_length=python_data.get("line_length", 100),
        max_complexity=python_data.get("max_complexity", 10),
        max_args=python_data.get("max_args", 5),
        coverage_threshold=python_data.get("coverage_threshold", 80),
    )

    js_data = merged.get("javascript", {})
    js_config = JavaScriptConfig(
        enabled=js_data.get("enabled", True),
        indent_size=js_data.get("indent_size", 2),
    )

    go_data = merged.get("go", {})
    go_config = GoConfig(enabled=go_data.get("enabled", True))

    platforms_data = merged.get("platforms", {})
    platforms_config = PlatformConfig(
        cursor=platforms_data.get("cursor", True),
        copilot=platforms_data.get("copilot", True),
        claude_code=platforms_data.get("claude_code", False),
        antigravity=platforms_data.get("antigravity", False),
        agent_os=platforms_data.get("agent_os", False),
        chatgpt=platforms_data.get("chatgpt", False),
    )

    exclude = merged.get("exclude", [])

    return Config(
        profile=profile,
        python=python_config,
        javascript=js_config,
        go=go_config,
        exclude=exclude,
        platforms=platforms_config,
    )


def load_config(project_dir: Optional[Path] = None) -> Config:
    """Load configuration from project directory.

    Searches for configuration in this order:
    1. .coding-standards.toml in project root
    2. [tool.coding-standards] section in pyproject.toml
    3. Built-in defaults

    Args:
        project_dir: Project directory to search in (defaults to current directory)

    Returns:
        Config object with loaded settings
    """
    if project_dir is None:
        project_dir = Path.cwd()
    else:
        project_dir = Path(project_dir).resolve()

    config_file = project_dir / ".coding-standards.toml"
    if config_file.exists():
        try:
            with open(config_file, "rb") as f:
                data = tomllib.load(f)
            return _parse_toml_config(data)
        except tomllib.TOMLDecodeError as e:
            raise ValueError(f"Invalid TOML in {config_file}: {e}") from e

    pyproject_file = project_dir / "pyproject.toml"
    if pyproject_file.exists():
        try:
            with open(pyproject_file, "rb") as f:
                data = tomllib.load(f)
            if "tool" in data and "coding-standards" in data["tool"]:
                return _parse_toml_config(data["tool"]["coding-standards"])
        except tomllib.TOMLDecodeError as e:
            raise ValueError(f"Invalid TOML in {pyproject_file}: {e}") from e

    return Config()


def load_config_from_file(config_path: Path) -> Config:
    """Load configuration from a specific file.

    Args:
        config_path: Path to configuration file

    Returns:
        Config object with loaded settings

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If config file is invalid
    """
    config_path = Path(config_path).resolve()

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    try:
        with open(config_path, "rb") as f:
            data = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        raise ValueError(f"Invalid TOML in {config_path}: {e}") from e

    if config_path.name == "pyproject.toml":
        if "tool" in data and "coding-standards" in data["tool"]:
            return _parse_toml_config(data["tool"]["coding-standards"])
        return Config()

    return _parse_toml_config(data)
