import logging
from logging.handlers import RotatingFileHandler
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

# --- Configure Logger ---
logger = logging.getLogger("chatbot_logger")
logger.setLevel(logging.DEBUG)  # Capture all levels

if not logger.hasHandlers():
    # File handler (with rotation)
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=5*1024*1024, backupCount=3)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    file_handler.setFormatter(formatter)
    #
    # Console handler
    # console_handler = logging.StreamHandler()
    # console_handler.setFormatter(formatter)
    #
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)