from Registration_page import AddToCart
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()

Test_run = AddToCart(driver=browser)
Test_run.go()

apparel_accessories_link = Test_run.apparel_accessories
apparel_accessories_link.hover_to_element()
sleep(1)
apparel_shoes = Test_run.apparel_shoes_link
apparel_shoes.button_click()
sleep(1)
ladies_shoes = Test_run.new_ladies_shoes
ladies_shoes.button_click()
sleep(1)
ladies_shoes_size = Test_run.new_ladies_shoes_size
ladies_shoes_size.button_click()
sleep(1)
ladies_shoes_add_cart = Test_run.new_ladies_shoes_add_to_cart
ladies_shoes_add_cart.button_click()
sleep(1)
men_hover_link = Test_run.men_link
men_hover_link.hover_to_element()
sleep(1)
mens_fragrance_link = Test_run.mens_fragrance_set
mens_fragrance_link.button_click()
sleep(1)
mens_fragrance_item = Test_run.man_fragrance_item
mens_fragrance_item.button_click()
sleep(1)
fragrance_hover_link = Test_run.fragrance_link
fragrance_hover_link.hover_to_element()
sleep(1)
fragrance_men_link = Test_run.fragrance_men
fragrance_men_link.button_click()
sleep(1)
fragrance_men_item_pick = Test_run.fragrance_men_item
fragrance_men_item_pick.button_click()
sleep(1)
fragrance_men_add_cart = Test_run.fragrance_men_item_add_to_cart
fragrance_men_add_cart.button_click()
sleep(1)
change_quantity_3 = Test_run.change_quantity.web_element
change_quantity_3.clear()
change_quantity_3.send_keys('3')
sleep(2)
update_cart_button_press = Test_run.update_cart_button
update_cart_button_press.button_click()
sleep(1)
cart_checkout_button_press = Test_run.cart_checkout_button
cart_checkout_button_press.button_click()


