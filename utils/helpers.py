import os
import logging
from datetime import datetime

# Setup logger
def setup_logger(name):
    os.makedirs("logs", exist_ok=True)
    log_path = f"logs/{name}.log"
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent multiple handlers
    if not logger.handlers:
        fh = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger

def take_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(path)
    return path
