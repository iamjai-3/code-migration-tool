import sys
from file_utils import read_file, write_file
from translator import CodeTranslator
from utils import extract_code_block


def main():
    """
    Main entry point for the code translation application.
    """
    if len(sys.argv) != 4:
        print("Usage: python main.py <source_file> <source_lang> <target_lang>")
        sys.exit(1)

    source_file = sys.argv[1]
    source_lang = sys.argv[2]
    target_lang = sys.argv[3]
    output_file = "dest/translated_code.js"

    # Read the source code
    source_code = read_file(source_file)

    # Initialize translator
    translator = CodeTranslator()

    print(f"Translating {source_lang} code to {target_lang}...")

    # Translate code
    translated_response = translator.translate_code(
        source_code=source_code, source_lang=source_lang, target_lang=target_lang
    )

    # Extract code block
    translated_code = extract_code_block(translated_response, target_lang)

    # Write translated code to file
    if translated_code:
        write_file(output_file, translated_code)
        print(f"Translation complete! Translated code written to {output_file}")
    else:
        print("No code block found in the translated response.")


if __name__ == "__main__":
    main()
