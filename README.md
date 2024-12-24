# Python Project Structure Creator

This Python script automates the setup of a Python project directory with a predefined structure and necessary files.

---
## Features

- Creates a standard Python project directory structure.
- Generates a `main_script.py` with a template for the main project script.
- Includes a utility script for file operations.
- Creates a `requirements.txt` file with predefined dependencies.
- Easily customizable for additional folders, files, or functionality.

---

## Directory Structure

The script creates the following directory structure:
```
/<project-directory>/
├── config/              # Configuration files (e.g., JSON, YAML, INI files)
├── docs/                # Documentation files
├── input/               # Input data files (e.g., CSV, JSON, etc.)
├── libs/                # Shared library or modules (if not publishing to PyPI)
├── logs/                # Log files generated during runtime
├── scripts/
│   ├── tools/           # Standalone scripts or tools
│   ├── utils/           # Utility functions/modules
├── temp/                # Temporary files
├── tests/               # Unit tests, test scripts
├── third_party/         # Third-party tools, libraries, or scripts
├── main_script.py       # Entry point for the project
└── requirements.txt     # Dependencies for the project
```

## How to Use This Tool

### 1. Save the Script
Save the provided Python script as `setup_project.py`.

### 2. Run the Script
Run the script from the command line:
bash: python setup_project.py /path/to/your/project
- Replace `/path/to/your/project` with the desired path for your project directory.

## Customize the Project
Add more folders or files by editing the folders list and associated functions in the script
Extend utility scripts to include additional functionality as required.

## Benefits
- Reusable: Easily reuse this script for new project setups.
- Customizable: Adjust folder structures, templates, or requirements to match specific project needs.
- Time-Saving: Automates repetitive tasks, allowing you to focus on development
