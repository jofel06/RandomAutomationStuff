from selenium.webdriver.common.by import By
from PO_BaseElement import BaseElement
from Base_Page import BasePage
from Locator import Locator

class TrainingGroundPage(BasePage):
    url = 'https://techstepacademy.com/training-ground'

    @property
    def button1(self):
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(driver=self.driver, locator = locator)
