
from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class AdduserPO(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger(logLevel=logging.DEBUG)

    #Locators
    _firstname_txt_box = "(//input[@placeholder='First Name'])[3]"
    _lastname_txt_box = "(//input[@placeholder='Last Name'])[3]"
    _emailid_txt_box = "(//input[@placeholder='Email'])[3]"
    _save_and_send_invitation_link = "//div[text()='Save & Send Invitation']"
    _close_btn = "(//span[text()='Close'])[1]"

    def firstname(self, firstname):
        self.entertext(firstname, locatorvalue=self._firstname_txt_box, locatortype="xpath")
        self.log.info("First name entered")

    def lastname(self, lastname):
        self.entertext(lastname, locatorvalue=self._lastname_txt_box, locatortype="xpath")
        self.log.info("Last name entered")

    def emailid(self, emailid):
        self.entertext(emailid, locatorvalue=self._emailid_txt_box, locatortype="xpath")
        self.log.info("Email id entered")

    def saveandsendinvitation(self):
        self.elementclick(locatorvalue=self._save_and_send_invitation_link, locatortype="xpath")
        self.log.info("Clicked on save and send invitation link")

    def closebtn(self):
        self.elementclick(locatorvalue=self._close_btn, locatortype="xpath")
        self.log.info("Clicked on Close button")