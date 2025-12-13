# Opencode Support

## Overview

This repository now explicitly supports **opencode** as an AI coding assistant, alongside existing support for tools such as Cursor and GitHub Copilot.

Support for opencode is implemented through a standardized `AGENTS.md` file, which provides a clear, authoritative contract for agent behavior. This ensures consistent expectations, enforcement, and outcomes regardless of which AI coding assistant is used.

---

## What Was Added

- A root-level `AGENTS.md` file defining agent rules and expectations
- Explicit compatibility with opencode’s agent discovery and execution model
- Alignment and feature parity with existing `.cursorrules` and `.cursor/rules/*.mdc`
- Clear build, lint, and test commands for agent execution

No existing Cursor or Copilot behavior was changed.

---

## How It Works

### AGENTS.md as the Entry Point

opencode agents automatically read `AGENTS.md` to understand:

- Which rules are authoritative
- How to build, lint, and test the codebase
- What coding standards must be followed
- What actions are prohibited (e.g. unrelated refactors, adding secrets)

The file intentionally **does not duplicate** detailed standards. Instead, it references existing rule sources to prevent drift and ambiguity.

---

## Rule Hierarchy

When an opencode agent operates in this repository, rules are applied in the following order:

1. User or system instructions
2. The most specific applicable `AGENTS.md`
3. `.cursorrules`
4. `.cursor/rules/*.mdc`
5. Documentation in `docs/guides/*`

This hierarchy matches existing Cursor behavior.

---

## Supported Agent Capabilities

With opencode enabled, agents are expected to:

- Make minimal, scoped changes
- Preserve existing architecture and patterns
- Use repository-defined tooling and configuration
- Run the narrowest relevant tests
- Respect CI, linting, and security hooks

Agents are explicitly prohibited from introducing new dependencies, changing public APIs, or fixing unrelated issues unless instructed.

---

## Why This Matters

By adding opencode support:

- Teams can use multiple AI coding assistants interchangeably
- Coding standards are enforced consistently across tools
- Agent behavior is predictable, auditable, and CI-aligned
- The repository becomes future-proof for additional agentic tools

---

## Adoption in Other Repositories

To enable opencode support elsewhere:

1. Copy `AGENTS.md` to the repository root
2. Ensure existing coding standards are referenced, not duplicated
3. Verify build, lint, and test commands are accurate
4. Validate behavior via CI

---

## Compatibility

The opencode integration is fully compatible with:

- Cursor
- GitHub Copilot (instruction-only mode)
- Human contributors

No editor-specific behavior is required.
