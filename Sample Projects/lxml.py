from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

divs = browser.find_elements(By.XPATH, '//div/span/..')
tree = etree.HTML(browser.page_source)
tree.findall('//div')
tree.findall('//div/span/..')
