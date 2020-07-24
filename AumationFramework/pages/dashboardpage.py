
from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class DashboardPO(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger(logLevel=logging.DEBUG)

    #Locators
    _logout_lnk = "//a[text()='Logout']"
    _Users_tab = "//div[text()='Users']"
    _Newuser_btn = "//div[text()='New User']"

    def logout(self):
        self.elementclick(locatorvalue=self._logout_lnk,locatortype="xpath")

    def userstab(self):
        self.elementclick(locatorvalue=self._Users_tab,locatortype="xpath")
        self.log.info("Clicked on New users tab")

    def newuserbtn(self):
        self.elementclick(locatorvalue=self._Newuser_btn,locatortype="xpath")
        self.log.info("Clicked on New User button")
