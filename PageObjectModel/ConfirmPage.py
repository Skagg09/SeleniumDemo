from selenium.webdriver.common.by import By

class ConfirmPage:
    enterCountry=(By.ID, "country")
    country=(By.LINK_TEXT, "India")
    checkBox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase=(By.XPATH, "//input[@value='Purchase']")
    message=(By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self,driver):
        self.driver=driver

    def seachCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def clickPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def validateMessage(self):
        return self.driver.find_element(*ConfirmPage.message)

    def entCountry(self):
        return self.driver.find_element(*ConfirmPage.enterCountry)