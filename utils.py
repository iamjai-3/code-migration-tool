import re
import sys


def extract_code_block(text: str, targetLang: str) -> str:
    """
    Extracts the first code block from a string delimited by triple backticks (```).
    :param text: Input text containing code block(s).
    :return: Extracted code block, or an empty string if no block is found.
    """
    match = re.search(rf"```{targetLang}(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else ""


def display_progress(current: int, total: int, prefix: str = "Progress") -> None:
    """
    Display the progress percentage in the CLI.
    :param current: The current chunk being processed.
    :param total: The total number of chunks.
    :param prefix: A prefix to display before the progress percentage.
    """
    progress = (current / total) * 100
    sys.stdout.write(f"\r{prefix}: {progress:.2f}%")
    sys.stdout.flush()
