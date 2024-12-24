"""
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
