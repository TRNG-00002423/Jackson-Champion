"""
Configure logging for the QA Test Framework.

Requirements:
1. Console handler: Show INFO and above, concise format
2. File handler: Capture DEBUG and above, detailed format with timestamps
3. Use a RotatingFileHandler (max 1MB, keep 3 backups)
"""

import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_file="test_framework.log", console_level=logging.INFO):
    """Configure and return the root logger for the framework.

    Args:
        log_file: Path to the log file
        console_level: Minimum level for console output

    Returns:
        logging.Logger configured with both handlers
    """
    # TODO: Create logger named "qa_framework"
    # TODO: Add StreamHandler for console (INFO+)
    # TODO: Add RotatingFileHandler for file (DEBUG+)
    # TODO: Set appropriate formatters on each handler
    # TODO: Return the configured logger
    logger = logging.getLogger("qa_framework")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,
        backupCount=3
    )
    file_handler.setLevel(logging.DEBUG)

    console_format = logging.Formatter(
        "%(levelname)s | %(message)s"
    )

    file_format = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
    