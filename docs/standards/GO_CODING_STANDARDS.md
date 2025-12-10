# Go Coding Standards

## Table of Contents

1. [Introduction](#introduction)
2. [Tooling](#tooling)
3. [General Principles](#general-principles)
4. [Code Organization](#code-organization)
5. [Naming Conventions](#naming-conventions)
6. [Error Handling](#error-handling)
7. [Concurrency](#concurrency)
8. [Performance](#performance)

---

## Introduction

### Purpose

These standards aim to maintain idiomatic, readable, and efficient Go code. They draw heavily from "Effective Go" and common industry practices.

### Scope

These standards apply to all Go microservices, tools, and libraries developed within the organization.

---

## Tooling

All Go code must check against standard tools before being merged.

1.  **Format**: `gofmt` (or `goimports`) must be run on all code.
2.  **Lint**: `golangci-lint` is arguably the standard linter.
3.  **Dependencies**: Use Go Modules (`go.mod`, `go.sum`).

### Configuration

-   `.golangci.yml`: Standard configuration is provided by this package.

---

## General Principles

### 1. Simplicity and Clarity

Go favors simplicity. Avoid clever tricks, magic, or unnecessary abstraction layers. The code should be obvious.

> "Clear is better than clever."

### 2. Explicit is Better than Implicit

Go does not have exceptions (in the traditional sense), method overloading, or elaborate inheritance. This is a feature, not a bug.

-   Handle errors explicitly.
-   Pass context explicitly.

### 3. Composition over Inheritance

Go uses struct embedding for composition. Prefer small interfaces and composition to build complex behavior.

---

## Code Organization

### Package Layout

Follow the standardized project layout:

-   `/cmd`: Main applications (entry points).
-   `/pkg`: Library code that's ok to use by external applications.
-   `/internal`: Private application and library code. This is enforced by the Go compiler.
-   `/api`: OpenAPI/gRPC definitions.

### Imports

Group imports into three blocks separated by blank lines:

1.  Standard library
2.  Third-party packages
3.  Local/Internal packages

```go
import (
    "fmt"
    "os"

    "github.com/gin-gonic/gin"
    "github.com/rs/zerolog"

    "github.com/myorg/project/internal/user"
)
```

---

## Naming Conventions

### General

-   **MixedCaps** (CamelCase) for everything. No snake_case.
-   **Exported** identifiers (public) must start with an Uppercase letter.
-   **Unexported** identifiers (private) must start with a lowercase letter.

### Variables

-   **Short names** are preferred for scopes that are small (`i` for loop index, `r` for reader).
-   **Descriptive names** for larger scopes or global variables.
-   **Acronyms**: Keep them consistent case (`ServeHTTP`, `IDProcessor` - NOT `ServeHttp`, `IdProcessor`).

### Interfaces

-   One-method interfaces are named by the method name + `er` suffix (e.g., `Reader`, `Writer`).
-   Include method definitions that are concise.

```go
type UserStorer interface {
    Save(ctx context.Context, u *User) error
}
```

---

## Error Handling

### 1. Check Errors Immediately

Handle errors as soon as they occur. Avoid nesting success paths; use "guard clauses".

```go
// Good
f, err := os.Open("file.txt")
if err != nil {
    return err
}
// ... use f

// Bad
f, err := os.Open("file.txt")
if err == nil {
    // ... use f
} else {
    return err
}
```

### 2. Wrap Errors

When passing an error up the stack, wrap it with context if useful, using `%w` verb.

```go
if err := db.Query(...); err != nil {
    return fmt.Errorf("querying users failed: %w", err)
}
```

### 3. Custom Errors

Define custom error types or variables for errors the caller might want to check against (using `errors.Is` or `errors.As`).

```go
var ErrUserNotFound = errors.New("user not found")
```

---

## Concurrency

### 1. Share Memory by Communicating

Don't communicate by sharing memory. Use **channels** to pass data between goroutines.

### 2. Context

Always pass `context.Context` as the first argument to functions that involve I/O or long-running processes. This enables cancellation and timeouts.

```go
func FetchData(ctx context.Context, url string) error {
    req, _ := http.NewRequestWithContext(ctx, "GET", url, nil)
    // ...
}
```

### 3. Leak Prevention

Never start a goroutine without knowing how it will stop. Use `sync.WaitGroup` or proper channel closing mechanisms to ensure cleanup.

---

## Performance

### 1. Slices and Maps

Pre-allocate slices and maps if you know the size (or a reasonable estimate). This reduces allocation overhead.

```go
// Good
users := make([]User, 0, len(ids))

// Bad
var users []User
```

### 2. Pointers vs Values

-   Use **pointers** for large structs or when the function needs to modify the receiver/argument.
-   Use **values** for small structs, basic types, and maps/channels/functions (which are reference types already).

### 3. Benchmarking

Use Go's built-in benchmarking tools (`go test -bench=.`) to verify performance before optimizing.

```bash
go test -bench=. -benchmem
```
