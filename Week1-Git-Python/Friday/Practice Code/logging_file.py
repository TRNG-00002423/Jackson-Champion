import logging
import logging.handlers
import os

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(asctime)s | %(levelname) -8s | %(message)s",))

#File Handler
log_file = "my_logs.log"
file_handler = logging.FileHandler(log_file,mode="w")
file_handler.setFormatter(logging.Formatter(
    format = "%(asctime)s | %(levelname) -8s | %(message)s",
    datefmt= "%H:%M:%S"))

logger.addHandler(console)
logger.addHandler(file_handler)

logging.debug("This is a DEBUG Message")
logging.info("This is TNFO Message")
