import logging
import sys
logging.basicConfig(level=logging.INFO,format="%(message)s",stream=sys.stdout)
n = int(input())
if n < 0:
    logging.error("NEG")
else:
    logging.info("POS")