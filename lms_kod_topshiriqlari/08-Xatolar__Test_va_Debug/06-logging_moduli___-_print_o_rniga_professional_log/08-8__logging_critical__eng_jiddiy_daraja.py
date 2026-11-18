import logging
import sys
logging.basicConfig(level=logging.CRITICAL,format="%(message)s",stream=sys.stdout)
logging.critical("CRIT")