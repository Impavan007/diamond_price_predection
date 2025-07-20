import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)
LOG_File=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_log.txt"
logs_path = os.path.join(os.getcwd(),"logs", LOG_File)
os.makedirs(logs_path, exist_ok=True)
log_file_path = os.path.join(logs_path, LOG_File)

logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.INFO,
)