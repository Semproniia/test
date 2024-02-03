import subprocess
import string

def removenonprintablecharacters(inputstr):
    # Keep only printable ASCII characters
    printable_chars = set(string.printable)
    return ''.join(char for char in input_str if char in printable_chars)

def run_pylint_analysis(file_path):
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Sanitize the content by removing non-printable characters
        sanitized_content = remove_non_printable_characters(file_content)

        # Run Pylint on the sanitized content
        result = subprocess.run(['pylint', '--disable=all', '--enable=errors', '-'], input=sanitized_content, capture_output=True, text=True)

        # Print the Pylint output
        print(result.stdout)

    except Exception as e:
        print(f"Error running Pylint: {e}")

if __name == "__main":
    # Replace 'path/to/your_file.py' with the actual path to your Python file
    file_path = 'path/to/your_file.py'

    run_pylint_analysis(file_path)
