# Contributing to vite-core

Thank you for your interest in contributing to vite-core! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please:
1. Check if the issue has already been reported in the [Issues](https://github.com/Project-VITA-AI/vita-core/issues) section

When creating a bug report, please include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version and operating system
- Any relevant error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
1. Check if the enhancement has already been suggested
2. Provide a clear description of the proposed enhancement
3. Explain why this enhancement would be useful
4. Provide examples of how it would be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Ensure all tests pass** and code is properly formatted
6. **Submit the pull request** with a clear description of changes

## Development

### Running Tests

```bash
pytest
```

To run with coverage:
```bash
pytest --cov=vita-core --cov-report=html
```

### Code Formatting

Format code with Black:
```bash
black vita-core tests examples
```

### Linting

Check code with Ruff:
```bash
ruff check vita-core tests
```

Auto-fix issues:
```bash
ruff check --fix vita-core tests
```

### Type Checking

Run mypy:
```bash
mypy vita-core
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use Black for formatting (line length: 100)
- Use type hints for all function signatures
- Write docstrings for all public classes and methods

### Code Structure

- Keep functions focused and single-purpose
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions reasonably short

### Documentation

- Use Google-style docstrings
- Include type information in docstrings
- Document all public APIs
- Update README.md for user-facing changes

### Testing

- Write tests for all new features
- Aim for >80% code coverage
- Use descriptive test names
- Test both success and error cases

## Commit Messages

Write clear, descriptive commit messages:
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when applicable

Example:
```
Refactored operation loading

Update reload logic of operations during runtime.
Includes tests and documentation updates.

Fixes #123
```

## Questions?

If you have questions about contributing, please:
- Open an issue with the "question" label
- Check existing issues and discussions

Thank you for contributing to vita-core!

