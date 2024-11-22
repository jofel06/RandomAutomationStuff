from Base_Page import BasePage
from selenium.webdriver.common.by import By
from PO_BaseElement import BaseElement
from Locator import Locator

class TrialPage(BasePage):

    url = 'https://techstepacademy.com/trial-of-the-stones'
    @property
    def stone_input(self):
        locator = Locator(By.ID, 'r1Input')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def stone_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def secret_password(self):
        locator = Locator(By.CSS_SELECTOR, 'div#passwordBanner > h4')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def secrets_input(self):
        locator = Locator(By.ID, 'r2Input')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def secret_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r2Butn')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def rich_merchant(self):
        locator = Locator(By.ID, 'r3Input')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def rich_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r3Butn')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def check_answer_button(self):
        locator = Locator(By.ID, 'checkButn')
        return BaseElement(driver=self.driver, locator = locator)





#by=By.XPATH, value='div[@ID="passwordBanner"]/h4')[0].innerHTML