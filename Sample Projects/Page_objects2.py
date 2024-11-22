from selenium.webdriver.common.by import By

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        """Navigate to the Training Ground page."""
        self.driver.get(self.url)

    def input_text(self, text):
        """Enter text into the input field."""
        input_field = self.driver.find_element(By.CSS_SELECTOR, 'input#ipt1')
        input_field.clear()
        input_field.send_keys(text)

    def click_button1(self):
        """Click Button 1."""
        button1 = self.driver.find_element(By.CSS_SELECTOR, 'button#b1')
        button1.click()

#Test Script

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

# Test Setup: Initialize WebDriver
browser = webdriver.Chrome()

try:
    # Test: Navigate to Training Ground page
    training_page = TrainingGroundPage(driver=browser)
    training_page.go()

    # Input text 'It worked' in the input field
    test_value = 'It worked'
    training_page.input_text(test_value)

    # Optionally, wait to observe the action
    sleep(2)

    # Click Button 1
    training_page.click_button1()

    # Handle the alert that appears after clicking the button
    WebDriverWait(browser, 10).until(alert_is_present())
    Alert(browser).accept()

finally:
    # Clean up: Close the browser
    browser.quit()