# Markdown Standards - Quick Reference

> One-page reference for documentation standards. See `MARKDOWN_STANDARDS.md` for full documentation.

## Document Structure

```
# Title (H1 - one per document)

Brief description.

## Table of Contents (if 3+ sections)

---

## Major Section (H2)

### Subsection (H3)

---

## Another Section

---

**Last Updated**: YYYY-MM-DD  
**Version**: X.Y.Z
```

## Heading Rules

| Level | Usage | Example |
|-------|-------|---------|
| H1 `#` | Document title only | `# Installation Guide` |
| H2 `##` | Major sections | `## Prerequisites` |
| H3 `###` | Subsections | `### Windows Setup` |
| H4 `####` | Rare - sub-subsections | `#### Environment Variables` |

- ✅ One H1 per document
- ✅ Sequential hierarchy (don't skip levels)
- ✅ Sentence case
- ❌ No trailing punctuation (except `?` for FAQ)

## Text Formatting

| Style | Syntax | Use For |
|-------|--------|---------|
| **Bold** | `**text**` | Important terms, warnings |
| *Italic* | `*text*` | Introducing terms, emphasis |
| `Code` | `` `text` `` | Files, commands, code |
| ~~Strike~~ | `~~text~~` | Deprecated (sparingly) |

## Lists

**Unordered:**
```markdown
- Item one
- Item two
  - Nested item
```

**Ordered:**
```markdown
1. First step
2. Second step
   1. Sub-step
```

**Checklist:**
```markdown
- [ ] Incomplete
- [x] Complete
```

## Code Blocks

Always specify language:

````markdown
```python
def example():
    return "Hello"
```
````

Common languages: `python`, `bash`, `json`, `yaml`, `javascript`, `sql`

## Tables

```markdown
| Left | Center | Right |
|:-----|:------:|------:|
| Text | Text   |   123 |
```

## Links

```markdown
[Display text](path/to/file.md)           <!-- File link -->
[Section link](#section-name)             <!-- Same-page anchor -->
[External](https://example.com)           <!-- External URL -->
```

- ✅ Descriptive link text
- ❌ Avoid "click here", "this link"

## Images

```markdown
![Descriptive alt text](path/to/image.png)
```

## Callouts

```markdown
> **Note**: Additional information.

> ⚠️ **Warning**: Potential issues.

> 💡 **Tip**: Helpful suggestion.
```

## Emoji Usage

| Emoji | Meaning |
|-------|---------|
| ✅ | Do this / Correct |
| ❌ | Don't do this |
| ⚠️ | Warning |
| 💡 | Tip |
| 📝 | Note |
| 🚀 | Quick start |
| 🛠️ | Tools/Config |

Use in section headers and callouts only. Never in code.

## File Naming

| Type | Pattern | Example |
|------|---------|---------|
| Root standards | `UPPER_CASE.md` | `README.md`, `CONTRIBUTING.md` |
| Policy docs | `UPPER_SNAKE.md` | `CODING_STANDARDS.md` |
| General docs | `kebab-case.md` | `getting-started.md` |

## Section Separators

- ✅ Use `---` between H2 sections
- ❌ Don't use between H3 subsections
- ✅ Blank line before and after `---`

## Good/Bad Pattern

```markdown
**Good:**
\`\`\`python
# Correct approach
\`\`\`

**Bad:**
\`\`\`python
# Incorrect approach
\`\`\`
```

## Quick Checklist

- [ ] Single H1 title
- [ ] Table of contents (if 3+ sections)
- [ ] No skipped heading levels
- [ ] `---` between major sections only
- [ ] Code blocks have language
- [ ] Descriptive link text
- [ ] Images have alt text
- [ ] Consistent emoji usage
- [ ] Last updated date

---

**Full Documentation**: See `MARKDOWN_STANDARDS.md`

