import re


def extract_code_block(text: str, targetLang: str) -> str:
    """
    Extracts the first code block from a string delimited by triple backticks (```).
    :param text: Input text containing code block(s).
    :return: Extracted code block, or an empty string if no block is found.
    """
    match = re.search(rf"```{targetLang}(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else ""
