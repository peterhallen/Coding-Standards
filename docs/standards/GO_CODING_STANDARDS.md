# Go Coding Standards

This document outlines the coding standards for Go projects.

## Tooling
- **Formatting**: `gofmt` (standard) or `goimports`
- **Linting**: `golangci-lint` (recommended) or `go vet`

## General Principles
1.  **Formatting**: Always use `gofmt`. Code must be formatted before commit.
2.  **Error Handling**: Handle errors explicitly. Do not ignore errors using `_` unless absolutely necessary and documented.
    ```go
    // Bad
    f, _ := os.Open("filename")

    // Good
    f, err := os.Open("filename")
    if err != nil {
        return err
    }
    ```
3.  **Naming**:
    - Use `CamelCase` for exported names, `camelCase` for unexported.
    - Keep variable names short but descriptive (`i` for loops, `req` for requests).
    - Package names should be lowercase, single word, and match the directory name.

## Code Organization
- Group imports: standard library first, then 3rd party, then local.
- Avoid circular dependencies.
- Keep functions short and focused.

## Testing
- Use the standard `testing` package.
- Test files must end in `_test.go`.
- Use table-driven tests for multiple cases.
