import pyperclip
import re

def read_clipboard():
    """Reads the content of the clipboard and returns it."""
    return pyperclip.paste()


def write_to_clipboard(text):
    """Writes the processed text to the clipboard."""
    try:
        pyperclip.copy(text)
        print("Processed text copied to clipboard.")
    except pyperclip.PyperclipException:
        print("Failed to write to clipboard. Please check your clipboard access permissions.")

def extract_numbers(text):
    match = re.search(r"[\d]*\d\.\d+", text)
    if match:
        number_str = match.group(0).replace("'", "")
        try:
            return float(number_str)
        except ValueError:
            return None
        
def get_multiplier(value):
    """
        (32000000.00, 0.50),
        (16000000.00, 0.55),
        (8000000.00, 0.60),
        (4000000.00, 0.65),
        (2000000.00, 0.70),
        (1.00, 0.75)
    """
    if value <= 1.00:
        return 1.75
    elif value <= 2000000.00:
        return 1.70
    elif value <= 4000000.00:
        return 1.65
    elif value <= 8000000.00:
        return 1.60
    elif value <= 16000000.00:
        return 1.55
    else:
        return 1.50
    
def process_text(text):
    """
    Todo
    """
    return text
    

def main():
    """
    Main function to read from clipboard, process the numbers and write back to clipboard
    """
    try:
        text = read_clipboard()
    except pyperclip.PyperclipException:
        print("Failed to read from clipboard. Please check your clipboard access permissions.")
        return
    
    if not text:
        print("Clipboard is empty.")
        return
    
    result = process_text(text)
    write_to_clipboard(result)

if __name__ == "__main__":
    main()