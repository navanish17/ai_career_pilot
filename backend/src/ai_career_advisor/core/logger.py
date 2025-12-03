import os
import sys 
from loguru import logger

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok = True)

#filepath
log_file_path = os.path.join(log_dir, 'app.log')

logger.add(
    sys.stdout,
    level = "INFO",
    format = "<green>{time: YYYY-MM-DD HH:mm:ss}</green> | "
            "<level> {level} </level> | "
            "{module} |"
            "{message} |"
            
)

#add rotating file handler

logger.add(
    log_file_path,
    rotation = '10MB',
    retention = '15 days',
    compression = 'zip',
    level = 'INFO',
    format = '{time: YYYY-MM-DD HH:mm:ss} | {level} | {module} | {message}'

)


logger = logger

