from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

#declare locator
input1_locator = 'input[id="r1Input"]' #using CSS locator

#2 METHODS
#input1_result = browser.find_element(By.XPATH, '//div[@id="passwordBanner"]/h4')
input1_result = browser.find_element(By.CSS_SELECTOR, 'div#passwordBanner > h4')

input2_locator = '//input[@id="r2Input"]' #using xpath locator
button1_locator = 'button[id="r1Btn"]'
button2_locator = 'button[id="r2Butn"]'
input3_locator = '//input[@name="r3Input"]'
button3_locator = browser.find_element(By.XPATH, '//button[@id="r3Butn"]')
button4_locator = browser.find_element(By.XPATH, '//button[@name="checkButn"]')

#Assign elements
input_1 = browser.find_element(By.CSS_SELECTOR, input1_locator)
input_2 = browser.find_element(By.XPATH, input2_locator)
button_1 = browser.find_element(By.CSS_SELECTOR, button1_locator)
button_2 = browser.find_element(By.CSS_SELECTOR, button2_locator)

#RUN SCRIPT
input_1.send_keys('rock')
sleep(1)
button_1.click()
sleep(1)

input_password = input1_result.text
input_2.send_keys(input_password)

sleep(1)
button_2.click()
sleep(1)
input_3 = browser.find_element(By.XPATH, input3_locator)
input_3.send_keys('Jessica')
sleep(1)
button3_locator.click()
sleep(1)
button4_locator.click()

while(True):
    pass


#$x('//b[text()="Jessica"]/../../p')[0].innerHTML