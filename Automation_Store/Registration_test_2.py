from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

browser = webdriver.Chrome()
browser.get('https://automationteststore.com/')

#Locators
login_register = browser.find_element(By.LINK_TEXT, 'Login or register')
login_register.click()
register_continue = browser.find_element(By.XPATH, '//div[@class="loginbox"]//button')
register_continue.click()

#Locators
input_first_name =  browser.find_element(By.ID, 'AccountFrm_firstname')
input_last_name = browser.find_element(By.ID, 'AccountFrm_lastname')
input_email = browser.find_element(By.ID, 'AccountFrm_email')
input_address1 = browser.find_element(By.ID, 'AccountFrm_address_1')
input_city = browser.find_element(By.ID, 'AccountFrm_city')
input_zip = browser.find_element(By.ID, 'AccountFrm_postcode')
select_country = Select(browser.find_element(By.ID, 'AccountFrm_country_id'))
select_region_state = Select(browser.find_element(By.XPATH, '//select[@ID="AccountFrm_zone_id"]'))
create_login_name =  browser.find_element(By.ID, 'AccountFrm_loginname')
create_password =  browser.find_element(By.ID, 'AccountFrm_loginname')
confirm_create_password = browser.find_element(By.ID, 'AccountFrm_confirm')
subscribe_newsletter = browser.find_element(By.ID,'AccountFrm_newsletter1')
privacy_policy_click = browser.find_element(By.XPATH, '//label[@class="col-md-6 mt20 mb40"]//a')
privacy_button_close = browser.find_element(By.CSS_SELECTOR, 'button[class="close"]')
privacy_checkbox = browser.find_element(By.ID, "AccountFrm_agree")
registration_continue = browser.find_element(By)

#Locators Login details
input_login_name = browser.find_element(By.ID, 'AccountFrm_loginname')
input_password = browser.find_element(By.ID, 'AccountFrm_password')
input_confirm_password = browser.find_element(By.ID, 'AccountFrm_confirm')

# Input Personal details
input_first_name.send_keys('Username')
input_last_name.send_keys('Lastname')
input_email.send_keys('E-mail address')
input_address1.send_keys('I am Address 1')
input_city.send_keys('this is City')
input_zip.send_keys('this is Zip code')

select_country.select_by_visible_text('Yemen')
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//select[@ID='AccountFrm_zone_id']/option[text()='Adan']")))
select_region_state.select_by_visible_text('Adan')

#Create Login Details
create_login_name.send_keys('My Username')
create_password.send_keys('My Password')
confirm_create_password.send_keys('Confirm my Password')

subscribe_newsletter.click()
privacy_policy_click.click()
sleep(2)
privacy_button_close.click()
privacy_checkbox.click()