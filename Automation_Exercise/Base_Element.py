from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class MainElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.locate_element()


    def wait_for_element(self, condition):
        return WebDriverWait(self.driver, 10).until(condition(self.locator))

    def locate_element(self):
        self.web_element = self.wait_for_element(EC.visibility_of_element_located)

    def is_displayed(self):
        return self.web_element.is_displayed()

    def input(self, text):
        if self.web_element:
            self.web_element.send_keys(text)
        else:
            raise Exception("Element not found for input operation")

    def click(self):
        if self.web_element:
            element = self.wait_for_element(EC.element_to_be_clickable)
            element.click()
        else:
            raise Exception("Element not found for click operation")

    def select_dropdown(self, text):
        if self.web_element:
            select = Select(self.web_element)
            select.select_by_visible_text(text)
        else:
            raise Exception("Element not found for dropdown selection")

    def hover_to(self):
        if self.web_element:
            action = ActionChains(self.driver)
            action.move_to_element(self.web_element).perform()
        else:
            raise Exception("Element not found for hover operation")

    def get_attribute(self, attribute_name):
        if self.web_element:
            value = self.web_element.get_attribute(attribute_name)
            print('Element Changed')
            return value
        else:
            raise Exception("Element not found for dropdown selection")



