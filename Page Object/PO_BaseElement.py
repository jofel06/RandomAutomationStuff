
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver   #An instance of the Selenium WebDriver, which controls the browser.
        self.locator = locator  #The value used to locate the web element (e.g., the ID, class name, or any other attribute).
                                #The method used to locate the element (e.g., By.ID, By.CLASS_NAME).
                                # A tuple combining by and value, # which is used to identify the element on the

        self.web_element = None #Initially set to None, this will store the actual web element found on the page.
        self.find()  # The find method is called automatically when a BaseElement object is created, locating the web element.

    """Purpose: This method locates the web element using the locator"""
    def find(self):
        element = WebDriverWait(self.driver, 10).until(   #Waits up to 10 seconds for the condition to be met.
            EC.visibility_of_element_located(locator=self.locator))     #This expected condition waits until the element is both present in the DOM and visible (displayed).
        self.web_element = element      # Stores the found element in self.web_element so that other methods can interact with it.
        return None

    """Purpose: used to send text to a web element"""
    def input_text(self, text):
        self.web_element.send_keys(text)

    """Purpose: This method waits until the element is clickable and then clicks it"""
    def click(self):
        element = WebDriverWait(self.driver, 10).until(  #Waits up to 10 seconds for the element to become clickable.
            EC.element_to_be_clickable(self.locator))   #This expected condition waits until the element is visible and enabled (clickable).
        element.click()

    """Purpose: This method returns the text content of the web element"""
    def text(self):
        text = self.web_element.text    #Retrieves the text from the found web element.
        return text


