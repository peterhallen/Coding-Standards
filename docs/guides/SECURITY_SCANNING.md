# Security Scanning Guide

This guide explains how to use the automated security scanning tools included in this project to prevent credentials and sensitive data from being committed to the repository.

## Overview

We use two complementary tools to protect our codebase:
1.  **detect-secrets (Yelp)**: Scans for high-entropy strings, secrets, API keys, and passwords.
2.  **Sensitive Data Hook (Custom)**: Scans for healthcare-specific data (HL7, MDS, PHI keys).

## Tool 1: detect-secrets

[Yelp's detect-secrets](https://github.com/Yelp/detect-secrets) is a pre-commit hook that spots potential secrets.

### How it Works
It uses "baselining". A `.secrets.baseline` file sits in the repo root. This file lists all "known" potential secrets that are currently allowed (e.g., false positives or legacy debt).
*   **If you add a NEW secret**: The hook FAILS because it's not in the baseline.
*   **If you change existing code**: The hook passes, as long as you don't introduce new secrets.

### Handling "Secret Detected" Errors

If `git commit` fails with a `detect-secrets` error:

1.  **Is it a real secret?**
    *   **YES**: Remove it. Use environment variables (from `.env` or AWS Secrets Manager) instead.
    *   **NO (False Positive)**: If it's a random string (like a test hash) that isn't a credential:
        1.  Run the audit tool:
            ```bash
            detect-secrets audit .secrets.baseline
            ```
        2.  Follow the prompts to label the item as a false positive (y/n).
        3.  Commit the updated `.secrets.baseline` file.

## Tool 2: Sensitive Data Hook

See [SENSITIVE_DATA_HOOK.md](SENSITIVE_DATA_HOOK.md) for details on healthcare-specific scanning.

## Daily Workflow for Developers

### 1. Installation
The hooks are installed automatically with:
```bash
coding-standards install --pre-commit
# or directly:
pre-commit install
```

### 1a. Adding to an Existing Repository (CRITICAL)
If you are adding this to a repo that already has code:

1.  **Do NOT** just install the hook yet (it may block your implementation if you have legacy secrets).
2.  **Generate the Baseline** first:
    ```bash
    detect-secrets scan > .secrets.baseline
    ```
3.  **Audit the Baseline**:
    ```bash
    detect-secrets audit .secrets.baseline
    ```
    Mark true false positives with `y`.
    Mark actual secrets with `n` (and plan to rotate/remove them).
4.  **Commit the Baseline**:
    ```bash
    git add .secrets.baseline
    git commit -m "Security: Add secrets baseline"
    ```
5.  **NOW Install the Hook**:
    ```bash
    pre-commit install
    ```
    Future commits will now check against this baseline.

### 2. Manual Scanning
You can scan all files at any time:
```bash
pre-commit run detect-secrets --all-files
pre-commit run check-sensitive-data --all-files
```

### 3. Updating the Baseline
If you need to refresh the baseline from scratch (use with caution):
```bash
detect-secrets scan > .secrets.baseline
```
Then review/audit the new baseline.
