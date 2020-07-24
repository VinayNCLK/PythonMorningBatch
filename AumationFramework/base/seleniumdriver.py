
import logging
import utilities.custom_logger as cl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import sys

class SeleniumDriver():
    def __init__(self,driver):
        self.driver = driver

    log = cl.customLogger(logLevel=logging.DEBUG)

    def getbytype(self,locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "class":
            return By.CLASS_NAME
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "linktext":
            return By.LINK_TEXT
        elif locatortype == "partialinktext":
            return By.PARTIAL_LINK_TEXT
        elif locatortype == "xpath":
            return By.XPATH
        else:
            self.log.error("Locator type "+locatortype+" not correct. Please pass proper locator type")
            return False

    #Get the webelement
    def getElement(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        element = None
        try:
            bytype = self.getbytype(locatortype)
            element = self.driver.find_element(bytype, locatorvalue)
            self.log.info("Element found with locator :"+locatortype+" and locator value "+locatorvalue)
            return element
        except Exception as e:
            self.log.error("Element not found with locator :" + locatortype + " and locator value " + locatorvalue+" "+e)
            return False

    #Enter the url
    def enterUrl(self,url):
        self.driver.get(url)
        self.log.info("Entered url on browser - "+url)

    # Close the window opened
    def closewindow(self):
        self.driver.close()

    #Waiting perticular amount of time
    def waitTime(self,sec):
        time.sleep(sec)

    #minimizing window
    def minimizebrowserwindow(self):
        self.driver.minimize_window()

    def setwindowsize(self,height,width):
        self.driver.set_window_size(height,width)

    def setwindowposition(self,height,width):
        self.driver.set_window_position(height,width)

    def geturl(self):
        url = self.driver.current_url
        self.log.info("Obtained url "+url)
        return url

    def getTitle(self):
        title = self.driver.title
        self.log.info("Obtained title "+title)
        return title

    def getPagesource(self):
        page_source = self.driver.page_source
        self.log.info("Obtained page source "+page_source)
        return page_source

    def nativebrowserback(self):
        self.driver.back()
        self.log.info("Clicked on back button")

    def nativebrowserforward(self):
        self.driver.forward()
        self.log.info("Clicked on forward button")

    def nativebrowserrefresh(self):
        self.driver.refresh()
        self.log.info("Clicked on refresh button")

    def elementclick(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            element.click()
            self.log.info("Clicked on element with locator type "+locatortype +" and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to click on element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def entertext(self,data,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            element.send_keys(data)
            self.log.info("Entered text on element with locator type "+locatortype +"and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to enter text on element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def elementclear(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            element.clear()
            self.log.info("Cleared on element with locator type "+locatortype +" and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to clear on element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def getelementtext(self, locatorvalue, locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue, locatortype)
            text = element.text
            self.log.info("Obtained text from element with locator type " + locatortype + " and locator value " + locatorvalue)
            return text
        except Exception as e:
            self.log.error("Unable to obtain text from element with locator type " + locatortype + " and locator value " +
                           locatorvalue + str(e))
            return False

        # Get the webelement

    def getElements(self, locatorvalue, locatortype="id/name/xpath/css/linktext/partiallinktext"):
        elements = []
        try:
            bytype = self.getbytype(locatortype)
            elements = self.driver.find_elements(bytype, locatorvalue)
            self.log.info("Elements found with locator :" + locatortype + " and locator value " + locatorvalue)
            return elements
        except Exception as e:
            self.log.error(
                "Elements not found with locator :" + locatortype + " and locator value " + locatorvalue + " " + e)
            return False

    def selectoptionfromdrpdwn(self,option,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            s1 = Select(element)
            s1.select_by_visible_text(option)
            self.log.info("selected option - "+option+"from element with locator type "+locatortype +" and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to select option from element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def deselectoptionfromdrpdwn(self,option,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            s1 = Select(element)
            s1.deselect_by_visible_text(option)
            self.log.info("Deselected option - "+option+"from element with locator type "+locatortype +" and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to deselect option from element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def deselectalloptionsfromdrpdwn(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            s1 = Select(element)
            s1.deselect_all()
            self.log.info("deselected all options from element with locator type "+locatortype +" and locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to deselect all options from element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def getfirst_selected_option(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        firstselectedoption = ""
        try:
            element = self.getElement(locatorvalue,locatortype)
            s1 = Select(element)
            firstselectedoption = s1.first_selected_option.text
            self.log.info("Obtained first selected option "+firstselectedoption+" from element with locator type "+locatortype +" and locator value "+locatorvalue)
            return firstselectedoption
        except Exception as e:
            self.log.error("Unable to obtain first selected option from element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def getall_selected_option(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        allselectedoption = []
        try:
            element = self.getElement(locatorvalue,locatortype)
            s1 = Select(element)
            allselectedoption = s1.all_selected_options
            self.log.info("Obtained all selected option "+allselectedoption+" from element with locator type "+locatortype +" and locator value "+locatorvalue)
            return allselectedoption
        except Exception as e:
            self.log.error("Unable to obtain all selected option from element with locator type "+locatortype+" and locator value "+
                           locatorvalue +str(e))
            return False

    def switchintoframe_webelement(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue, locatortype)
            self.driver.switch_to.frame(element)
            self.log.info(
                "Switched into the frame from element with locator type " + locatortype + " and locator value " + locatorvalue)
        except Exception as e:
            self.log.error(
                "Unable to switch to the from element with locator type " + locatortype + " and locator value " +
                locatorvalue + str(e))
            return False

    def switchintoframe_index_name(self,index=0,id=None):
        try:
            if id is not None:
                self.driver.switch_to.frame(id)
                self.log.info(
                    "Switched into the frame from id "+id)
            else:
                self.driver.switch_to.frame(index)
                self.log.info("Switched into the frame from index "+index)
        except Exception as e:
            self.log.error(
                "Unable to switch into the frame")
            return False

    def switchtoparentframe(self):
        self.driver.switch_to.default_content()
        self.log.info("Switched to the parent frame")

    def getcurrentwindowid(self):
        currentwindowid = self.driver.current_window_handle
        self.log.info("Obtained window id is "+currentwindowid)
        return currentwindowid

    def getallwindowids(self):
        listofwindowids = self.driver.window_handles
        self.log.info("Obtained window ids - "+listofwindowids)
        return listofwindowids

    def switchtowindow(self,id=None):
        self.driver.switch_to.window(id)
        self.log.info("Switched to window with window id - "+id)

    def mouseover(self,locatorvalue,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue, locatortype)
            act = ActionChains(self.driver)
            act.move_to_element(element).perform()
            self.log.info(
                "Moved to element with locator type " + locatortype + " and locator value " + locatorvalue)
        except Exception as e:
            self.log.error(
                "Unable to move to element with locator type " + locatortype + " and locator value " +
                locatorvalue + str(e))
            return False

    def mouse_clickandhold(self, locatorvalue, locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue, locatortype)
            act = ActionChains(self.driver)
            act.click_and_hold(element).perform()
            self.log.info(
                "Click and hold to element with locator type " + locatortype + " and locator value " + locatorvalue)
        except Exception as e:
            self.log.error(
                "Unable to click and hold to element with locator type " + locatortype + " and locator value " +
                locatorvalue + str(e))
            return False

    def movetoelementandrelease(self,locatorvalue, locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            element = self.getElement(locatorvalue, locatortype)
            act = ActionChains(self.driver)
            act.move_to_element(element).release().perform()
            self.log.info(
                "moved to element with locator type " + locatortype + " and locator value " + locatorvalue)
        except Exception as e:
            self.log.error(
                "Unable to move to element with locator type " + locatortype + " and locator value " +
                locatorvalue + str(e))
            return False

    def scrollthepage(self,x,y):
        self.driver.execute_script("window.scrollBy("+x+","+y+"")

    def explicitwaitforelementandclick(self,locatorvalue,timeout=20,poll_frequency=2,locatortype="id/name/xpath/css/linktext/partiallinktext"):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                                                ElementClickInterceptedException])
            bytype = self.getbytype(locatortype)
            ele1 = wait.until(EC.element_to_be_clickable((bytype, locatorvalue)))
            ele1.click()
            self.log.info(
                "waited for element with timeout "+str(timeout)+" and clicked on element with locator type " + locatortype + " and locator value " + locatorvalue)
        except Exception as e:
            self.log.error(
                "Unable to wait for element with locator type " + locatortype + " and locator value " +
                locatorvalue + str(e) +"even after time out "+str(timeout))
            return False

    def explicitwaitfortitlecontains(self,title,timeout=20,poll_frequency=2):
        try:
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                                                ElementClickInterceptedException])
            wait.until(EC.title_contains, title)
            self.log.info(
                "Title of the page is  found within time out "+str(timeout)+"")
        except Exception as e:
            self.log.error("Unable to obtain title of the page even after time out "+str(timeout))
            return False

    def getjavascriptpopuptext(self):
        return self.driver.switch_to.alert.text

    def acceptjspopup(self):
        self.driver.switch_to.alert.accept()
        self.log.info("Accepted the JS alert")

    def dismissjspopup(self):
        self.driver.switch_to.alert.dimiss()
        self.log.info("Cancelled the JS alert")

    def screenshot(self,scname):
        try:
            self.driver.save_screenshot(sys[1]+"//screenshots//"+scname+".png")
            self.log.info("Screen shot taken and saved ")
        except Exception as e:
            self.log.error("Exception while taking the screen shot "+e)