# SARA
import subprocess

def run_pylint_analysis(file_path):
    try:
        result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
        pylint_output = result.stdout

        # Check if there are any issues reported by Pylint
        if "Your code has been rated at" not in pylint_output:
            print(f'Pylint found issues: {pylint_output}')
        else:
            print(f'Pylint Output: {pylint_output}')

    except subprocess.CalledProcessError as e:
        print(f'Error running Pylint: {e.stderr}')

if _name_ == "_main_":
    # Replace 'your_file.py' with the actual path to your Python file
    file_path = 'path/to/your_file.py'
    
    run_pylint_analysis(file_path)
