"""
project_name/
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
├── requirements.txt     # Dependencies for the project
└── README.md            # Project description and setup instructions
"""

import os

# Function to create a directory if it doesn't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to create the main project structure
def setup_project_structure(base_path):
    folders = [
        "config",
        "docs",
        "input",
        "libs",
        "logs",
        "scripts/tools",
        "scripts/utils",
        "temp",
        "tests",
        "third_party",
    ]

    for folder in folders:
        create_directory(os.path.join(base_path, folder))

# Function to create the main script template
def create_main_script(base_path):
    main_script_path = os.path.join(base_path, "main_script.py")
    main_script_content = '''"""
Main script for the project.

Author:
-------
- Owner: Vijay Bari

Version:
--------
- 1.0.0 (2000-00-00)

Change Log:
-----------
- Version 1.0.0 (2000-00-00): Initial implementation by Vijay Bari.

Description:
------------
This script ...

1. ...
2. ...

Usage:
------
1. ...

Notes:
------
- ...
- ...
"""

import os
from colorama import Fore, Style, init
init() # Initialize colorama for cross-platform color support

from scripts.utils.paths_utils import get_generic_paths, get_specific_paths


def main():
    while True:
        # Pass the current working directory as the root folder & Construct paths using the current directory
        current_directory = os.getcwd()
        generic_paths = get_generic_paths(current_directory)

        # generic path constants
        LOG_FOLDER = generic_paths["LOGS"]
        INPUT_FOLDER = generic_paths["INPUT"]
        TOOLS_FOLDER = generic_paths["TOOLS"]

if __name__ == "__main__":
    main()
'''
    with open(main_script_path, "w") as file:
        file.write(main_script_content)

# Function to create basic utility scripts
def create_utils_scripts(base_path):
    utils_script_content = '''"""
Utility functions for file operations.

Author: Vijay Bari
"""

import shutil


def copy_content(source, destination):
    """Copy content from source to destination."""
    try:
        shutil.copy(source, destination)
        print(f"Successfully copied {source} to {destination}")
    except Exception as e:
        print(f"Failed to copy: {e}")
'''
    utils_path_content = '''from pathlib import Path

def get_generic_paths(root_folder):
    """
    Returns a dictionary of generic paths relative to the provided root folder.
    """
    root_folder = Path(root_folder).resolve()

    # Define generic paths
    generic_paths = {
        "ROOT": str(root_folder),
        "CONFIG": str(root_folder / "config"),
        "DOCS": str(root_folder / "docs"),
        "INPUT": str(root_folder / "input"),
        "LIBS": str(root_folder / "libs"),
        "LOGS": str(root_folder / "logs"),
        "SCRIPTS": str(root_folder / "scripts"),
        "TOOLS": str(root_folder / "scripts" / "tools"),
        "UTILS": str(root_folder / "scripts" / "utils"),
        "TEMP": str(root_folder / "temp"),
        "TESTS": str(root_folder / "tests"),
        "THIRD_PARTY": str(root_folder / "third_party"),
    }

    return generic_paths


def get_specific_paths(generic_paths):
    """
    Returns a dictionary of specific paths constructed using generic paths.
    """
    specific_paths = {
        # Specific paths
        "BM_BL_MERGER_TOOL": str(Path(generic_paths["THIRD_PARTY"]) / "50_Release" / "Generate_binFiles_for_DGUI_R8.bat"),
        "TEMP_LOCAL": str(Path(generic_paths["TEMP"]) / "local"),
        "TEMP_SVN": str(Path(generic_paths["TEMP"]) / "svn"),
        "DELETE_SVN_FOLDERS_SCRIPT": str(Path(generic_paths["TOOLS"]) / "delete_svn_folders.bat"),
        "LOG_FOLDER": generic_paths["LOGS"],  # Alias for generic path
    }

    return specific_paths'''
    
    utils_path = os.path.join(base_path, "scripts", "utils", "file_utils.py")
    utils_path_1 = os.path.join(base_path,"scripts", "utils", "paths_utils.py")
    with open(utils_path, "w") as file:
        file.write(utils_script_content)
    with open(utils_path_1, "w") as file:
        file.write(utils_path_content)

# Function to create a requirements.txt file
def create_requirements_file(base_path):
    requirements_path = os.path.join(base_path, "requirements.txt")
    requirements_content = """colorama==0.4.6"""
    with open(requirements_path, "w") as file:
        file.write(requirements_content)

import os

def create_readme_template(path):
    """
    Creates a README.md template file at the specified path.

    Parameters:
        path (str): The directory where the README.md file should be created.

    Returns:
        str: Full path of the created README.md file or an error message if the operation fails.
    """
    try:
        # Ensure the provided path exists, if not, create it
        if not os.path.exists(path):
            os.makedirs(path)

        # Define the full file path
        readme_file_path = os.path.join(path, 'README.md')

        # Define the template content
        readme_content = """# Project Title

A brief description of what this project does and who it's for

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
# Install dependencies
$ your-installation-command
```

## Usage

```bash
# Run the application
$ your-usage-command
```

## Contributing

Contributions are always welcome!

See `CONTRIBUTING.md` for ways to get started.

## License

[MIT](https://choosealicense.com/licenses/mit/)
"""

        # Write the template content to the README.md file
        with open(readme_file_path, 'w') as readme_file:
            readme_file.write(readme_content)

        return f"README.md created successfully at: {readme_file_path}"

    except Exception as e:
        return f"An error occurred while creating the README.md file: {e}"

# add .gitkeep files in empty directories
def add_gitkeep_files(base_path):
    """
    Generates .gitkeep files in the specified directory structure.

    Args:
        base_path (str): The base path where the folders exist.
    """
    folder_structure = {
        "config": "config",
        "docs": "docs",
        "input": "input",
        "libs": "libs",
        "logs": "logs",
        "scripts/tools": "scripts/tools",
        "temp": "temp",
        "tests": "tests",
        "third_party": "third_party"
    }

    import os

    for folder in folder_structure.values():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        gitkeep_path = os.path.join(folder_path, ".gitkeep")
        with open(gitkeep_path, "w") as gitkeep_file:
            gitkeep_file.write("")

    print(".gitkeep files have been generated in the specified folders.")


# Main function to initialize the project
def initialize_project(base_path):
    setup_project_structure(base_path)
    create_main_script(base_path)
    create_utils_scripts(base_path)
    create_requirements_file(base_path)
    create_readme_template(base_path)
    add_gitkeep_files(base_path)
    print(f"Python project structure created at: {base_path}")


# How to use this as a tool
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Setup Python project directory structure.")
    parser.add_argument("path", type=str, help="Base path for the project directory")

    args = parser.parse_args()

    initialize_project(args.path)

if __name__ == "__main__":
    main()
