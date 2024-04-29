import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.ConfirmPage import ConfirmPage
from PageObjectModel.HomePage import HomePage
from PageObjectModel.CheckOut import CheckOut

from selenium.webdriver.chrome.service import Service

from BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        homePage=HomePage(self.driver)
        checkOut=homePage.shopItems()




        log.info("Selecting device")
        li = checkOut.shopItems()

        for l in li:
            x = l.find_element(By.XPATH, "div/h4/a").text
            if x == 'Blackberry':
                l.find_element(By.XPATH, "div/button").click()

        checkOut.checkOutButton().click()
        time.sleep(3)
        confirmPage=checkOut.confButton()
        time.sleep(3)
        log.info("Selecting country")
        confirmPage.entCountry().send_keys("Ind")
        time.sleep(3)
        self.verifyLink("India")
        confirmPage.seachCountry().click()
        confirmPage.selectCheckbox().click()
        confirmPage.clickPurchase().click()

        time.sleep(3)
        mess = confirmPage.validateMessage().text
        log.info("Text received: "+mess)
        assert "Success" in mess