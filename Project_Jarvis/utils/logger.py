import logging
import sys
import os

def get_logger(name: str = "Jarvis"):
    # Create logs inside utils folder
    log_dir = os.path.dirname(os.path.abspath(__file__))   # path of utils/
    log_file = os.path.join(log_dir, "jarvis.log")         # utils/jarvis.log

    logger = logging.getLogger(name)
    if not logger.handlers:  # avoid duplicate handlers
        logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        # File handler
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.INFO)  # file logs only INFO and above

        # Formatter (applies to both console + file)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
