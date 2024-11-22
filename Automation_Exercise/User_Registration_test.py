from Page_Locator import UserRegistration
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
Registration_test = UserRegistration(browser)

signup_login = Registration_test.signup_login()
signup_login.click()
Registration_test.signup_name().input('sample')
Registration_test.signup_email().input('lacev41600@ploncy.com')
signup_button = Registration_test.signup_button()
signup_button.click()

sleep(2)
"""Enter Account Information"""
title_rbutton = Registration_test.title_rbutton()
title_rbutton.click()
Registration_test.signup_password().input('sample1010')
Registration_test.select_day().select_dropdown('3')
Registration_test.select_month().select_dropdown('March')
Registration_test.select_years().select_dropdown('1990')
signup_newsletter = Registration_test.signup_newsletter()
signup_newsletter.click()
signup_special_offers = Registration_test.signup_special_offers()
signup_special_offers.click()
sleep(2)

"""Address Information"""
Registration_test.signup_firstname().input('first name')
Registration_test.signup_lastname().input('last name')
Registration_test.signup_company().input('Company')
Registration_test.signup_address1().input('this is address 1')
Registration_test.signup_zip().input('this is address 2')
Registration_test.select_country().select_dropdown('Singapore')
Registration_test.signup_state().input('state it is')
Registration_test.signup_city().input('this is city')
Registration_test.signup_zip().input('my zip code')
Registration_test.signup_mobilenumber().input('09000000022')
create_account = Registration_test.create_account()
create_account.click()
