from Base_page import BasePage
from selenium.webdriver.common.by import By
from Base_Element import BaseElement
from locator import Locator

class HomePage(BasePage):
    url = 'https://techstepacademy.com/training-ground'

    @property
    def input_field1(self):
        locator = Locator(By.ID, 'ipt1')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def button_1(self):
        locator = Locator(By.ID, 'b1')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def button_2(self):
        locator = Locator(By.ID, 'b2')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def input_field2(self):
        locator = Locator(By.ID, 'ipt2')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def button_3(self):
        locator = Locator(By.ID, 'b3')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def button_4(self):
        locator = Locator(By.ID, 'b4')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def drop_down(self):
        locator = Locator(By.ID, 'sel1')
        return BaseElement(driver=self.driver, locator = locator)


