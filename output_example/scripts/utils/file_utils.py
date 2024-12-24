"""
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
