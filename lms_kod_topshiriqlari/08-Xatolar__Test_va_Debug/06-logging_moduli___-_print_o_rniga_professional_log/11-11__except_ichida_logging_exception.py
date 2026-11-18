import logging
import sys
logging.basicConfig(level=logging.ERROR,format="%(message)s",stream=sys.stdout)
try:
    1/0
except ZeroDivisionError:
    logging.exception("ERR", exc_info=False)