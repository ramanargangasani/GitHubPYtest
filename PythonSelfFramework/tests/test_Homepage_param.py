import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver


class TestHomePage(BaseClass):
    def test_formSubmission(self, getdata):
        log = self.GetLogger()
        homepage = HomePage(self.driver)
        log.info("first name :" + getdata["firstname"])
        homepage.GetName().send_keys(getdata["firstname"])
        log.info("first name :" + getdata["lastname"])
        homepage.GetEmail().send_keys(getdata["lastname"])
        homepage.GetChekBox().click()
        # select package
        log.info("first name :" + getdata["gender"])
        self.SelectOptionByText(homepage.GetGender(), getdata["gender"])
        homepage.ClicksubmitButton().click()
        str1 = homepage.GetSucessText().text
        str2 = "Success! The Form has been submitted successfully!."
        assert "Success" in str1  # comparing substring of the success message
        self.driver.refresh()

    # @pytest.fixture(params=[("Ramana", "Gangasani", "Male"), ("RamaDevi", "Gangasani", "Female")])
    # @pytest.fixture(params=[{"firstname":"Ramana", "lastname":"Gangasani", "gender" : "Male"}, {"firstname":"RamaDevi", "lastname":"Gangasani", "gender" : "Female"}])
    
    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getdata(self, request):
        return request.param
