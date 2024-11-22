from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    """Purpose: This method locates the web element using the locator"""
    def find(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    """Purpose: used to send text to a web element"""
    def input_text(self, text):
        self.web_element.send_keys(text)

    """Purpose: This method waits until the element is clickable and then clicks it"""
    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator))
        element.click()
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except TimeoutException:
            print("No alert appeared within the timeout period")

    def select_value(self, text):
        select = Select(self.web_element)
        select.select_by_visible_text(text)