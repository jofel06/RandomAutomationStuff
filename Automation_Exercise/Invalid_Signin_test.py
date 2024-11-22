from Page_Locator import InvalidSignin
from selenium import webdriver
import logging

# Setup logging to ensure logs are displayed

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Initialize the browser and start the test
logger.info("Launching Firefox browser")
browser = webdriver.Firefox()
browser.get('https://automationexercise.com/')

try:
    valid_signin_test = InvalidSignin(browser)

    # Navigate to Signup/Login page
    logger.info("Navigating to Signup/Login page")
    signup_login = valid_signin_test.signup_login()
    signup_login.click()

    # Enter valid email and password
    logger.info("Entering valid email and password")
    valid_signin_test.enter_invalidemail().input('lacev41600@ploncy.com')
    valid_signin_test.enter_invalidpassword().input('sample1010')

    # Click the login button
    logger.info("Clicking login button")
    login_button = valid_signin_test.login_button()
    login_button.click()

    # Add logging for assertions or checks if needed
    logger.info("Login attempt made")

finally:
    logger.info("Test completed, closing browser")
    browser.quit()
