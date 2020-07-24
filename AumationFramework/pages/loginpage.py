
from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPO(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger(logLevel=logging.DEBUG)

    #Locators
    _username_txt_bx = "username"
    _pwd_txt_bx = "//input[@placeholder='Password']"
    _keepmeloggedin_chk_bx = "keepLoggedInCheckBox"
    _login_btn = "//div[contains(text(),'Login')]"
    _errormsg = "//table[@id='ErrorsTable']//span"


    def enterusername(self,username):
        self.elementclear(locatorvalue=self._username_txt_bx,locatortype="id")
        self.entertext(username,locatorvalue=self._username_txt_bx,locatortype="id")
        self.log.info("Entered text "+username)

    def enterpassword(self,password):
        self.elementclear(locatorvalue=self._pwd_txt_bx,locatortype="xpath")
        self.entertext(password,locatorvalue=self._pwd_txt_bx,locatortype="xpath")
        self.log.info("Entered password "+password)

    def clickkeepmeloggedin(self):
        self.elementclick(locatorvalue=self._keepmeloggedin_chk_bx,locatortype="id")
        self.log.info("Clicked on keep me logged in check box")

    def clickloginbtn(self):
        self.elementclick(locatorvalue=self._login_btn,locatortype="xpath")
        self.log.info("Clicked on login button")

    def waitfordashboardpage(self):
        self.waitTime(15)
        self.explicitwaitfortitlecontains(self.driver, "actiTIME -  Enter Time-Track")
        assert "https://demo.actitime.com/user/submit_tt.do" == self.geturl(), "I am not on dashboard page"
        self.log.info("Successfully landed on the dashboard page")

    def validateinvalidloginerrormsg(self):
        self.waitTime(30)
        actualtext = self.getelementtext(locatorvalue=self._errormsg,locatortype="xpath")
        expectedtext = "Username or Password is invalid. Please try again."
        assert actualtext == expectedtext, "Error message is not displayed on the page"
        self.log.info("Error msg displayed properly "+actualtext)

    def validlogin(self,username,password):
        self.enterusername(username)
        self.enterpassword(password)
        self.clickkeepmeloggedin()
        self.clickloginbtn()
        self.waitfordashboardpage()
