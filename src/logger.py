"""
logger.py
----------
Configure the application's logging system.

Author : Scott
Project : CodeAlpha Basic Network Sniffer
"""

import logging
from pathlib import Path


def get_logger(name: str = "NetworkSniffer") -> logging.Logger:
    """
    Configure and return a logger instance.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Configured logger object.
    """

    # Create logs directory if it does not exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "capture.log"

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
