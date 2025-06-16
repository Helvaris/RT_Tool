import pyperclip
import re
import time

def watch_clipboard(poll_interval=1.0):
    """
    Watches the clipboard for changes and processes the text if it changes.
    """
    last_text = None
    print("Watching clipboard for changes...Press Ctrl+C to exit.")

    try:
        while True:
            # Read the current clipboard content
            current_text = pyperclip.paste()

            # If the clipboard content has changed, process it
            if current_text != last_text and current_text.strip():
                # Update last_text and process the new clipboard content
                last_text = current_text
                result = process_text(current_text)
                if result.strip():
                    # Write the processed text back to the clipboard
                    write_to_clipboard(result)
            time.sleep(poll_interval)
    except KeyboardInterrupt:
        print("\nStopped watching clipboard.")

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
    elif value >= 32_000_000.00:
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
            processed.append(f"{result:.2f}")
        else:
            continue
        # If no number is found, keep the original line

    return "\n".join(processed)

def main():
    """
    Main function to read from clipboard, process the numbers and write back to clipboard
    and watch for changes.
    This function will run indefinitely until interrupted.
    """
    try:
        text = read_clipboard()
        if not text.strip():
            print("Clipboard is empty. Please copy some text to the clipboard.")
        else:
            result = process_text(text)
            write_to_clipboard(result)
    except pyperclip.PyperclipException:
        print("Failed to read from clipboard. Please check your clipboard access permissions.")

    # Start watching the clipboard for changes
    watch_clipboard(poll_interval=0.5) # Adjust the poll interval as needed

if __name__ == "__main__":
    main()