# Examples

This directory contains code examples demonstrating the coding standards defined in `CODING_STANDARDS.md`.

## Files

### `good_example.py`
Demonstrates code that follows all coding standards:
- ✅ Proper documentation (docstrings for all public functions/classes)
- ✅ Type hints for all function parameters and returns
- ✅ Error handling with specific exceptions
- ✅ Proper code organization (imports, constants, classes, functions)
- ✅ Appropriate function length and complexity
- ✅ Meaningful variable and function names
- ✅ Early returns to reduce nesting
- ✅ Proper use of constants

### `bad_example.py`
⚠️ **WARNING**: Contains intentionally bad code for educational purposes.

Demonstrates common violations:
- ❌ Missing documentation
- ❌ No type hints
- ❌ Poor error handling (bare except, suppressing errors)
- ❌ Too many function parameters
- ❌ High cyclomatic complexity
- ❌ Deep nesting
- ❌ Unclear variable names
- ❌ Obvious comments
- ❌ Wrong data structures for use case

### `test_example.py`
Demonstrates proper testing practices:
- ✅ Arrange-Act-Assert pattern
- ✅ Descriptive test names
- ✅ Test organization with classes
- ✅ Testing edge cases and error conditions
- ✅ Proper use of mocks and patches
- ✅ Type hints in test functions

## Running the Examples

### Run the good example:
```bash
python examples/good_example.py
```

### Run the tests:
```bash
pytest examples/test_example.py -v
```

### Lint the examples:
```bash
flake8 examples/
pylint examples/
```

### Type check the examples:
```bash
mypy examples/
```

## Learning from Examples

1. **Compare good vs bad**: Read both `good_example.py` and `bad_example.py` side-by-side to understand the differences
2. **Run the linters**: See how the bad example fails linting checks
3. **Study the tests**: Understand how to write comprehensive tests
4. **Apply to your code**: Use the good example as a template for your own code

