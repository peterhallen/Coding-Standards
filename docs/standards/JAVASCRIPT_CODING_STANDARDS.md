# JavaScript/TypeScript Coding Standards

This document outlines the coding standards for JavaScript and TypeScript projects.

## Tooling
- **Linting**: ESLint (standard config provided)
- **Formatting**: Prettier
- **Type Checking**: TypeScript (strict mode)

## General Principles
1.  Use `const` by default, `let` if reassignment is needed. Avoid `var`.
2.  Use arrow functions for callbacks.
3.  Prefer async/await over raw promises.
4.  Use strict equality (`===`).

## TypeScript
1.  Avoid `any`. Use `unknown` if type is truly uncertain.
2.  Define interfaces for objects.
3.  Use explicit return types for exported functions.
