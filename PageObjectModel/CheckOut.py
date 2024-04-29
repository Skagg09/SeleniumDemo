from selenium.webdriver.common.by import By

from PageObjectModel.ConfirmPage import ConfirmPage


class CheckOut:

    itemsList=(By.XPATH, "//div[@class='card h-100']")
    chckbtn=(By.XPATH, "//div[@id='navbarResponsive']/ul/li")
    confbtn=(By.CSS_SELECTOR, ".btn-success")
    def __init__(self,driver):
        self.driver=driver

    def shopItems(self):
        return self.driver.find_elements(*CheckOut.itemsList)

    def checkOutButton(self):
        return self.driver.find_element(*CheckOut.chckbtn)


    def confButton(self):
         self.driver.find_element(*CheckOut.confbtn).click()
         confirmPage = ConfirmPage(self.driver)
         return confirmPage