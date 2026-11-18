import logging
import sys
logging.basicConfig(level=logging.ERROR, format="%(message)s",stream=sys.stdout)
logging.error("ERR")