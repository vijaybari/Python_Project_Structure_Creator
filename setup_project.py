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

Author: Vijay Bari
"""

def main():
    """Entry point for the script."""
    print("Hello, World!")

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
    
    utils_path = os.path.join(base_path, "scripts", "utils", "file_utils.py")
    with open(utils_path, "w") as file:
        file.write(utils_script_content)

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


# Main function to initialize the project
def initialize_project(base_path):
    setup_project_structure(base_path)
    create_main_script(base_path)
    create_utils_scripts(base_path)
    create_requirements_file(base_path)
    create_readme_template(base_path)
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
