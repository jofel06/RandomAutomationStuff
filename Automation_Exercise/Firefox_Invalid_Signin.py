from Page_Locator import InvalidSignin
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
valid_signin_test = InvalidSignin(browser)


signup_login = valid_signin_test.signup_login()
signup_login.click()
sleep(2)
valid_signin_test.enter_validemail().input('lacev41600@ploncy.com')
valid_signin_test.enter_validpassword().input('sample1010')
sleep(1)
login_button = valid_signin_test.login_button()
login_button.click()

