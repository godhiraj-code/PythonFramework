import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def inputData(self, webelement ,inputData):
        webelement.send_keys(inputData)

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger


