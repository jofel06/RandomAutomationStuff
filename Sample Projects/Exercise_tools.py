from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import Select
import selenium.common.exceptions


browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')

#Declare
button_1 = browser.find_element(By.CSS_SELECTOR, 'button[id="b1"]')


print('I have arrived')
sleep(2)

#Alert
try:
    button_1.click()
    WebDriverWait(browser, 10).until(alert_is_present())
    print('An Alert appeared')
    Alert(browser).accept()
except selenium.common.exceptions.TimeoutException:
    print('Alert did not appear on time')


sleep(2)
Select_1 = browser.find_element(By.ID, 'sel1') #Drop down
my_select = Select(Select_1)
my_select.select_by_index(1) #to select the str in the drop down

while(True):
    pass