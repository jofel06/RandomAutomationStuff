from Base_Page import BasePage
from Base_Element import BaseElement
from Locator import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Exp_Con
from selenium.webdriver.support.wait import WebDriverWait


class Homepage(BasePage):

    url = 'https://automationteststore.com/'

    @property
    def register_login(self):
        locator = Locator(By.LINK_TEXT, 'Login or register')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def cont_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[title="Continue"]')
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def first_name(self):
        locator = Locator(By.ID, 'AccountFrm_firstname')
        return BaseElement(driver=self.driver, locator = locator)

    def last_name(self):
        locator = Locator(By.ID, 'AccountFrm_lastname')
        return BaseElement(driver=self.driver, locator = locator)

    def email_add(self):
        locator = Locator(By.ID, 'AccountFrm_email')
        return BaseElement(driver=self.driver, locator = locator)

    def address_1(self):
        locator = Locator(By.ID, 'AccountFrm_address_1')
        return BaseElement(driver=self.driver, locator = locator)

    def input_city(self):
        locator = Locator(By.ID, 'AccountFrm_city')
        return BaseElement(driver=self.driver, locator = locator)

    def select_country(self):
        locator = Locator(By.ID, 'AccountFrm_country_id')
        return BaseElement(driver=self.driver, locator=locator)

    def select_region_state(self):
        locator = Locator(By.ID, 'AccountFrm_zone_id')
        return BaseElement(driver=self.driver, locator=locator)

    def input_zip(self):
        locator = Locator(By.ID, 'AccountFrm_postcode')
        return BaseElement(driver=self.driver, locator = locator)

    def create_login(self):
        locator = Locator(By.ID, 'AccountFrm_loginname')
        return BaseElement(driver=self.driver, locator = locator)

    def create_password(self):
        locator = Locator(By.ID, 'AccountFrm_password')
        return BaseElement(driver=self.driver, locator = locator)

    def confirm_password(self):
        locator = Locator(By.ID, 'AccountFrm_confirm')
        return BaseElement(driver=self.driver, locator = locator)

    def r_button_no(self):
        locator = Locator(By.ID, 'AccountFrm_newsletter0')
        return BaseElement(driver=self.driver, locator = locator)

    def privacy_policy(self):
        locator = Locator(By.CSS_SELECTOR, 'a[onclick]')
        return BaseElement(driver=self.driver, locator=locator)

    def privacy_close(self):
        locator = Locator(By.XPATH, '//div[@class="modal-footer"]/button')
        return BaseElement(driver=self.driver, locator=locator)

    def continue_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[title="Continue"]')
        return BaseElement(driver=self.driver, locator = locator)

    def privacy_check_box(self):
        locator = Locator(By.ID, 'AccountFrm_agree')
        return BaseElement(driver=self.driver, locator=locator)

#Dynamic Dropdown, define that it will wait until the value appears
def drop_down(driver):
    WebDriverWait(driver, 20).until(Exp_Con.presence_of_element_located((By.XPATH, "//select[@id='AccountFrm_zone_id']/option[text()='Abra']")))



class AddToCart(BasePage):

    url = 'https://automationteststore.com/'

    @property
    def apparel_accessories(self):
        locator = Locator(By.XPATH, "//a[contains(text(), '\u00A0\u00A0Apparel & accessories')]")
        return BaseElement(driver=self.driver, locator = locator)

    @property
    def apparel_shoes_link(self):
        locator = Locator(By.XPATH, "//a[contains(text(), '\u00A0\u00A0Apparel & accessories')]/..//a[text()='\u00A0\u00A0\u00A0\u00A0Shoes']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def new_ladies_shoes(self):
        locator = Locator(By.CSS_SELECTOR, "a[title='New Ladies High Wedge Heel Toe Thong Diamante Flip Flop Sandals']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def new_ladies_shoes_size(self):
        locator = Locator(By.ID, 'option344747')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def new_ladies_shoes_add_to_cart(self):
        locator = Locator(By.XPATH, "//ul[@class='productpagecart']//a")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def men_link(self):
        locator = Locator(By.XPATH, "//ul[@class='nav-pills categorymenu']//a[text()='\u00A0\u00A0Men']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def mens_fragrance_set(self):
        locator = Locator(By.XPATH, "//ul[@class='nav-pills categorymenu']//li//li//a[text()='\u00A0\u00A0\u00A0\u00A0Fragrance Sets']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def man_fragrance_item(self):
        locator = Locator(By.XPATH, "//a[@title='Euphoria Men Intense Eau De Toilette Spray']/../../..//i[@class='fa fa-cart-plus fa-fw']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fragrance_link(self):
        locator = Locator(By.XPATH, "//ul[@class='nav-pills categorymenu']//a[text()='\u00A0\u00A0Fragrance']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fragrance_men(self):
        locator = Locator(By.XPATH, "//ul[@class='nav-pills categorymenu']//li//li//a[text()='\u00A0\u00A0\u00A0\u00A0Men']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fragrance_men_item(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="ck one shock for him Deodorant"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def fragrance_men_item_add_to_cart(self):
        locator = Locator(By.CSS_SELECTOR, "ul[class='productpagecart']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def change_quantity(self):
        locator = Locator(By.XPATH, "//div[@class='input-group input-group-sm']//input[@id='cart_quantity62']")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def update_cart_button(self):
        locator = Locator(By.ID, "cart_update")
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def cart_checkout_button(self):
        locator = Locator(By.ID,"cart_checkout1")
        return BaseElement(driver=self.driver, locator=locator)
