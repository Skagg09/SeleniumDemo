from selenium.webdriver.common.by import By

from PageObjectModel.CheckOut import CheckOut


class HomePage:

    shop=(By.LINK_TEXT, "Shop")
    name=(By.NAME, "name")
    email=(By.NAME, "email")
    pwd=(By.ID, "exampleInputPassword1")
    chkBx=(By.XPATH, "//input[@type='checkbox']")
    smbt=(By.XPATH, "//input[@type='submit']")
    m = (By.CLASS_NAME, "alert-success")
    def __init__(self,driver):
        self.driver=driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOut = CheckOut(self.driver)
        return checkOut

    def sendName(self,text):
        return self.driver.find_element(*HomePage.name).send_keys(text)
    def sendEmail(self,text):
        return self.driver.find_element(*HomePage.email).send_keys(text)

    def sendPwd(self,text):
        return self.driver.find_element(*HomePage.pwd).send_keys(text)

    def clickCheckBox(self):
        return self.driver.find_element(*HomePage.chkBx)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.smbt)

    def verifyMessage(self):
        return self.driver.find_element(*HomePage.m)