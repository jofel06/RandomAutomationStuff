from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/iframe-training')

#Iframe
iframe_element = browser.find_element(By.CSS_SELECTOR, 'iframe')
browser.switch_to.frame(iframe_element) #to switch to the iframe in the webpage
iframe_text = browser.find_element(By.CSS_SELECTOR,'div#block-ec928cee802cf918d26c div p')
print('I am inside the Iframe')
sleep(2)

input_1 = browser.find_element(By.CSS_SELECTOR, 'input#ipt1') #first input field
input_1.send_keys('Hello')
sleep(2)
button_1 = browser.find_element(By.CSS_SELECTOR, 'button#b1') #first button
button_1.click()
#for the alert after pressing the button
WebDriverWait(browser, 10).until(alert_is_present())
Alert(browser).accept()

sleep(2)

#switch back to default
browser.switch_to.default_content()
title_text = browser.find_element(By.CSS_SELECTOR, 'div#block-5d3de848045889000188d389')

print("I am back outside the Iframe")
