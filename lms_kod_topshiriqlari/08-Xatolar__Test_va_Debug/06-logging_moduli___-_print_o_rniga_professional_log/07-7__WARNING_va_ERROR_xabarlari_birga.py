import logging
import sys
logging.basicConfig(level=logging.WARNING,format="%(message)s",stream=sys.stdout)
logging.warning("W")
logging.error("E")