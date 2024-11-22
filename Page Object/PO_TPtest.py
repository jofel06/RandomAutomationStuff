from selenium import webdriver
from PO_TrialPage import TrialPage


browser = webdriver.Chrome()

trial_page = TrialPage(driver=browser)
trial_page.go()

trial_page.stone_input.input_text('Rock')
trial_page.stone_button.click()
sec_password = trial_page.secret_password.text()
trial_page.secrets_input.input_text(sec_password)
trial_page.secret_button.click()
trial_page.rich_merchant.input_text('Jessica')
trial_page.rich_button.click()
trial_page.check_answer_button.click()



