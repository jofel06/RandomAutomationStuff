from selenium import webdriver
from time import sleep
from Registration_page import drop_down
from Registration_page import Homepage
import logging

browser = webdriver.Chrome()

logging.basicConfig(level=logging.INFO)
logging.info("Starting test...")

registration_page = Homepage(driver=browser)
registration_page.go()

login_link = registration_page.register_login
login_link.button_click()
registration_page.cont_button.button_click()

registration_page.first_name.text_input('sample')
registration_page.last_name().text_input('sample')
registration_page.email_add().text_input('sample@gmail.com')
registration_page.address_1().text_input('Mabuhay')
registration_page.input_city().text_input('Laguna')
registration_page.input_zip().text_input('0001')
dd_country = registration_page.select_country()
dd_country.drop_down_select('Philippines')
drop_down(browser) # Wait for the Region/State dropdown options to refresh
dd_region_state = registration_page.select_region_state()
dd_region_state.drop_down_select('Abra')

sleep(2)
browser.execute_script('window.scrollBy(0, 500)')
sleep(2)
registration_page.create_login().text_input('sample')
registration_page.create_password().text_input('sample')
registration_page.confirm_password().text_input('samplesample')
radio_button_no = registration_page.r_button_no()
radio_button_no.button_click()
sleep(2)
privacy_policy_click = registration_page.privacy_policy()
privacy_policy_click.button_click()
sleep(2)
browser.execute_script('window.scrollBy(0, 1000)')
privacy_close_button = registration_page.privacy_close()
privacy_close_button.button_click()
sleep(1)
privacy_check = registration_page.privacy_check_box()
privacy_check.button_click()
sleep(2)
continue_button = registration_page.continue_button()
continue_button.button_click()

