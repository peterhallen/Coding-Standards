# Sensitive Data Pre-commit Hook Guide

This guide details the usage, configuration, and troubleshooting of the sensitive data pre-commit hook included in this repository.

## Overview

The sensitive data pre-commit hook is designed to prevent accidental commits of Protected Health Information (PHI), Personally Identifiable Information (PII), and other sensitive data formats common in healthcare (HL7, MDS).

### What It Detects

1.  **HL7 Messages**
    *   **Pattern**: Lines starting with 3 uppercase letters followed by a pipe (e.g., `MSH|`, `PID|`).
    *   **Reason**: HL7 messages often contain raw patient data.

2.  **MDS 3.0 Assessments**
    *   **Pattern**: Sample structure markers like `A0100.`, `B0100.`, and headers like `MINIMUM DATA SET (MDS)` or `Section A - Identification Information`.
    *   **Reason**: MDS assessments contain detailed resident information.

3.  **PHI/PII Keywords**
    *   **Keywords**: "Social Security Number", "Medicare Number", "Resident Name", "Date of Birth".
    *   **Reason**: Explicit mentions of these fields often indicate hardcoded personal data.

4.  **Sensitive File Extensions**
    *   blocked by `.gitignore`: `*.hl7`, `*.mds`, `*.pem`, `*.key`, `*.p12`, `*.pfX` (case-insensitive via OS/git).

## Installation

The hook is part of the repository's pre-commit configuration.

1.  **Install pre-commit** (if not already installed):
    ```bash
    pip install pre-commit
    ```

2.  **Install the git hooks**:
    ```bash
    pre-commit install
    ```

Once installed, the hook will run automatically on every `git commit`.

## Usage

### Automatic Checking
When you run `git commit`, the hook scans the staged files.

*   **Pass**: If no sensitive patterns are found, the commit proceeds.
*   **Fail**: If sensitive patterns are found, the commit is **blocked** and an error message is displayed showing the file and line number.

**Example Failure:**
```text
[ERROR] Sensitive data pattern found in data/sample.hl7 at line 1:
    Line content: MSH|^~\&|EPIC|EPICADT|SMS|SMSADT|199912271408|CHARRIS|ADT^A04|...
Commit rejected: Sensitive data usage detected.
```

### Manual Checking
You can run the hook manually against all files (useful for checking existing code):

```bash
pre-commit run check-sensitive-data --all-files
```

## Troubleshooting & False Positives

### "I validly need to commit this data"

If you are committing **synthentic**, **anonymized**, or **test** data that triggers the hook, you have two options:

1.  **Modify the Data (Recommended)**: Change the data so it doesn't match the strict regex. For example, change `Social Security Number` to `SSN_Field` in your test constants.
2.  **Skip the Hook (Use with Caution)**:
    If you are absolutely sure the data is safe to commit, you can bypass the hook for a specific commit:
    ```bash
    git commit -n -m "Commit message"
    # or
    git commit --no-verify -m "Commit message"
    ```
    > **Warning**: This skips ALL pre-commit hooks, including linting and formatting.

### "The hook is missing my file"

The hook is configured to check specific file types. Check `.pre-commit-config.yaml` to see the `types` or `files` configuration. By default, it checks text-based files (`py`, `md`, `txt`, `json`, `xml`, `hl7`).

## Configuration

The hook is defined in `.pre-commit-config.yaml` under the `repo: local` section:

```yaml
- repo: local
  hooks:
    - id: check-sensitive-data
      name: check sensitive data
      entry: python src/ai_coding_standards/pre_commit/sensitive_data_check.py
      language: system
      types: [text]
      exclude: ^(src/ai_coding_standards/pre_commit/sensitive_data_check\.py|tests/.*)$
```

### Exclusions
Files in `tests/` and the script itself are excluded by default to allow for testing the detector. If you need to exclude a specific secure data file, add it to the `exclude` regex.

## Development

The detection logic is located in:
`src/ai_coding_standards/pre_commit/sensitive_data_check.py`

To add new patterns:
1.  Open the script.
2.  Add a new `re.compile(...)` entry to the `SENSITIVE_PATTERNS` list.
3.  Add a test case in `tests/test_sensitive_data_check.py`.
