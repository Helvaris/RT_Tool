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

def extract_number(text):
    match = re.search(r"[\d']*\d\.\d+", text)
    if match:
        number_str = match.group(0).replace("'", "")
        try:
            return float(number_str)
        except ValueError:
            return None
        
def get_multiplier(value):
    """
    Returns a multiplier based on the value.
    The multiplier is determined by the following ranges:
    """
    if 1.00 <= value < 2_000_000.00:
        return 1.75
    elif 2_000_000.00 <= value < 4_000_000.00:
        return 1.70
    elif 4_000_000.00 <= value < 8_000_000.00:
        return 1.65
    elif 8_000_000.00 <= value < 16_000_000.00:
        return 1.60
    elif 16_000_000.00 <= value < 32_000_000.00:
        return 1.55
    elif value >=32_000_000.00:
        return 1.50
    else:
        return 1.75  # Default multiplier for values less than 1.00
    
def process_text(text):
    """
    Processes the input text to extract numbers, calculate the multiplier, and format the output.
    """
    # Extract the number from the text
    lines = text.strip().splitlines()
    processed = []

    for line in lines:
        value = extract_number(line)
        # If a number is found, calculate the multiplier and format the output
        if value is not None:
            multiplier = get_multiplier(value)
            result = round(value * multiplier, 2)
            processed.append(f"{line} => {result}")
        else:
            processed.append(f"{line} => No valid number found")

    return "\n".join(processed)

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