import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger(name, console_level=logging.INFO, file_level=logging.DEBUG, log_file='app.log'):
    """
    Sets up and returns a logger with specified name, console logging level, and file logging level.

    :param name: The name of the logger.
    :param console_level: Logging level for console output (default is logging.INFO).
    :param file_level: Logging level for file output (default is logging.DEBUG).
    :param log_file: The log file path (default is 'app.log').
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Capture all levels; handlers will filter levels appropriately.

    # Check if handlers are already added to avoid duplication.
    if not logger.handlers:
        # Console handler for stdout.
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(console_level)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # File handler with rotation.
        file_handler = RotatingFileHandler(log_file, maxBytes=1e6, backupCount=3)
        file_handler.setLevel(file_level)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger

# Example usage
if __name__ == "__main__":
    log = setup_logger(__name__)
    log.debug("Debug message")
    log.info("Info message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")
