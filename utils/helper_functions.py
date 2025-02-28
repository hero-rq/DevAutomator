import os
import subprocess
import shlex
import logging

def run_command(command, logger=None):
    """
    Executes a shell command securely and returns its output, error message, and return code.

    :param command: The shell command to execute as a string.
    :param logger: Optional logger instance for logging command execution details.
    :return: Tuple of (stdout, stderr, returncode)
    """
    if logger:
        logger.info(f"Executing command: {command}")

    try:
        # Securely split the command into a list
        command_list = shlex.split(command)

        # Run the command safely without `shell=True` (prevents shell injection attacks)
        result = subprocess.run(command_list, capture_output=True, text=True)

        # Log command output
        if logger:
            logger.info(f"Command output:\n{result.stdout.strip()}")
            if result.stderr:
                logger.warning(f"Command error:\n{result.stderr.strip()}")

        return result.stdout.strip(), result.stderr.strip(), result.returncode

    except FileNotFoundError:
        error_message = "Command not found. Please check if the required tools are installed."
        if logger:
            logger.error(error_message)
        return None, error_message, 127  # 127 is the exit code for "command not found"

    except Exception as e:
        error_message = f"Failed to execute command: {e}"
        if logger:
            logger.error(error_message)
        return None, error_message, 1

def file_exists(filepath):
    """
    Checks if a given file exists.

    :param filepath: Path to the file.
    :return: True if the file exists, False otherwise.
    """
    exists = os.path.isfile(filepath)
    return exists

def directory_exists(dirpath):
    """
    Checks if a given directory exists.

    :param dirpath: Path to the directory.
    :return: True if the directory exists, False otherwise.
    """
    exists = os.path.isdir(dirpath)
    return exists

# Example Logger Setup (for standalone testing)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Test Command Execution
    output, error, code = run_command("ls -la", logger)
    print(f"Output:\n{output}\nError:\n{error}\nExit Code: {code}")

    # Test File Check
    print(f"File Exists: {file_exists('setup.py')}")

    # Test Directory Check
    print(f"Directory Exists: {directory_exists('utils')}")
