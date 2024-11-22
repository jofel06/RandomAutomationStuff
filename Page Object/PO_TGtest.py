from selenium import webdriver
from PO_TrainingGround import TrainingGroundPage

#Test setup
browser = webdriver.Chrome()
test_value = 'It worked'

TG_page = TrainingGroundPage(driver=browser)
TG_page.go()
TG_page.button1.click()