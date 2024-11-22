from Base_Element import MainElement
from selenium.webdriver.common.by import By

class UserRegistration(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://automationexercise.com/')  # Load the page in the constructor

    def signup_login(self):
        locator = (By.XPATH, "//ul[@class='nav navbar-nav']//a[@href='/login']")
        return MainElement(driver=self.driver, locator = locator)

    def signup_name(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
        return MainElement(driver=self.driver, locator = locator)

    def signup_email(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
        return MainElement(driver=self.driver, locator = locator)

    def signup_button(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
        return MainElement(driver=self.driver, locator = locator)

    def title_rbutton(self):
        locator = (By.ID, "id_gender1")
        return MainElement(driver=self.driver, locator = locator)

    def signup_password(self):
        locator = (By.ID, "password")
        return MainElement(driver=self.driver, locator = locator)

    def select_day(self):
        locator = (By.ID, "days")
        return MainElement(driver=self.driver, locator = locator)

    def select_month(self):
        locator = (By.ID, "months")
        return MainElement(driver=self.driver, locator = locator)

    def select_years(self):
        locator = (By.ID, "years")
        return MainElement(driver=self.driver, locator = locator)

    def signup_newsletter(self):
        locator = (By.ID, "newsletter")
        return MainElement(driver=self.driver, locator = locator)

    def signup_special_offers(self):
        locator = (By.ID, "optin")
        return MainElement(driver=self.driver, locator = locator)

    def signup_firstname(self):
        locator = (By.ID, "first_name")
        return MainElement(driver=self.driver, locator = locator)

    def signup_lastname(self):
        locator = (By.ID, "last_name")
        return MainElement(driver=self.driver, locator = locator)

    def signup_company(self):
        locator = (By.ID, "company")
        return MainElement(driver=self.driver, locator = locator)

    def signup_address1(self):
        locator = (By.ID, "address1")
        return MainElement(driver=self.driver, locator = locator)

    def signup_address2(self):
        locator = (By.ID, "address2")
        return MainElement(driver=self.driver, locator = locator)

    def select_country(self):
        locator = (By.ID, "country")
        return MainElement(driver=self.driver, locator = locator)

    def signup_state(self):
        locator = (By.ID, "state")
        return MainElement(driver=self.driver, locator = locator)

    def signup_city(self):
        locator = (By.ID, "city")
        return MainElement(driver=self.driver, locator = locator)

    def signup_zip(self):
        locator = (By.ID, "zipcode")
        return MainElement(driver=self.driver, locator = locator)

    def signup_mobilenumber(self):
        locator = (By.ID, "mobile_number")
        return MainElement(driver=self.driver, locator = locator)

    def create_account(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='create-account']")
        return MainElement(driver=self.driver, locator = locator)


class ValidSignin(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://automationexercise.com/')

    def signup_login(self):
        locator = (By.XPATH, "//ul[@class='nav navbar-nav']//a[@href='/login']")
        return MainElement(driver=self.driver, locator=locator)

    def enter_validemail(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
        return MainElement(driver=self.driver, locator=locator)

    def enter_validpassword(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
        return MainElement(driver=self.driver, locator=locator)

    def login_button(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='login-button']")
        return MainElement(driver=self.driver, locator=locator)

    def delete_account(self):
        locator = (By.XPATH, "//div[@class='shop-menu pull-right']//a[@href='/delete_account']")
        return MainElement(driver=self.driver, locator=locator)


class InvalidSignin (object):
    def __init__(self, driver):
        self.driver = driver

    def signup_login(self):
        locator = (By.XPATH, "//ul[@class='nav navbar-nav']//a[@href='/login']")
        return MainElement(driver=self.driver, locator=locator)

    def enter_invalidemail(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
        return MainElement(driver=self.driver, locator=locator)

    def enter_invalidpassword(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
        return MainElement(driver=self.driver, locator=locator)

    def login_button(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='login-button']")
        return MainElement(driver=self.driver, locator=locator)

class AddToCart (object):
    def __init__(self, driver):
        self.driver = driver

    def Productslink(self):
        locator = (By.XPATH,"//div[@class='shop-menu pull-right']//a[@href='/products']")
        return MainElement(driver=self.driver, locator=locator)

    def Product1(self):
        locator = (By.XPATH, "//div[@class='col-sm-4']//img[@src='/get_product_picture/1']")
        return MainElement(driver=self.driver, locator=locator)

    def Product1_AddToCart(self):
        locator = (By.XPATH, "//div[@class='overlay-content']//a[@data-product-id='1']")
        return MainElement(driver=self.driver, locator=locator)

    def ContinueShoppingButton(self):
        locator = (By.CSS_SELECTOR, "button[class='btn btn-success close-modal btn-block']")
        return MainElement(driver=self.driver, locator=locator)

    def ViewProduct_2(self):
        locator = (By.XPATH, "//div[@class='product-image-wrapper']//a[@ href='/product_details/2']")
        return MainElement(driver=self.driver, locator=locator)

    def ChangeQuantity(self):
        locator = (By.CSS_SELECTOR, "input[id='quantity']")
        return MainElement(driver=self.driver, locator=locator)

    def AddtoCart(self):
        locator = (By.CSS_SELECTOR, "button[class='btn btn-default cart']")
        return MainElement(driver=self.driver, locator=locator)

    def AddtoCartButton(self):
        locator = (By.CSS_SELECTOR, "button[class='btn btn-default cart']")
        return MainElement(driver=self.driver, locator=locator)

    def EnterName(self):
        locator = (By.ID, "name")
        return MainElement(driver=self.driver, locator=locator)

    def EnterEmail(self):
        locator = (By.ID, "email")
        return MainElement(driver=self.driver, locator=locator)

    def AddReview(self):
        locator = (By.ID, "review")
        return MainElement(driver=self.driver, locator=locator)

    def SubmitReview(self):
        locator = (By.ID, "button-review")
        return MainElement(driver=self.driver, locator=locator)

    def ViewCart(self):
        locator = (By.XPATH, "//div[@class='modal-content']//a")
        return MainElement(driver=self.driver, locator=locator)

    def DeleteItemfromCart(self):
        locator = (By.XPATH, "//td[@class='cart_delete']//a[@data-product-id='2']")
        return MainElement(driver=self.driver, locator=locator)

    def ProceedToCheckout(self):
        locator = (By.CSS_SELECTOR, "a[class='btn btn-default check_out']")
        return MainElement(driver=self.driver, locator=locator)

    def CheckoutRegister_Login(self):
        locator = (By.XPATH, "//p[@class='text-center']//a[@href='/login']")
        return MainElement(driver=self.driver, locator=locator)

    def enter_invalidemail(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-email']")
        return MainElement(driver=self.driver, locator=locator)

    def enter_invalidpassword(self):
        locator = (By.CSS_SELECTOR, "input[data-qa='login-password']")
        return MainElement(driver=self.driver, locator=locator)

    def login_button(self):
        locator = (By.CSS_SELECTOR, "button[data-qa='login-button']")
        return MainElement(driver=self.driver, locator=locator)