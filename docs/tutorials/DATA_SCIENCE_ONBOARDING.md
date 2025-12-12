# Data Science Onboarding: Protecting Sensitive Data

Welcome to the Coding Standards project! This module is designed to help you commit code safely by automatically detecting sensitive data (PII/PHI) before it enters the repository.

## The Object Lesson: A "Live" Demo

This tutorial walks you through a simulated scenario where you accidentally attempt to commit sensitive patient assessment data (MDS), and how the system protects you.

### Scenario
You are processing Minimum Data Set (MDS 3.0) assessments and have saved a raw export and meeting notes in your workspace.

### Step 1: Attempting to Commit Sensitive Data

Imagine you have created the following files:

1.  `mds_assessment.txt`: Contains a raw MDS 3.0 form with identifying headers and resident names.
2.  `notes.txt`: Contains notes mentioning specific MDS sections and PII fields.

When you run `git commit`, the **Sensitive Data Hook** runs automatically.

**Output:**
```
[ERROR] Sensitive data pattern found in examples/data_science_demo/mds_assessment.txt at line 1:
    Line content: MINIMUM DATA SET (MDS) - Version 3.0...
[ERROR] Sensitive data pattern found in examples/data_science_demo/mds_assessment.txt at line 2:
    Line content: Section A - Identification Information...
[ERROR] Sensitive data pattern found in examples/data_science_demo/mds_assessment.txt at line 4:
    Line content: A0100. Facility Provider Numbers...
[ERROR] Sensitive data pattern found in examples/data_science_demo/notes.txt at line 7:
    Line content: 2. Check if we are incorrectly parsing 'Social Security Number' fields...

Commit rejected: Sensitive data usage detected.
Please remove the sensitive data before committing.
```

### Step 2: Remediation

To fix this, you must **remove** or **obfuscate** the sensitive data.

1.  **Delete** `mds_assessment.txt` (Raw identification data should never be in the repo!).
2.  **Edit** `notes.txt` to replace specific PHI terms with generic ones (e.g., "SSN", "Indentifiers").

### Step 3: Success

After cleaning up your files, run the commit again.

**Output:**
```
check sensitive data.....................................................Passed
```

## Key Takeaways
- **Structural Detection**: The hook detects MDS 3.0 distinct markers like `Section A - Identification Information` and Item tags (`A0100.`).
- **Keyword Detection**: The hook looks for protected terms like "Social Security Number".
- **Best Practice**: Process identifying data in a secure, designated environment, not in the git repository.

## Running this Simulation
You can run this check manually at any time on your files:
```bash
pre-commit run check-sensitive-data --all-files
```
