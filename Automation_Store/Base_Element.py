from selenium.webdriver.support import expected_conditions as Exp_Con
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class BaseElement(object):
    def __init__(self, locator, driver):
        self.locator = locator
        self.driver = driver
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(Exp_Con.visibility_of_element_located(locator=self.locator))
        self.web_element = element

    def text_input(self, text):
        self.web_element.send_keys(text)

    def button_click(self):
        element = WebDriverWait(self.driver, 10).until(Exp_Con.element_to_be_clickable(self.locator))
        element.click()

    def drop_down_select(self, text):
        select = Select(self.web_element)
        select.select_by_visible_text(text)

    def hover_to_element(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.web_element).perform()
