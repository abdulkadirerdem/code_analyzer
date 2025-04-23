# Python Code Analysis Tool

This tool statically analyzes Python projects and visualizes code structure, dependencies, and function relationships.

## Features

- Automatically scan Python files
- Analyze code structure (functions, classes, variables)
- Detect dependencies between functions
- Perform fan-in and fan-out analysis for each function
- Identify entry point functions
- Extract documentation strings (docstrings)
- Output results in JSON or plain text format
- Support single-file or whole-project analysis

## Installation

1. Clone the repository:

```bash
git clone https://github.com/abdulkadirerdem/code_analyzer
cd code_analyzer
```

2. Install Dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Terminal Commands

You can use the following commands to analyze your project:

```bash
# Analyze default project directory in regular format
python main.py

# Analyze default project directory in JSON format
python main.py --json

# Analyze a specific project directory
python main.py --path my_project --json

# Analyze only a specific file
python main.py --file my_project/services.py --json
```

### Response Format

The output of the tool is as follows:

```json
{
  "user_service.py": {
    "file": "user_service.py",
    "functions": [
      {
        "name": "create_user",
        "code": "def create_user(data):\n    \"\"\"Creates a new user...\"\"\"\n    user = User(**data)\n    db.save(user)\n    return user.id",
        "docstring": "Creates a new user and saves it to the database.",
        "fan_in": 3,
        "fan_out": 2,
        "is_entry_point": false
      },
      {
        "name": "initialize_app",
        "code": "def initialize_app():\n    \"\"\"Initializes the application.\"\"\"\n    load_env()\n    start_server()\n    return True",
        "docstring": "Initializes the application.",
        "fan_in": 0,
        "fan_out": 1,
        "is_entry_point": true
      }
    ]
  }
}
```

### Response Description

- **file**: Name of the analyzed file
- **functions**: List of functions found in the file
- **name**: Function name
- **code**: Source code of the function
- **docstring**: Documentation string of the function
- **fan_in**: Number of other functions that call the function
- **fan_out**: Number of other functions that the function calls
- **is_entry_point**: Whether the function has an entry point (true if not called by any function)

## Test

To run the tests:

```bash
# Run all tests
pytest

# Run a specific test file
pytest -s tests/test_analyzer.py

# The -s flag allows print statements to be displayed during testing
```
