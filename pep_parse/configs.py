import logging
from logging.handlers import RotatingFileHandler

from pep_parse.constants import DT_FORMAT, LOG_DIR, LOG_FILE, LOG_FORMAT


def configure_logging():
    LOG_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=10 ** 6,
        backupCount=5,
        encoding='utf-8'
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(
            rotating_handler,
            logging.StreamHandler()
        )
    )
