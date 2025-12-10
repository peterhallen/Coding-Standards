# JavaScript/TypeScript Coding Standards

## Table of Contents

1. [Introduction](#introduction)
2. [Tooling](#tooling)
3. [General Principles](#general-principles)
4. [Code Organization](#code-organization)
5. [Naming Conventions](#naming-conventions)
6. [TypeScript Specifics](#typescript-specifics)
7. [Error Handling](#error-handling)
8. [Testing](#testing)

---

## Introduction

### Purpose

These standards ensure that JavaScript and TypeScript code across our projects is consistent, maintainable, and less prone to bugs. They are designed to be followed by both human developers and AI coding assistants.

### Scope

These standards apply to all JavaScript and TypeScript projects, including Node.js backends, React frontends, and utility libraries. **TypeScript is preferred** for all new projects.

---

## Tooling

We rely on automated tooling to enforce many of these standards.

1.  **TypeScript**: All new code should be written in TypeScript.
2.  **ESLint**: Lints code for bugs and quality issues.
3.  **Prettier**: Handles code formatting (indentation, semicolons, quotes).

### Configuration

Standard configuration files are provided by this package:
-   `.eslintrc.json`: Recommended ESLint rules.
-   `.prettierrc.json`: Prettier settings (2 spaces, single quotes, trailing commas).
-   `tsconfig.json`: Strict type checking enabled.

**Note**: Do not disable linting rules inline (`// eslint-disable-line`) without a compelling reason and a comment explanation.

---

## General Principles

### 1. Modern JavaScript (ES6+)

Use modern syntax features that improve readability and safety.

-   **Variables**: Use `const` by default. Use `let` only if reassignment is strictly necessary. Never use `var`.
-   **Functions**: Use arrow functions for callbacks and functional components.
    ```typescript
    // Good
    const add = (a: number, b: number) => a + b;
    items.map(item => item.id);
    
    // Bad
    var that = this; // Avoid 'this' aliasing, use arrows
    ```
-   **Template Literals**: Use backticks for string interpolation.
    ```typescript
    // Good
    const greeting = `Hello, ${name}`;
    ```
-   **Destructuring**: Use object and array destructuring.
    ```typescript
    // Good
    const { name, age } = user;
    const [first, second] = items;
    ```

### 2. Functional Style

Prefer functional programming patterns over imperative loops when appropriate.

-   Use `.map()`, `.filter()`, `.reduce()`, `.find()` instead of explicit `for` loops for array transformations.
-   Keep functions pure (same output for same input, minimal side effects) where possible.

### 3. Immutability

Avoid mutating objects and arrays directly.

```typescript
// Good
const newItems = [...items, newItem];
const updatedUser = { ...user, age: 25 };

// Bad
items.push(newItem);
user.age = 25;
```

---

## Code Organization

### Module Structure

1.  **Imports**: Group external imports first, then internal/relative imports.
2.  **Types/Interfaces**: Define local types at the top or in a separate file if shared.
3.  **Constants**: Module-level constants.
4.  **Main Function/Component**: The primary export of the file.
5.  **Helper Functions**: Private helpers at the bottom.

### Component Structure (React)

Create small, focused components.

```typescript
// components/UserProfile.tsx

import React from 'react';
import { User } from '../types';
import { formatDate } from '../utils/date';

interface UserProfileProps {
  user: User;
  onEdit: () => void;
}

export const UserProfile: React.FC<UserProfileProps> = ({ user, onEdit }) => {
  return (
    <div className="user-profile">
      <h2>{user.name}</h2>
      <p>Joined: {formatDate(user.joinedAt)}</p>
      <button onClick={onEdit}>Edit Profile</button>
    </div>
  );
};
```

---

## Naming Conventions

### General

-   **Files**: `kebab-case.ts` (e.g., `user-profile.ts`) or `PascalCase.tsx` for React components.
-   **Variables/Functions**: `camelCase` (e.g., `fetchUserData`, `isActive`).
-   **Classes/Interfaces/Types**: `PascalCase` (e.g., `UserRequest`, `IUser`).
-   **Constants**: `UPPER_SNAKE_CASE` for global/static constants (e.g., `MAX_RETRIES`). `camelCase` for constants that are just immutable variables.

### Boolean Variables

Prefix boolean variables with `is`, `has`, `should`, or `can` to indicate they are flags.

```typescript
// Good
const isVisible = true;
const hasAccess = false;

// Bad
const visible = true; // Is this a boolean or the visible object?
const access = false;
```

### Event Handlers

Naming convention should follow `handle[Event]` pattern.

```typescript
// Good
const handleSubmit = () => { ... };
<button onClick={handleSubmit} />
```

---

## TypeScript Specifics

### 1. Strict Typing

-   **Avoid `any`**: The usage of `any` defeats the purpose of TypeScript. Use `unknown` if the type is truly not known yet, and narrow it down later.
-   **No Implicit Any**: `tsconfig.json` should have `noImplicitAny: true`.

### 2. Interfaces vs Types

-   Use **Interfaces** for defining public API shapes and object structures (they can be extended).
-   Use **Types** for unions, intersections, primitives, and complex utility types.

### 3. Return Types

Explicitly annotate return types for exported functions. This prevents accidental API changes.

```typescript
// Good
export const getUser = (id: string): Promise<User> => { ... };
```

### 4. Optional Chaining & Nullish Coalescing

Use `?.` and `??` to handle null/undefined safely.

```typescript
const cityName = user?.address?.city ?? 'Unknown City';
```

---

## Error Handling

### Async/Await

Use `try/catch` blocks for async operations.

```typescript
async function loadData() {
  try {
    const data = await api.fetchData();
    return data;
  } catch (error) {
    if (error instanceof ApiError) {
      // Handle specific API error
      console.error('API Error:', error.message);
    } else {
      // Handle generic error
      console.error('Unexpected error:', error);
    }
    throw error; // Re-throw if the caller needs to handle it
  }
}
```

### Throwing Errors

Throw proper `Error` objects, not strings.

```typescript
// Good
throw new Error('User not found');

// Bad
throw 'User not found';
```

---

## Testing

### Principles

1.  **Unit Tests**: Test individual functions and components in isolation.
2.  **Testing Library**: Use `@testing-library/react` for React components. Test behavior, not implementation details.
3.  **Mocking**: Mock external dependencies (API calls) to keep tests fast and deterministic.

### Example

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { Counter } from './Counter';

test('increments count when button is clicked', () => {
  render(<Counter />);
  
  const button = screen.getByText(/increment/i);
  fireEvent.click(button);
  
  expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
});
```
