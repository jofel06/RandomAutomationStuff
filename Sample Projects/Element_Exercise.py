
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')

#input_element = browser.find_element(By.CSS_SELECTOR,'input[id="ipt2"]') #an input field
#input_css_locator.send_keys('This is the Second Field')
#input2_element = browser.find_element(By.CSS_SELECTOR,'input_css_locator') #an input field
#input2_element.send_keys('This is the Second Field')

#declare locator
input1_css_locator = 'input[id="ipt1"]' # declare using CSS locator
input2_css_locator = 'input[id="ipt2"]' # declare using CSS locator
button4_xpath_locator = '//button[@id="b4"]' # declare using xpath locator

#Assign elements
input1_element = browser.find_element(By.CSS_SELECTOR, input1_css_locator)
input2_element = browser.find_element(By.CSS_SELECTOR, input2_css_locator)
button4_element = browser.find_element(By.XPATH, button4_xpath_locator)

#Manipulate elements
input1_element.send_keys('This is the first field')
sleep(2)
input2_element.send_keys('This is the second field')
sleep(2)
button4_element.click()

#$x('//b[text()="Product 1"]')
#$x('//b[text()="Product 1"]/../../p')[0].innerHTML