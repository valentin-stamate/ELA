import logging
from logging.handlers import RotatingFileHandler

import colorlog

# Create a logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# Create a handler with colorlog for console output
console_handler = colorlog.StreamHandler()
console_handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s [%(levelname)s] - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
    reset=True,
    style='%'
))
LOGGER.addHandler(console_handler)

# Create a rotating file handler for file output
file_handler = RotatingFileHandler('example.log', maxBytes=1024 * 1024, backupCount=3)
file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s'))
LOGGER.addHandler(file_handler)

# # Example usage
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")
