import subprocess
import sys
from pathlib import Path

def run_command(command):
    """Run a command in a subprocess and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout, result.returncode
    except subprocess.CalledProcessError as e:
        return f"Error running {command[0]}: {e.stderr}\n{e.stdout}", e.returncode

def run_pylint(file_path):
    """Run pylint on the given file."""
    return run_command(['pylint', file_path])

def run_bandit(file_path):
    """Run bandit on the given file."""
    return run_command(['bandit', '-r', file_path])

def run_radon_cc(file_path):
    """Run radon cc on the given file."""
    return run_command(['radon', 'cc', file_path])

def run_radon_mi(file_path):
    """Run radon mi on the given file."""
    return run_command(['radon', 'mi', file_path])

def automated_code_review(file_path):
    """Run automated code review tools on the given file."""
    print(f"Running code review on: {file_path}")

    print("\nRunning Pylint for PEP 8 compliance and general code quality...")
    pylint_output, pylint_code = run_pylint(file_path)
    print(pylint_output)
    if pylint_code != 0:
        print("Pylint detected issues or encountered an error.")

    print("\nRunning Bandit for security checks...")
    bandit_output, bandit_code = run_bandit(file_path)
    print(bandit_output)
    if bandit_code != 0:
        print("Bandit detected issues or encountered an error.")

    print("\nRunning Radon for code complexity...")
    radon_cc_output, radon_cc_code = run_radon_cc(file_path)
    print(radon_cc_output)
    if radon_cc_code != 0:
        print("Radon cc detected issues or encountered an error.")

    print("\nRunning Radon for maintainability index...")
    radon_mi_output, radon_mi_code = run_radon_mi(file_path)
    print(radon_mi_output)
    if radon_mi_code != 0:
        print("Radon mi detected issues or encountered an error.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_to_review>")
        sys.exit(1)

    file_to_review = sys.argv[1]
    file_path = Path(file_to_review)

    if not file_path.exists():
        print(f"Error: File path {file_path} does not exist.")
        sys.exit(1)

    automated_code_review(str(file_path))
