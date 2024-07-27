from us_Visa.logger import logging
from us_Visa.exception import USvisaException
import sys
try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)

logging.info("Welcome to cutom log demo")