from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # product.find_element_by_xpath("div/button").click()
    # driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    # driver.find_element_by_css_selector("button[class*='btn-success']").click()
    # driver.find_element_by_css_selector("button[class*='btn-success']").click()
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    ProductAddButton = (By.XPATH, "div/button")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    Button1 = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def GetCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def ClickAddButton(self):
        return self.product.find_element(*CheckoutPage.ProductAddButton)

    def ClickCheckOutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def ClickSucessButton(self):
        # return self.driver.find_element(*CheckoutPage.Button1)
        self.driver.find_element(*CheckoutPage.Button1).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
