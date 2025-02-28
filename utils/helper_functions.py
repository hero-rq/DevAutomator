import os
import subprocess

def run_command(command, logger=None):
    """
    Executes a shell command and returns its output, error message, and return code.
    
    :param command: The shell command to execute.
    :param logger: Optional logger instance for logging command execution details.
    :return: Tuple of (stdout, stderr, returncode)
    """
    if logger:
        logger.info(f"Running command: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if logger:
            logger.info(f"Command output: {result.stdout}")
            if result.stderr:
                logger.warning(f"Command error: {result.stderr}")
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        if logger:
            logger.error(f"Failed to run command: {e}")
        return None, str(e), 1

def file_exists(filepath):
    """
    Checks if a given file exists.
    
    :param filepath: Path to the file.
    :return: True if the file exists, False otherwise.
    """
    return os.path.isfile(filepath)
