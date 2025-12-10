# Markdown Documentation Standards

## Table of Contents

1. [Introduction](#introduction)
2. [Document Structure](#document-structure)
3. [Headings](#headings)
4. [Text Formatting](#text-formatting)
5. [Lists](#lists)
6. [Code Blocks](#code-blocks)
7. [Tables](#tables)
8. [Links and References](#links-and-references)
9. [Images](#images)
10. [Admonitions and Callouts](#admonitions-and-callouts)
11. [Emoji Usage](#emoji-usage)
12. [File Naming](#file-naming)
13. [Document Types](#document-types)
14. [Accessibility](#accessibility)
15. [Quick Reference](#quick-reference)

---

## Introduction

### Purpose

This document establishes standards for writing Markdown documentation across all projects. Consistent documentation improves readability, maintainability, and professionalism.

### Scope

These standards apply to:
- README files
- Documentation files (`*.md`)
- Changelog files
- Contributing guides
- API documentation
- Tutorial content

### Principles

- **Clarity**: Write for your audience, not yourself
- **Consistency**: Use the same patterns throughout
- **Scannability**: Enable readers to quickly find information
- **Accessibility**: Ensure content is accessible to all readers
- **Maintainability**: Keep documentation easy to update

---

## Document Structure

### Required Elements

Every documentation file should include:

1. **Title** (H1) - Clear, descriptive document title
2. **Table of Contents** - For documents with 3+ sections
3. **Introduction/Overview** - What the document covers
4. **Main Content** - Organized into logical sections
5. **Footer** - Last updated date and version (for versioned docs)

### Standard Template

```markdown
# Document Title

Brief description of what this document covers (1-2 sentences).

## Table of Contents

1. [Section One](#section-one)
2. [Section Two](#section-two)
3. [Section Three](#section-three)

---

## Section One

### Subsection

Content here...

---

## Section Two

Content here...

---

**Last Updated**: YYYY-MM-DD  
**Version**: X.Y.Z
```

### Section Separators

- Use horizontal rules (`---`) between major sections (H2 level)
- Do NOT use horizontal rules between subsections (H3, H4)
- Place a blank line before and after horizontal rules

**Good:**
```markdown
## Section One

Content for section one...

---

## Section Two

Content for section two...
```

**Bad:**
```markdown
## Section One

Content...
---
### Subsection
---
More content...
```

---

## Headings

### Heading Hierarchy

| Level | Usage | Example |
|-------|-------|---------|
| H1 (`#`) | Document title only | `# Installation Guide` |
| H2 (`##`) | Major sections | `## Prerequisites` |
| H3 (`###`) | Subsections | `### Windows Setup` |
| H4 (`####`) | Sub-subsections (use sparingly) | `#### Environment Variables` |
| H5/H6 | Avoid - indicates need to restructure | - |

### Heading Rules

1. **One H1 per document** - The document title only
2. **Sequential hierarchy** - Don't skip levels (H2 → H4)
3. **Descriptive text** - Use clear, action-oriented headings
4. **No trailing punctuation** - Except question marks for FAQ
5. **Sentence case** - Capitalize first word and proper nouns only

**Good:**
```markdown
# User authentication guide

## Prerequisites

### System requirements

#### Minimum specifications
```

**Bad:**
```markdown
# User Authentication Guide:

#### System Requirements   <!-- Skipped H2 and H3 -->

### prerequisites          <!-- Inconsistent capitalization -->
```

### Heading Formatting

- Leave one blank line before headings
- Leave one blank line after headings
- Don't use bold or italic in headings
- Keep headings under 60 characters

```markdown
Some paragraph content here.

## Next Section

Content for this section...
```

---

## Text Formatting

### Emphasis

| Style | Syntax | Usage |
|-------|--------|-------|
| **Bold** | `**text**` | Key terms, important warnings |
| *Italic* | `*text*` | Emphasis, introducing terms |
| `Code` | `` `text` `` | File names, commands, code elements |
| ~~Strikethrough~~ | `~~text~~` | Deprecated content (use sparingly) |

### Usage Guidelines

**Bold** - Use for:
- Important warnings or notes
- UI elements users must interact with
- Key terms on first use

*Italic* - Use for:
- Introducing new terms
- Titles of books/articles
- Slight emphasis

`Code formatting` - Use for:
- File names: `config.yaml`
- Directory paths: `src/utils/`
- Commands: `pip install`
- Function/method names: `calculate_total()`
- Variable names: `user_id`
- Code keywords: `True`, `None`

### Paragraph Guidelines

- Keep paragraphs to 3-5 sentences
- One idea per paragraph
- Use blank lines between paragraphs
- Line length: 80-100 characters (for readability in editors)

**Good:**
```markdown
The configuration file controls all application settings. You can find it
at `config/settings.yaml` in the project root.

Each setting is documented with inline comments. Modify values as needed
for your environment.
```

**Bad:**
```markdown
The configuration file controls all application settings. You can find it at config/settings.yaml in the project root. Each setting is documented with inline comments. Modify values as needed for your environment. Make sure to restart the application after making changes. The default values work for most use cases but you may need to adjust them for production deployments.
```

---

## Lists

### Unordered Lists

Use for items without inherent order:

```markdown
- First item
- Second item
- Third item
  - Nested item
  - Another nested item
- Fourth item
```

**Formatting rules:**
- Use `-` consistently (not `*` or `+`)
- One space after the dash
- Indent nested items with 2 spaces
- Keep items parallel in structure

### Ordered Lists

Use for sequential steps or ranked items:

```markdown
1. First step
2. Second step
3. Third step
   1. Sub-step one
   2. Sub-step two
4. Fourth step
```

**Formatting rules:**
- Use `1.` for all items (auto-numbered on render)
- Indent nested items with 3 spaces
- Use for procedures, rankings, or sequences

### Checklists

Use for tasks or requirements:

```markdown
- [ ] Incomplete task
- [x] Completed task
- [ ] Another incomplete task
```

### Definition Lists

For term/definition pairs (if supported):

```markdown
Term 1
: Definition for term 1

Term 2
: Definition for term 2
```

Or use bold for terms:

```markdown
**Term 1**: Definition for term 1

**Term 2**: Definition for term 2
```

### List Content Guidelines

- Start items with capital letters
- Use consistent punctuation:
  - No punctuation for short items (phrases)
  - Periods for complete sentences
- Keep list items parallel in structure

**Good:**
```markdown
The system supports:

- User authentication
- Role-based access control
- Session management
- Audit logging
```

**Bad:**
```markdown
The system supports:

- authenticating users.
- Role-based Access Control
- it manages sessions
- Audit logging is included
```

---

## Code Blocks

### Inline Code

Use backticks for inline code:

```markdown
Run `pip install package` to install.

The `config.yaml` file contains settings.

Set `DEBUG=True` for development.
```

### Fenced Code Blocks

Always specify the language for syntax highlighting:

````markdown
```python
def hello_world():
    """Print a greeting."""
    print("Hello, World!")
```
````

### Supported Languages

Use these language identifiers:

| Language | Identifier |
|----------|------------|
| Python | `python` |
| JavaScript | `javascript` or `js` |
| TypeScript | `typescript` or `ts` |
| Bash/Shell | `bash` or `shell` |
| JSON | `json` |
| YAML | `yaml` |
| Markdown | `markdown` or `md` |
| SQL | `sql` |
| HTML | `html` |
| CSS | `css` |
| Plain text | `text` or omit |

### Code Block Guidelines

1. **Always specify language** - Enables syntax highlighting
2. **Keep blocks focused** - Show only relevant code
3. **Include comments** - Explain non-obvious parts
4. **Use realistic examples** - Avoid `foo`, `bar`, `baz`
5. **Show output** - Include expected output when helpful

**Good:**
````markdown
```python
def calculate_discount(price: float, percentage: float) -> float:
    """Calculate discounted price.
    
    Args:
        price: Original price
        percentage: Discount percentage (0-100)
    
    Returns:
        Price after discount
    """
    return price * (1 - percentage / 100)

# Example usage
final_price = calculate_discount(100.00, 15)
print(f"Final price: ${final_price:.2f}")  # Output: Final price: $85.00
```
````

**Bad:**
````markdown
```
def foo(x, y):
    return x * y
```
````

### Command Examples

For shell commands, show the prompt style consistently:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py --config config.yaml
```

For commands with output:

```bash
$ python --version
Python 3.12.0

$ pip list | grep requests
requests    2.31.0
```

---

## Tables

### Table Structure

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### Column Alignment

```markdown
| Left-aligned | Center-aligned | Right-aligned |
|:-------------|:--------------:|--------------:|
| Left         | Center         | Right         |
| Text         | Text           | 123           |
```

### Table Guidelines

1. **Use for structured data** - Comparisons, specifications, mappings
2. **Keep tables simple** - Max 5-6 columns
3. **Align columns** - Improve source readability
4. **Include headers** - Always describe columns
5. **Keep cells concise** - Use notes for details

**Good:**
```markdown
| Metric | Maximum | Preferred | Notes |
|--------|--------:|----------:|-------|
| Function length | 50 lines | 30 lines | Extract helpers if exceeded |
| Parameters | 5 | 3 | Use dataclass for more |
| Complexity | 10 | 5 | Refactor if exceeded |
```

**When NOT to use tables:**
- Simple key-value pairs (use definition lists)
- Long text content (use sections)
- Code examples (use code blocks)

---

## Links and References

### Link Types

**Inline links:**
```markdown
See the [Installation Guide](INSTALLATION.md) for setup instructions.
```

**Reference links (for repeated URLs):**
```markdown
Read the [coding standards][standards] before contributing.

Check the [API documentation][api-docs] for details.

[standards]: CODING_STANDARDS.md
[api-docs]: https://api.example.com/docs
```

**Section links:**
```markdown
See [Error Handling](#error-handling) for details.
```

### Link Guidelines

1. **Use descriptive link text** - Not "click here" or "this link"
2. **Use relative paths** - For internal documentation
3. **Check links regularly** - Broken links frustrate readers
4. **Open external links appropriately** - Note if opens in new tab

**Good:**
```markdown
See the [Contributing Guide](CONTRIBUTING.md) for submission guidelines.

Review [Python type hints](https://docs.python.org/3/library/typing.html)
for syntax details.
```

**Bad:**
```markdown
Click [here](CONTRIBUTING.md) to read about contributing.

For more info, see [this](https://docs.python.org).
```

### File References

When referencing project files:

```markdown
- Configuration: [`config/settings.yaml`](config/settings.yaml)
- Main module: [`src/main.py`](src/main.py)
- Tests: [`tests/`](tests/)
```

---

## Images

### Image Syntax

```markdown
![Alt text describing the image](path/to/image.png)

![Architecture diagram showing system components](docs/images/architecture.png)
```

### Image Guidelines

1. **Always include alt text** - Describes image for accessibility
2. **Use relative paths** - Store images in `docs/images/` or similar
3. **Optimize file size** - Compress images appropriately
4. **Use descriptive filenames** - `user-flow-diagram.png` not `img1.png`
5. **Prefer SVG** - For diagrams and icons (scales better)

### Image Organization

```
project/
├── docs/
│   ├── images/
│   │   ├── architecture-overview.png
│   │   ├── user-flow-diagram.svg
│   │   └── screenshot-dashboard.png
│   └── guides/
│       └── getting-started.md
```

---

## Admonitions and Callouts

### Standard Callout Patterns

Use blockquotes with emoji or bold markers:

**Note/Info:**
```markdown
> **Note**: This feature requires Python 3.9 or later.
```

**Warning:**
```markdown
> ⚠️ **Warning**: This action cannot be undone.
```

**Tip:**
```markdown
> 💡 **Tip**: Use keyboard shortcuts to speed up your workflow.
```

**Important:**
```markdown
> 🔴 **Important**: Back up your data before proceeding.
```

**Example:**
```markdown
> **Example**: Here's how to configure the setting:
> ```yaml
> debug: true
> ```
```

### Callout Usage

| Type | Emoji | Use Case |
|------|-------|----------|
| Note | 📝 or none | Additional context, clarification |
| Tip | 💡 | Helpful suggestions, best practices |
| Warning | ⚠️ | Potential issues, cautions |
| Important | 🔴 or ❗ | Critical information |
| Success | ✅ | Confirmation, completion |
| Error | ❌ | Common mistakes, what to avoid |

---

## Emoji Usage

### Approved Emoji Set

Use emoji consistently for visual scanning:

| Emoji | Meaning | Example Usage |
|-------|---------|---------------|
| ✅ | Do this / Correct / Complete | Good practices |
| ❌ | Don't do this / Incorrect | Anti-patterns |
| ⚠️ | Warning / Caution | Important caveats |
| 💡 | Tip / Idea | Helpful suggestions |
| 📝 | Note / Documentation | Additional info |
| 🔴 | Critical / Important | Breaking changes |
| 🚀 | Quick start / Launch | Getting started |
| 📋 | List / Table of contents | Navigation |
| 🛠️ | Tools / Configuration | Setup sections |
| 📚 | Documentation / Learning | Reference sections |
| 🤖 | AI / Automation | AI-related content |
| 🔗 | Links / References | External resources |
| 📊 | Metrics / Data | Statistics, benchmarks |
| 👥 | Team / Community | Contributing, people |
| 🔄 | Update / Sync | Changelog, updates |

### Emoji Guidelines

1. **Use sparingly** - Enhance, don't overwhelm
2. **Be consistent** - Same emoji for same meaning
3. **Section headers** - Acceptable for visual navigation
4. **Body text** - Use only for callouts and emphasis
5. **Avoid in code** - Never in technical content

**Good:**
```markdown
## 🚀 Quick Start

## 📋 Table of Contents

> ⚠️ **Warning**: This is a breaking change.
```

**Bad:**
```markdown
## 🎉🚀✨ Getting Started! 🎊

Install the package 📦 by running 💻 this command ⌨️:
```

---

## File Naming

### Documentation File Names

| Pattern | Example | Use Case |
|---------|---------|----------|
| `UPPERCASE.md` | `README.md`, `CONTRIBUTING.md` | Root-level standard files |
| `UPPER_SNAKE.md` | `CODING_STANDARDS.md` | Standard/policy documents |
| `kebab-case.md` | `getting-started.md` | General documentation |
| `snake_case.md` | `api_reference.md` | Alternative (be consistent) |

### Standard File Names

| File | Purpose |
|------|---------|
| `README.md` | Project overview and quick start |
| `CONTRIBUTING.md` | How to contribute |
| `CHANGELOG.md` | Version history |
| `LICENSE` or `LICENSE.md` | License information |
| `CODE_OF_CONDUCT.md` | Community guidelines |
| `SECURITY.md` | Security policy |
| `INSTALLATION.md` | Detailed setup instructions |

### Directory Structure

```
docs/
├── README.md              # Documentation index
├── getting-started.md     # Quick start guide
├── guides/
│   ├── installation.md
│   ├── configuration.md
│   └── deployment.md
├── reference/
│   ├── api.md
│   └── cli.md
└── images/
    └── ...
```

---

## Document Types

### README Files

**Required sections:**
1. Project title and description
2. Quick start / Installation
3. Usage examples
4. Documentation links
5. Contributing info
6. License

**Template:**
```markdown
# Project Name

Brief description of what the project does.

## 🚀 Quick Start

\`\`\`bash
pip install project-name
\`\`\`

## 📖 Documentation

- [Installation Guide](docs/installation.md)
- [User Guide](docs/user-guide.md)
- [API Reference](docs/api.md)

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

[MIT License](LICENSE)
```

### How-To Guides

**Structure:**
1. Title with clear goal
2. Prerequisites
3. Step-by-step instructions
4. Verification/testing
5. Troubleshooting (optional)

### Reference Documentation

**Structure:**
1. Overview
2. API/CLI reference (alphabetical or logical grouping)
3. Examples for each item
4. Related links

### Changelogs

**Format (Keep a Changelog style):**
```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New feature description

### Changed
- Changed behavior description

### Fixed
- Bug fix description

## [1.0.0] - 2025-01-15

### Added
- Initial release features
```

---

## Accessibility

### Writing for Accessibility

1. **Use descriptive link text** - Screen readers announce link text
2. **Add alt text to images** - Describe what the image shows
3. **Use semantic structure** - Proper heading hierarchy
4. **Avoid "click here"** - Use meaningful link descriptions
5. **Don't rely on color alone** - Use text + emoji/icons

### Alt Text Guidelines

**Good alt text:**
```markdown
![Flowchart showing user authentication process with login, validation, and session creation steps](images/auth-flow.png)
```

**Bad alt text:**
```markdown
![image](images/auth-flow.png)
![flow](images/auth-flow.png)
```

### Heading Structure

Screen readers use headings for navigation. Ensure:
- Logical hierarchy (H1 → H2 → H3)
- Descriptive heading text
- No skipped levels

---

## Quick Reference

### Document Checklist

- [ ] Single H1 title at top
- [ ] Table of contents (if 3+ sections)
- [ ] Logical heading hierarchy
- [ ] Horizontal rules between major sections only
- [ ] Code blocks have language specified
- [ ] Links use descriptive text
- [ ] Images have alt text
- [ ] Consistent emoji usage
- [ ] Last updated date (for versioned docs)

### Formatting Cheat Sheet

| Element | Syntax |
|---------|--------|
| Bold | `**text**` |
| Italic | `*text*` |
| Code | `` `code` `` |
| Link | `[text](url)` |
| Image | `![alt](path)` |
| Heading | `## Heading` |
| List item | `- item` |
| Numbered | `1. item` |
| Checkbox | `- [ ] task` |
| Quote | `> quote` |
| HR | `---` |

### Common Patterns

**Good/Bad examples:**
```markdown
**Good:**
\`\`\`python
# Good code example
\`\`\`

**Bad:**
\`\`\`python
# Bad code example
\`\`\`
```

**Comparison table:**
```markdown
| Aspect | Option A | Option B |
|--------|----------|----------|
| Speed | Fast | Slow |
| Cost | Low | High |
```

**Step-by-step:**
```markdown
1. First, do this
2. Then, do that
3. Finally, verify
```

---

**Last Updated**: 2025-12-08  
**Version**: 1.0.0

