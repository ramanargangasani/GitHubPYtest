
# self.driver.find_element_by_css_selector("a[href*='shop']").click()
from selenium.webdriver.common.by import By

# creating page object modal machinem i.e POM
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    check1 = (By.ID, "exampleCheck1")
    Gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successtext = (By.CLASS_NAME, "alert-success")

    def ClickShopLink(self):
        # return self.driver.find_element(*HomePage.shop)   # clicking Shop link on the page
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def GetName(self):
        return self.driver.find_element(*HomePage.name)

    def GetEmail(self):
        return self.driver.find_element(*HomePage.email)

    def GetChekBox(self):
        return self.driver.find_element(*HomePage.check1)

    def GetGender(self):
        return self.driver.find_element(*HomePage.Gender)

    def ClicksubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def GetSucessText(self):
        return self.driver.find_element(*HomePage.successtext)