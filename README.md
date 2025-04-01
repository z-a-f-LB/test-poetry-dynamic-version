# Hello World Package

A simple Python package that demonstrates cloud build capabilities and git hooks integration.

## Features

- Simple "Hello World" functionality
- Pre-commit hooks for code formatting
- Cloud build ready
- Type hints and documentation

## Installation

This package can be installed using Poetry:

```bash
poetry install
```

## Usage

```python
from hello_world import say_hello

# Basic usage
print(say_hello())  # Output: Hello, World!

# With custom name
print(say_hello("Alice"))  # Output: Hello, Alice!
```

## Development Setup

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository and install dependencies:
   ```bash
   git clone <repository-url>
   cd hello-world-package
   poetry install
   ```

3. Set up pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

## Development Tools

- `black`: Code formatting
- `isort`: Import sorting
- `pytest`: Testing framework
- `pre-commit`: Git hooks management
