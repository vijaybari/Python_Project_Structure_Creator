from pathlib import Path

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

    return specific_paths