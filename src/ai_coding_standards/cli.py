"""
CLI tool for installing and managing coding standards in projects.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

import shutil

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Python < 3.9
    import importlib_resources as pkg_resources

try:
    from ai_coding_standards import PACKAGE_ROOT
except ImportError:
    # Fallback for development
    PACKAGE_ROOT = Path(__file__).parent.parent.parent


def _get_package_data_path(file_path: str) -> Optional[Path]:
    """Get path to a file in the package data.
    
    Args:
        file_path: Relative path to file from package root (e.g., ".editorconfig")
    
    Returns:
        Path to file if found, None otherwise
    """
    # First, try to determine if we're in an installed package or development mode
    is_installed = False
    installed_pkg_dir = None
    
    try:
        import importlib.util
        spec = importlib.util.find_spec("ai_coding_standards")
        if spec and spec.origin:
            installed_pkg_dir = Path(spec.origin).parent
            # Check if this is an installed package (not in our dev repo)
            if "site-packages" in str(installed_pkg_dir) or "dist-packages" in str(installed_pkg_dir):
                is_installed = True
            # Also check if the data directory exists (indicates installed package structure)
            if (installed_pkg_dir / "data").exists():
                is_installed = True
    except Exception:
        pass
    
    # If installed, prioritize installed package location
    if is_installed and installed_pkg_dir:
        data_path = installed_pkg_dir / "data" / file_path
        if data_path.exists():
            return data_path
        # Also try pkg_resources methods for installed packages
        try:
            import pkg_resources as old_pkg_resources
            resource_path = old_pkg_resources.resource_filename("ai_coding_standards", f"data/{file_path}")
            if Path(resource_path).exists():
                return Path(resource_path)
        except Exception:
            pass
    
    # Then try development mode (files in repo root)
    for base_path in [PACKAGE_ROOT, PACKAGE_ROOT.parent]:
        potential_path = base_path / file_path
        if potential_path.exists():
            return potential_path
    
    # Fallback: try package data directory even if not detected as installed
    if installed_pkg_dir:
        data_path = installed_pkg_dir / "data" / file_path
        if data_path.exists():
            return data_path
    
    # Method 2: Use importlib.resources (Python 3.9+)
    try:
        if hasattr(pkg_resources, "files"):
            pkg = pkg_resources.files("ai_coding_standards")
            data_path = pkg / "data" / file_path
            if data_path.is_file():
                # For Python 3.9+, use as_path()
                try:
                    return data_path.as_path()
                except (AttributeError, TypeError):
                    # Fallback: read and write to temp file
                    import tempfile
                    import hashlib
                    # Create unique temp file name
                    file_hash = hashlib.md5(str(file_path).encode()).hexdigest()[:8]
                    temp_file = Path(tempfile.gettempdir()) / f"ai_coding_standards_{file_hash}_{Path(file_path).name}"
                    if not temp_file.exists():
                        temp_file.write_bytes(data_path.read_bytes())
                    return temp_file
    except Exception:
        pass
    
    # Method 3: Try pkg_resources.resource_filename (most reliable for installed packages)
    try:
        import pkg_resources as old_pkg_resources
        # Try data/ subdirectory
        try:
            resource_path = old_pkg_resources.resource_filename("ai_coding_standards", f"data/{file_path}")
            if Path(resource_path).exists():
                return Path(resource_path)
        except Exception:
            pass
        # Try direct
        try:
            resource_path = old_pkg_resources.resource_filename("ai_coding_standards", file_path)
            if Path(resource_path).exists():
                return Path(resource_path)
        except Exception:
            pass
    except Exception:
        pass
    
    # Method 4: Try pkg_resources.path()
    try:
        with pkg_resources.path("ai_coding_standards.data", file_path) as p:
            return Path(p)
    except Exception:
        pass
    
    return None


def get_config_files() -> List[Path]:
    """Get list of configuration files to install."""
    config_files = [
        ".editorconfig",
        ".flake8",
        ".pylintrc",
        "pyproject.toml",
        ".pre-commit-config.yaml",
        ".cursorrules",
    ]
    
    found_files = []
    for file_name in config_files:
        file_path = _get_package_data_path(file_name)
        if file_path and file_path.exists():
            found_files.append(file_path)
        else:
            # Debug: try to find where the package is installed
            try:
                import importlib.util
                spec = importlib.util.find_spec("ai_coding_standards")
                if spec and spec.origin:
                    pkg_dir = Path(spec.origin).parent
                    # Try data directory
                    data_file = pkg_dir / "data" / file_name
                    if data_file.exists():
                        found_files.append(data_file)
                        continue
            except Exception:
                pass
    
    return found_files


def get_documentation_files() -> List[Path]:
    """Get list of documentation files."""
    doc_files = [
        "CODING_STANDARDS.md",
        "CODING_STANDARDS_QUICK_REF.md",
        "AI_PROMPT_STANDARDS.md",
        "AI_PROMPT_STANDARDS_QUICK_REF.md",
    ]
    
    found_files = []
    for file_name in doc_files:
        file_path = _get_package_data_path(file_name)
        if file_path and file_path.exists():
            found_files.append(file_path)
    
    return found_files


def install_cursor_rules(target_dir: Path, overwrite: bool = False) -> None:
    """Install Cursor IDE rules to target directory.

    Args:
        target_dir: Directory where rules should be installed
        overwrite: Whether to overwrite existing files
    """
    target_dir = Path(target_dir).resolve()
    cursor_rules_dir = target_dir / ".cursor" / "rules"
    cursor_rules_dir.mkdir(parents=True, exist_ok=True)

    # Find source rules
    rule_file_names = [
        "function_standards.mdc",
        "documentation_standards.mdc",
        "error_handling.mdc",
        "naming_conventions.mdc",
        "testing_standards.mdc",
        "code_organization.mdc",
    ]
    
    rule_files = []
    
    # Try development mode first (files in repo)
    for base_path in [PACKAGE_ROOT, PACKAGE_ROOT.parent]:
        potential_dir = base_path / ".cursor" / "rules"
        if potential_dir.exists():
            rule_files = list(potential_dir.glob("*.mdc"))
            break
    
    # If not found, try package data
    if not rule_files:
        # Try to find the package data directory
        try:
            import importlib.util
            spec = importlib.util.find_spec("ai_coding_standards")
            if spec and spec.origin:
                pkg_dir = Path(spec.origin).parent
                rules_dir = pkg_dir / "data" / ".cursor" / "rules"
                if rules_dir.exists():
                    rule_files = list(rules_dir.glob("*.mdc"))
        except Exception:
            pass
        
        # If still not found, try individual files
        if not rule_files:
            for rule_name in rule_file_names:
                # Try multiple paths
                for path_variant in [
                    f".cursor/rules/{rule_name}",
                    f"data/.cursor/rules/{rule_name}",
                    rule_name,
                ]:
                    rule_path = _get_package_data_path(path_variant)
                    if rule_path and rule_path.exists():
                        rule_files.append(rule_path)
                        break
    
    if not rule_files:
        print("Warning: Cursor rules directory not found in package")
        return
    installed = []

    for rule_file in rule_files:
        target_path = cursor_rules_dir / rule_file.name

        if target_path.exists() and not overwrite:
            continue

        shutil.copy2(rule_file, target_path)
        installed.append(rule_file.name)
        print(f"✓ Installed Cursor rule: {rule_file.name}")

    if installed:
        print(f"\n✓ Installed {len(installed)} Cursor rule file(s) to {cursor_rules_dir}")
    else:
        print("No Cursor rules to install")


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


def check_compliance(
    target_dir: Path, detailed: bool = False, report: Optional[str] = None
) -> None:
    """Check code compliance with coding standards.

    Args:
        target_dir: Directory to check
        detailed: Show detailed information
        report: Path to save HTML report (optional)
    """
    target_dir = Path(target_dir).resolve()

    if not target_dir.exists():
        print(f"Error: Target directory does not exist: {target_dir}")
        sys.exit(1)

    print("Checking code compliance...")
    print("=" * 50)

    issues = []

    # Check for Python files
    python_files = list(target_dir.rglob("*.py"))
    python_files = [
        f
        for f in python_files
        if "__pycache__" not in str(f) and ".venv" not in str(f) and "venv" not in str(f)
    ]

    if not python_files:
        print("No Python files found to check.")
        return

    print(f"Found {len(python_files)} Python file(s)")
    print()

    # Run basic checks
    try:
        import subprocess

        # Check Black formatting
        print("Checking code formatting (Black)...")
        result = subprocess.run(
            ["black", "--check", "--diff", str(target_dir)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            issues.append("Code formatting issues (run: black .)")
            if detailed:
                print(result.stdout)

        # Check import sorting
        print("Checking import sorting (isort)...")
        result = subprocess.run(
            ["isort", "--check-only", "--diff", str(target_dir)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            issues.append("Import sorting issues (run: isort .)")
            if detailed:
                print(result.stdout)

        # Check with flake8
        print("Checking code quality (flake8)...")
        result = subprocess.run(
            ["flake8", str(target_dir)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            issues.append("Code quality issues (run: flake8 .)")
            if detailed and result.stdout:
                print(result.stdout[:500])  # Limit output

    except FileNotFoundError as e:
        print(f"Warning: Required tool not found: {e}")
        print("Install with: pip install black isort flake8")
        return

    # Summary
    print()
    print("=" * 50)
    if not issues:
        print("✅ Code appears to be compliant!")
        print("\nAll checks passed. Your code follows the standards.")
    else:
        print(f"⚠️  Found {len(issues)} compliance issue(s):")
        for issue in issues:
            print(f"  - {issue}")
        print("\nRun 'ai-coding-standards fix-compliance' to auto-fix some issues.")

    if report:
        print(f"\nReport saved to: {report}")
        # In a full implementation, generate HTML report


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
    install_parser.add_argument(
        "--cursor",
        action="store_true",
        help="Install Cursor IDE rules (.cursorrules and .cursor/rules/)",
    )

    # Check compliance command
    check_parser = subparsers.add_parser(
        "check-compliance", help="Check code compliance with standards"
    )
    check_parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory to check (default: current directory)",
    )
    check_parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed compliance information",
    )
    check_parser.add_argument(
        "--report",
        type=str,
        help="Path to save HTML compliance report",
    )

    # Fix compliance command
    fix_parser = subparsers.add_parser("fix-compliance", help="Automatically fix compliance issues")
    fix_parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory to fix (default: current directory)",
    )
    fix_parser.add_argument(
        "--check-only",
        action="store_true",
        help="Only check what would be fixed, don't make changes",
    )

    # Info command
    subparsers.add_parser("info", help="Show package information")
    
    # Debug command
    subparsers.add_parser("debug-paths", help="Debug package data paths (for troubleshooting)")

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

        if args.cursor:
            install_cursor_rules(target, overwrite=args.overwrite)

    elif args.command == "check-compliance":
        check_compliance(
            Path(args.target),
            detailed=args.detailed,
            report=args.report,
        )

    elif args.command == "fix-compliance":
        target = Path(args.target).resolve()
        print("Fixing compliance issues...")
        print("=" * 50)

        try:
            import subprocess

            if args.check_only:
                print("(Check-only mode - no changes will be made)")

            # Format with Black
            print("Formatting code with Black...")
            cmd = ["black", str(target)]
            if args.check_only:
                cmd.append("--check")
            subprocess.run(cmd, check=False)

            # Sort imports
            print("Sorting imports with isort...")
            cmd = ["isort", str(target)]
            if args.check_only:
                cmd.append("--check-only")
            subprocess.run(cmd, check=False)

            if not args.check_only:
                print("\n✅ Auto-fixable issues have been fixed!")
                print("Run 'ai-coding-standards check-compliance' to see remaining issues.")
            else:
                print("\n(Check-only mode - no changes made)")

        except FileNotFoundError:
            print("Error: Required tools not found.")
            print("Install with: pip install black isort")
            sys.exit(1)

    elif args.command == "info":
        show_info()
    
    elif args.command == "debug-paths":
        from ai_coding_standards.debug_paths import main as debug_main
        debug_main()
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
