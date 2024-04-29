import pytest

from BaseClass import BaseClass
from PageObjectModel.HomePage import HomePage
import time

from TestData.HomepageData import HomepageData


class TestForm(BaseClass):

    def test_form(self, getData):
        log = self.getlogger()
        log.info("Reached Homepage")
        homapage = HomePage(self.driver)
        homapage.sendName(getData["firstnane"])
        log.info("Entered Firstname: " + getData["firstnane"])
        time.sleep(2)
        homapage.sendEmail(getData["email"])
        log.info("Entered Email: " + getData["email"])
        homapage.sendPwd("KabriaEncores")
        log.info("Entered Password")

        homapage.clickCheckBox().click()
        log.info("Checkbox clicked")
        time.sleep(2)
        self.selectOptionById("exampleFormControlSelect1", 1)
        log.info("Selecting Option")
        homapage.clickSubmit().click()
        log.info("Clicking Submit")
        m = homapage.verifyMessage().text
        log.info("Text Message: " + m)
        print(m)
        time.sleep(2)
        assert "Success" in m
        self.driver.refresh()

    @pytest.fixture(scope='module', params=HomepageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
