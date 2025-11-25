"""
CLI tool for installing and managing coding standards in projects.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

import shutil

try:
    from ai_coding_standards import PACKAGE_ROOT
except ImportError:
    # Fallback for development
    PACKAGE_ROOT = Path(__file__).parent.parent.parent


def get_config_files() -> List[Path]:
    """Get list of configuration files to install."""
    config_files = [
        ".editorconfig",
        ".flake8",
        ".pylintrc",
        "pyproject.toml",
        ".pre-commit-config.yaml",
    ]
    return [PACKAGE_ROOT / file for file in config_files if (PACKAGE_ROOT / file).exists()]


def get_documentation_files() -> List[Path]:
    """Get list of documentation files."""
    doc_files = [
        "CODING_STANDARDS.md",
        "CODING_STANDARDS_QUICK_REF.md",
        "AI_PROMPT_STANDARDS.md",
        "AI_PROMPT_STANDARDS_QUICK_REF.md",
    ]
    # Try package root first, then fallback to parent of src/
    base_paths = [PACKAGE_ROOT, PACKAGE_ROOT.parent]
    for base_path in base_paths:
        files = [base_path / file for file in doc_files if (base_path / file).exists()]
        if files:
            return files
    return []


def install_configs(target_dir: Path, overwrite: bool = False, interactive: bool = True) -> None:
    """Install configuration files to target directory.

    Args:
        target_dir: Directory where configs should be installed
        overwrite: Whether to overwrite existing files
        interactive: Whether to prompt before overwriting
    """
    target_dir = Path(target_dir).resolve()

    if not target_dir.exists():
        print(f"Error: Target directory does not exist: {target_dir}")
        sys.exit(1)

    config_files = get_config_files()
    installed = []
    skipped = []

    for config_file in config_files:
        target_path = target_dir / config_file.name

        if target_path.exists() and not overwrite:
            if interactive:
                response = input(f"{config_file.name} already exists. Overwrite? [y/N]: ")
                if response.lower() != "y":
                    skipped.append(config_file.name)
                    continue
            else:
                skipped.append(config_file.name)
                continue

        shutil.copy2(config_file, target_path)
        installed.append(config_file.name)
        print(f"✓ Installed {config_file.name}")

    if installed:
        print(f"\n✓ Installed {len(installed)} configuration file(s)")

    if skipped:
        print(f"\n⊘ Skipped {len(skipped)} existing file(s) (use --overwrite to replace)")

    if not installed and not skipped:
        print("No configuration files to install")


def install_docs(target_dir: Path, overwrite: bool = False) -> None:
    """Install documentation files to target directory.

    Args:
        target_dir: Directory where docs should be installed
        overwrite: Whether to overwrite existing files
    """
    target_dir = Path(target_dir).resolve()
    docs_dir = target_dir / "docs" / "standards"
    docs_dir.mkdir(parents=True, exist_ok=True)

    doc_files = get_documentation_files()
    installed = []

    for doc_file in doc_files:
        target_path = docs_dir / doc_file.name

        if target_path.exists() and not overwrite:
            continue

        shutil.copy2(doc_file, target_path)
        installed.append(doc_file.name)
        print(f"✓ Installed {doc_file.name} to {docs_dir}")

    if installed:
        print(f"\n✓ Installed {len(installed)} documentation file(s) to {docs_dir}")


def setup_pre_commit(target_dir: Path) -> None:
    """Set up pre-commit hooks in target directory.

    Args:
        target_dir: Directory where pre-commit should be set up
    """
    target_dir = Path(target_dir).resolve()

    try:
        import subprocess

        # Check if pre-commit is installed
        result = subprocess.run(
            ["pre-commit", "--version"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("Warning: pre-commit is not installed.")
            print("Install it with: pip install pre-commit")
            return

        # Install pre-commit hooks
        subprocess.run(
            ["pre-commit", "install"],
            cwd=target_dir,
            check=True,
        )
        print("✓ Pre-commit hooks installed")

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Warning: Could not set up pre-commit hooks")
        print("Make sure pre-commit is installed: pip install pre-commit")


def show_info() -> None:
    """Show information about the coding standards package."""
    print("AI Coding Standards")
    print("=" * 50)
    print(f"Version: {__import__('ai_coding_standards').__version__}")
    print(f"Package root: {PACKAGE_ROOT}")
    print("\nConfiguration files:")
    for config in get_config_files():
        print(f"  - {config.name}")
    print("\nDocumentation files:")
    for doc in get_documentation_files():
        print(f"  - {doc.name}")


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Install and manage AI coding standards in your project"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install standards")
    install_parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory (default: current directory)",
    )
    install_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing configuration files",
    )
    install_parser.add_argument(
        "--no-interactive",
        action="store_true",
        help="Don't prompt for confirmation",
    )
    install_parser.add_argument(
        "--docs",
        action="store_true",
        help="Also install documentation files",
    )
    install_parser.add_argument(
        "--pre-commit",
        action="store_true",
        help="Set up pre-commit hooks",
    )

    # Info command
    subparsers.add_parser("info", help="Show package information")

    args = parser.parse_args()

    if args.command == "install":
        target = Path(args.target).resolve()
        install_configs(
            target,
            overwrite=args.overwrite,
            interactive=not args.no_interactive,
        )

        if args.docs:
            install_docs(target, overwrite=args.overwrite)

        if args.pre_commit:
            setup_pre_commit(target)

    elif args.command == "info":
        show_info()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
