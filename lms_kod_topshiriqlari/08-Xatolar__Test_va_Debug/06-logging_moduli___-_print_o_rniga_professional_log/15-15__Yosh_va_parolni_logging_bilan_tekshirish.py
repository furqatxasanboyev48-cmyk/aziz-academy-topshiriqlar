import logging
import sys
logging.basicConfig(level=logging.INFO,format="%(message)s",stream=sys.stdout)
age = int(input())
password = input()
if age < 18:
    logging.error("AGE")
elif len(password) < 6:
    logging.error("PASS")
else:
    logging.info("OK")