from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

        # self.driver.find_element_by_css_selector("div[class*='checkbox-primary']").click()
        # self.driver.find_element_by_css_selector("input[type='submit']").click()

    checkboxselect = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
    submitclick = (By.CSS_SELECTOR, "input[type='submit']")

    def CheckBoxClick(self):
        return self.driver.find_element(*ConfirmPage.checkboxselect)

    def SubmitButtonClick(self):
        return self.driver.find_element(*ConfirmPage.submitclick)