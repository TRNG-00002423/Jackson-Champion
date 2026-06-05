import logging

print("print vs logging")
print("Application Started ......")
print("Some thing went wrong ....")
print("Lets log this .....")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname) -8s | %(message)s",
    datefmt="%H:%M:%S"
)

logging.debug("This is a DEBUG Message")
logging.info("This is TNFO Message")