from src.logger import get_logger
from src.exception import CustomException
import sys
logger=get_logger(__name__)

if __name__=="__main__":
    try:
        logger.info("Division taking place")
        c=1/0
    except Exception as e:
        logger.error("Exception raised")
        raise CustomException(e,sys)
