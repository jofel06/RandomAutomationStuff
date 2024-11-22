from selenium.webdriver.common.by import By

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):     #navigates to the TrainingGround page
        self.driver.get(self.url)     #Implementation, to load the page in the browser.

    def input_field1(self, text):
        input1 = self.driver.find_element(By.CSS_SELECTOR,'input#ipt1')
        input1.clear()    #clears any existing text
        input1.send_keys(text)    #enters the provided text into the input field
        return None

    def get_input_text(self):
        input1 = self.driver.find_element(By.CSS_SELECTOR,'input#ipt1')
        elem_text = input1.get_attribute('value')     #Retrieves the current text from the input field
        return elem_text

    def click_button1(self):
        button1 = self.driver.find_element(By.CSS_SELECTOR, 'button#b1')
        button1.click()
        return None


#TEST Setup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = webdriver.Chrome()

training_page = TrainingGroundPage(driver=browser)   #Creates an instance of TrainingGroundPage, passing the browser instance to it.
training_page.go()     #Calls the go method to navigate to the "Training Ground" page.

test_value = 'It worked'
training_page.input_field1(test_value)
sleep(2)

training_page.click_button1()
WebDriverWait(browser, 10).until(alert_is_present())
Alert(browser).accept()

txt_from_input = training_page.get_input_text() #Retrieves the text from the input field
assert txt_from_input == test_value, f'Test Failed: input did not match expected ({test_value})'
print("Test Passed")

while(True):
    pass
