"""
cx_Freeze setup script for building Windows MSI installer.

Build with: python setup_msi.py bdist_msi
"""

import sys
from pathlib import Path

from cx_Freeze import Executable, setup

# Determine base for Windows GUI/Console
base = None
if sys.platform == "win32":
    base = "Console"  # Use "Win32GUI" for GUI apps

# Include files that should be bundled
include_files = [
    # Configuration files
    (".editorconfig", "data/.editorconfig"),
    (".flake8", "data/.flake8"),
    (".pylintrc", "data/.pylintrc"),
    (".cursorrules", "data/.cursorrules"),
    (".pre-commit-config.yaml", "data/.pre-commit-config.yaml"),
    # Cursor rules
    (".cursor/rules", "data/.cursor/rules"),
    # Antigravity rules
    (".antigravity/rules", "data/.antigravity/rules"),
    # Agent OS standards
    ("agent-os/standards", "data/agent-os/standards"),
    # ChatGPT instructions
    (".chatgpt", "data/.chatgpt"),
    # Copilot instructions
    (".github/copilot-instructions.md", "data/.github/copilot-instructions.md"),
    # Documentation
    ("docs/standards", "data/docs/standards"),
    ("docs/guides", "data/docs/guides"),
    # Package data
    ("src/coding_standards/data", "lib/coding_standards/data"),
]

# Filter to only include files/dirs that exist
filtered_include_files = []
for src, dest in include_files:
    src_path = Path(src)
    if src_path.exists():
        filtered_include_files.append((str(src_path), dest))

# Build options
build_exe_options = {
    "packages": [
        "coding_standards",
        "argparse",
        "pathlib",
        "shutil",
        "importlib",
    ],
    "excludes": [
        "tkinter",
        "unittest",
        "email",
        "html",
        "http",
        "xml",
        "pydoc",
        "doctest",
        "ftplib",
        "bdb",
        "tarfile",
    ],
    "include_files": filtered_include_files,
    "include_msvcr": True,
}

# MSI options
bdist_msi_options = {
    "upgrade_code": "{A5C8F5E2-4D3B-4E5F-9A1C-2B3D4E5F6A7B}",
    "add_to_path": True,
    "initial_target_dir": r"[ProgramFilesFolder]\CodingStandards",
    "all_users": True,
}

# Executable definition
executables = [
    Executable(
        script="src/coding_standards/cli.py",
        base=base,
        target_name="coding-standards.exe",
        icon=None,  # Add icon path here if you have one
        shortcut_name="Coding Standards",
        shortcut_dir="ProgramMenuFolder",
    )
]

setup(
    name="coding-standards",
    version="1.1.0",
    description="Coding standards and best practices for Python development with AI assistants",
    author="Coding Standards Team",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
    executables=executables,
)
