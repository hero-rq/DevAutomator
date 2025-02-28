import logging
import sys

def setup_logger(name, level=logging.INFO):
    """
    Sets up and returns a logger with the specified name and logging level.
    
    :param name: The name of the logger.
    :param level: The logging level (default is logging.INFO).
    :return: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding multiple handlers if the logger already has one.
    if not logger.handlers:
        # Create a stream handler to output logs to stdout.
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        
        # Define a logging format.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Add the handler to the logger.
        logger.addHandler(handler)
        
    return logger
