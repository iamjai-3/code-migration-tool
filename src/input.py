def format_code(code):
    """Format the translated code for readability."""
    print("Formatting code...")
    return code.strip()


def save_output(self, code, output_file):
    """Save the translated code to a file."""
    with open(output_file, "w") as f:
        f.write(code)
    print(f"Translated code saved to {output_file}")
