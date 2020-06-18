from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium import webdriver


class TestHomePage(BaseClass):
    def test_formSubmission(self):
        homepage = HomePage(self.driver)
        homepage.GetName().send_keys("Ramana")
        homepage.GetEmail().send_keys("Gangasani")
        homepage.GetChekBox().click()
        # select package
        self.SelectOptionByText(homepage.GetGender(), "Female")
        homepage.ClicksubmitButton().click()
        str1 = homepage.GetSucessText().text
        str2 = "Success! The Form has been submitted successfully!."
        assert "Success" in str1  # comparing substring of the success message
