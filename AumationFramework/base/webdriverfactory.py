import os
import sys
from selenium import webdriver
import utilities.custom_logger as cl
import logging

class WebdriverFactory():
    def __init__(self,browser):
        self.browser = browser
        self.browserexec_dir = sys.path[1]+"\\driversexec"
        self.chrome_driver_location = "C:\\Users\\VINAY\\PycharmProjects\\AumationFramework\\driversexec\\chromedriver.exe"
        self.firefox_driver_location = "C:\\Users\\VINAY\\PycharmProjects\\AumationFramework\\driversexec\\geckodriver.exe"
        self.ie_driver_location = self.browserexec_dir+"\\IEDriverServer.exe"
        # To inform to OS where executable files are present
        os.environ["webdriver.chrome.driver"] = self.chrome_driver_location
        os.environ["webdriver.gecko.driver"] = self.firefox_driver_location
        os.environ["webdriver.ie.driver"] = self.ie_driver_location

    log = cl.customLogger(logLevel=logging.DEBUG)

    def getWebdriverInstance(self):
        baseurl = "https://demo.actitime.com/login.do"
        if self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=self.chrome_driver_location)
            self.log.info("Chrome browser launched successfully")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=self.firefox_driver_location)
            self.log.info("FF browser launched successfully")
        elif self.browser == "ie":
            driver = webdriver.Ie(executable_path=self.ie_driver_location)
            self.log.info("IE browser launched successfully")
        else:
            self.log.error("Please enter the proper browser name eg:"
                           "chrome,firefox,ie")
        driver.get(baseurl)
        driver.implicitly_wait(20)
        return driver

