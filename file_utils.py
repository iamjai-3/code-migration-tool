import os
from typing import List


def read_file(file_path: str) -> str:
    """
    Reads the contents of a file.
    :param file_path: Path to the file.
    :return: File contents as a string.
    """
    with open(file_path, "r") as file:
        return file.read()


def write_file(file_path: str, content: str) -> None:
    """
    Writes content to a file.
    :param file_path: Path to the file.
    :param content: Content to write.
    """
    with open(file_path, "w") as file:
        file.write(content)


def find_files_by_extension(directory: str, extensions: List[str]) -> List[str]:
    """
    Recursively finds files in a directory with the given extensions.
    :param directory: Directory to search.
    :param extensions: List of file extensions to include (e.g., ['.py', '.js']).
    :return: List of file paths.
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files
