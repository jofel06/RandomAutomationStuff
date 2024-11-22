from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://automationteststore.com/')
sleep(2)

apparel_accessories_link = browser.find_element(By.XPATH, "//a[contains(text(), '\u00A0\u00A0Apparel & accessories')]") #&NBSP
actions = ActionChains(browser)
actions.move_to_element(apparel_accessories_link).perform()
apparel_shoes_link = browser.find_element(By.XPATH, "//a[contains(text(), '\u00A0\u00A0Apparel & accessories')]/..//a[text()='\u00A0\u00A0\u00A0\u00A0Shoes']")
apparel_shoes_link.click()


new_ladies_shoes = browser.find_element(By.CSS_SELECTOR, "a[title='New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals']")
new_ladies_shoes.click()
new_ladies_shoes_size = browser.find_element(By.ID, 'option344747')
new_ladies_shoes_size.click()
sleep(1)
new_ladies_shoes_add_to_cart = browser.find_element(By.XPATH, "//ul[@class='productpagecart']//a")
new_ladies_shoes_add_to_cart.click()
sleep(2)


men_link = browser.find_element(By.XPATH, "//ul[@class='nav-pills categorymenu']//a[text()='\u00A0\u00A0Men']") #&NBSP
actions.move_to_element(men_link).perform()
sleep(1)
mens_fragrance_set = browser.find_element(By.XPATH, "//ul[@class='nav-pills categorymenu']//li//li//a[text()='\u00A0\u00A0\u00A0\u00A0Fragrance Sets']")
mens_fragrance_set.click()
sleep(2)
man_fragrance_item = browser.find_element(By.XPATH, "//a[@title='Euphoria Men Intense Eau De Toilette Spray']/../../..//i[@class='fa fa-cart-plus fa-fw']")
man_fragrance_item.click()
browser.execute_script('window.scrollBy(1000, 0)')


sleep(2)
fragrance_link = browser.find_element(By.XPATH, "//ul[@class='nav-pills categorymenu']//a[text()='\u00A0\u00A0Fragrance']")
actions.move_to_element(fragrance_link).perform()
sleep(1)
fragrance_men = browser.find_element(By.XPATH, "//ul[@class='nav-pills categorymenu']//li//li//a[text()='\u00A0\u00A0\u00A0\u00A0Men']")
fragrance_men.click()
sleep(1)
fragrance_men_item = browser.find_element(By.CSS_SELECTOR, 'a[title="ck one shock for him Deodorant"]')
fragrance_men_item.click()
sleep(1)
fragrance_men_item_add_to_cart = browser.find_element(By.CSS_SELECTOR, "ul[class='productpagecart']")
fragrance_men_item_add_to_cart.click()
sleep(1)
change_quantity = browser.find_element(By.XPATH, "//div[@class='input-group input-group-sm']//input[@id='cart_quantity62']")
change_quantity.clear()
change_quantity.send_keys('3')
update_cart_button = browser.find_element(By.ID, "cart_update")
update_cart_button.click()
sleep(2)
cart_checkout_button = browser.find_element(By.ID,"cart_checkout1")
cart_checkout_button.click()
Automation_Store_homepage = browser.find_element(By.XPATH, "//a[@class='logo']//img[@alt='Automation Test Store']")
Automation_Store_homepage.click()
sleep(1)
browser.execute_script('window.scrollBy(0,1000)')
sleep(1)
go_top_arrow = browser.find_element(By.CSS_SELECTOR,"a[id='gotop']")
go_top_arrow.click()
sleep(1)
specials_option = browser.find_element(By.XPATH,"//ul[@id='main_menu_top']//a[@class='top menu_specials']")
specials_option.click()
sleep(1)

specials_sort_by = Select(browser.find_element(By.ID, 'sort'))
specials_sort_by.select_by_index(1)
sleep(2)
specials_sort_by = Select(browser.find_element(By.ID, 'sort'))
specials_sort_by.select_by_visible_text('Rating Lowest')
sleep(2)
specials_sort_by = Select(browser.find_element(By.ID, 'sort'))
specials_sort_by.select_by_value('rating-DESC')
sleep(2)

ListView_icon = browser.find_element(By.CSS_SELECTOR,"i[class='fa fa-th-list']")
ListView_icon.click()
sleep(2)
write_review = browser.find_element(By.XPATH, "//div[@class='col-md-8']//a[text()='BeneFit Girl Meets "
                                              "Pearl							(483857)']/..//a[@class='compare']")
write_review.click()
sleep(1)
StarRating = browser.find_element(By.CSS_SELECTOR, 'div[id="rating3"]')
StarRating.click()
Ratings_Name = browser.find_element(By.CSS_SELECTOR, "input[id='name']")
Ratings_Name.send_keys('Random Stranger')
Review_Area = browser.find_element(By.CSS_SELECTOR, "textarea")
Review_Area.send_keys('Here is my review. \n'
                      'This is a Great website to practice automation.\n'
                      'You will learn a lot of Great Things here')
captcha_input = browser.find_element(By.ID, "captcha")
captcha_input.send_keys('00000')

