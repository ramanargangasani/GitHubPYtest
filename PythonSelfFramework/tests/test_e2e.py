'''
# driver = self.driver
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup_initialization") # instead we are using Base class to call one time. i.e more optimize

class TestOne(BaseClass):
    def test_e2e(self):
        log = self.GetLogger()
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)  # calling page objects
        # driver.find_element_by_css_selector("a[href*='shop']").click()
        # homePage.ClickShopLink().click()
        checkoutpage = homePage.ClickShopLink()
        # checkoutpage = CheckoutPage(self.driver)
        log.info("Getting all the cart titles")
        products = checkoutpage.GetCardTitles()
        # products = driver.find_elements_byC:\Python\PythonSelfFramework_xpath("//div[@class='card h-100']")
        # //div[@class='card h-100']/div/h4/a
        for product in products:
            productname = product.find_element_by_xpath("div/h4/a").text
            log.info("product name:" + productname)
            if productname == "Blackberry":
                # checkoutpage.ClickAddButton().click()
                product.find_element_by_xpath("div/button").click()
        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkoutpage.ClickCheckOutButton().click()
        # the elements correct values for check out
        checkoutitems = self.driver.find_elements_by_xpath("//*[contains(@class,'table-hover')]/tbody/tr/td/div/div/h4/a")
        for item in checkoutitems:
            if item.text == "Blackberry":
                # print(" correct value checkout:" + item.text)
                log.info(" correct value checkout:" + item.text)
                confirmpage = checkoutpage.ClickSucessButton()
                # self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        log.info("Entering country name on the check box i.e ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        self.VerifyLinkPresenceWait("India")  # expilicit wait in base class
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        # self.driver.find_element_by_css_selector("div[class*='checkbox-primary']").click()
        # self.driver.find_element_by_css_selector("input[type='submit']").click()
        confirmpage = ConfirmPage(self.driver)  # calling Page objects
        confirmpage.CheckBoxClick().click()
        confirmpage.SubmitButtonClick().click()
        sucessText = self.driver.find_element_by_css_selector("div[class*='alert alert-success']").text
        assert "Thank you" in sucessText
        # print(sucessText)
        log.info(sucessText)
        self.driver.get_screenshot_as_file("screen.png")
