import logging
import sys
logging.basicConfig(stream=sys.stdout,level=logging.INFO,format="%(levelname)s:%(message)s")
n = int(input())
if n >= 0:
    logging.info("musbat")
else:
    logging.error("manfiy")