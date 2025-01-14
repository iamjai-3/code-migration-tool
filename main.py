import os
import sys
from file_utils import read_file, write_file, find_files_by_extension
from translator import CodeTranslator
from utils import extract_code_block

# Map target languages to file extensions
LANGUAGE_EXTENSION_MAP = {
    "javascript": ".js",
    "python": ".py",
    "java": ".java",
    "typescript": ".ts",
    "ruby": ".rb",
    # Add more mappings as needed
}


def translate_codebase(
    source_dir: str, source_lang: str, target_lang: str, output_dir: str
) -> None:
    """
    Translates all files in a codebase from one language to another.
    :param source_dir: Directory containing source code.
    :param source_lang: Source programming language.
    :param target_lang: Target programming language.
    :param output_dir: Directory to save the translated files.
    """
    translator = CodeTranslator()

    # Get the appropriate file extension for the target language
    target_extension = LANGUAGE_EXTENSION_MAP.get(target_lang.lower(), ".txt")

    # Find all source files
    extensions = (
        [".py"] if source_lang.lower() == "python" else []
    )  # Extend this as needed
    source_files = find_files_by_extension(source_dir, extensions)

    if not source_files:
        print("No files found to translate.")
        return

    print(f"Found {len(source_files)} file(s) to translate.")

    for source_file in source_files:
        # Read source code
        source_code = read_file(source_file)

        # Translate the code
        print(f"Translating file: {source_file}")
        translated_response = translator.translate_code(
            source_code=source_code,
            source_lang=source_lang,
            target_lang=target_lang,
        )

        # Extract the code block
        translated_code = extract_code_block(translated_response, target_lang)

        if translated_code:
            # Define the output path
            base_name = os.path.splitext(os.path.basename(source_file))[0]
            output_file = os.path.join(output_dir, base_name + target_extension)

            # Ensure the output directory exists
            os.makedirs(output_dir, exist_ok=True)

            # Write the translated code
            write_file(output_file, translated_code)
            print(f"Translated file written to: {output_file}")
        else:
            print(f"Skipping file: {source_file} (no valid translation found)")


def main():
    """
    Main entry point for the code translation application.
    """
    if len(sys.argv) != 5:
        print(
            "Usage: python main.py <source_dir> <source_lang> <target_lang> <output_dir>"
        )
        sys.exit(1)

    source_dir = sys.argv[1]
    source_lang = sys.argv[2]
    target_lang = sys.argv[3]
    output_dir = sys.argv[4]

    translate_codebase(source_dir, source_lang, target_lang, output_dir)


if __name__ == "__main__":
    main()
