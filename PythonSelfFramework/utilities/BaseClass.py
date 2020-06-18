import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_initialization")
class BaseClass:

    def GetLogger(self):
        LoggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__) #  print the test case name i.e Base Class
        logger = logging.getLogger(LoggerName)  # print the actual child class name i.e test_editprofile
        fileHandler = logging.FileHandler('logfile1.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object i.e filehandler nothing file location

        logger.setLevel(logging.INFO)
        return logger

    def VerifyLinkPresenceWait(self, text):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOptionByText(self, locator, text):
        drop_down = Select(locator)
        drop_down.select_by_visible_text(text)


