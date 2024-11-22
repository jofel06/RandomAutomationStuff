#from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() #call the chrome webdriver
browser.get('https://techstepacademy.com/training-ground') #to get the URL

input_element = browser.find_element(By.CSS_SELECTOR,'input[id="ipt1"]') #an input field
input_element.send_keys('This is the First Field')

button1_element = browser.find_element(By.CSS_SELECTOR, 'button[id="b1"]') #button 1
button1_element.click()


while(True):
    pass

#sleep(5000)