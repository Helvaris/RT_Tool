import pyperclip

def read_clipboard():
    """Reads the content of the clipboard."""
    return pyperclip.paste()

def write_clipboard(text):
    """Writes text to the clipboard."""
    pyperclip.copy(text)

def process_text(text):
    """Processes the text from the clipboard."""
    lines = text.strip().splitlines()
    # Prefix each line with a checkmark for processed output
    processed = [f"[✔] {line}" for line in lines]
    return "\n".join(processed)