import logging
import sys
logging.basicConfig(level=logging.INFO,format="%(message)s",stream=sys.stdout)
a = int(input())
b = int(input())
try:
    r = a // b 
except ZeroDivisionError:
    logging.error("DIV0")
else:
    logging.info(r)