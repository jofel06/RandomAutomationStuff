from selenium import webdriver
from Homepage import HomePage
from time import sleep


browser = webdriver.Chrome()

training_ground = HomePage(driver=browser)
training_ground.go()

training_ground.input_field1.input_text('This is the first field')
sleep(2)
training_ground.button_1.click()
training_ground.button_2.click()
training_ground.input_field2.input_text('This is the second field')
training_ground.button_3.click()
training_ground.button_4.click()
sleep(2)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # Scroll to bottom
sleep(2)
training_ground.drop_down.select_value('Battlestar Galactica')
sleep(2)
browser.execute_script("window.scrollTo(100, 0)") # Scroll to top


