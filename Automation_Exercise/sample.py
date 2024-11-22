import pytest
from selenium import webdriver
from Page_Locator import AddToCart
import logging

# Configure logging
logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get('https://automationexercise.com/')
    driver.maximize_window()
    logger.info('Opened Chrome browser and navigated to Automation Exercise')
    yield driver
    driver.quit()
    logger.info('Closed the Chrome browser')


def test_add_to_cart(browser):
    logger.info('Starting the add to cart test')

    run_test = AddToCart(browser)

    logger.info('Clicking Products Link')
    run_test.Productslink().click()
    browser.execute_script('window.scrollBy(0, 300)')

    # Assert that the product page is opened (check for a unique element)
    assert "Automation Exercise - All Products" in browser.title, "Test Failed: Products page not opened"
    logger.info('Verified that the products page is opened')

    """Add to Cart the first product"""
    logger.info('Hovering over the first product')
    ChooseProduct1 = run_test.Product1()
    ChooseProduct1.hover_to()

    logger.info('Clicking to add the first product to the cart')
    Product1_AddToCart = run_test.Product1_AddToCart()
    Product1_AddToCart.click()

    # Assert that the 'Continue Shopping' button appears after adding the product to the cart
    logger.info('Verifying the Continue Shopping button is displayed')
    ContinueShopping_button = run_test.ContinueShoppingButton()
    assert ContinueShopping_button.is_displayed(), "Test Failed: Continue Shopping button not displayed"
    logger.info('Continue Shopping button is displayed, clicking it')
    ContinueShopping_button.click()

    """View the 2nd product and change the Quantity"""
    logger.info('Viewing the second product')
    run_test.ViewProduct_2().click()

    logger.info('Hovering to change the quantity')
    ChangeQuantity = run_test.ChangeQuantity()
    ChangeQuantity.hover_to()
    browser.execute_script("arguments[0].stepUp();",
                           ChangeQuantity.web_element)  # Use JavaScript to change the quantity

    # Assert that the quantity was updated
    updated_quantity = ChangeQuantity.get_attribute('value')
    assert int(updated_quantity) == 2, "Test Failed: Quantity not updated"
    logger.info('Verified that the quantity was updated to %s', updated_quantity)

    """Write Review"""
    logger.info('Writing a review')
    run_test.EnterName().input('My name')
    run_test.EnterEmail().input('sample@gmail.com')
    run_test.AddReview().input('This is my Review\n'
                               'This is the 2nd line of Review\n'
                               '3rd line of Review')
    browser.execute_script('window.scrollBy(0, 800)')

    logger.info('Submitting the review')
    SubmitReview = run_test.SubmitReview()
    SubmitReview.click()

    # Assert that the review was submitted (check for success message)
    assert "Thank you for your review." in browser.page_source, "Test Failed: Review not submitted"
    logger.info('Review submitted successfully')

    """Add to Cart and view cart"""
    logger.info('Adding item to cart')
    AddToCartButton = run_test.AddtoCartButton()
    AddToCartButton.click()

    logger.info('Viewing the cart')
    ViewCartLink = run_test.ViewCart()
    ViewCartLink.click()

    # Assert that the cart page is opened
    assert "Automation Exercise - Checkout" in browser.title, "Test Failed: Cart page not opened"
    logger.info('Verified that the cart page is opened')

    """Delete an item from the cart and then checkout"""
    logger.info('Deleting an item from the cart')
    DeleteFromCart_button = run_test.DeleteItemfromCart()
    DeleteFromCart_button.click()

    """Proceed to Checkout"""
    logger.info('Proceeding to Checkout')
    ProceedToCheckout_button = run_test.ProceedToCheckout()
    ProceedToCheckout_button.click()

    logger.info('Going to Login/Registration page')
    CheckoutRegisterLogin_link = run_test.CheckoutRegister_Login()
    CheckoutRegisterLogin_link.click()

    # Assert that the checkout page opened
    assert "Automation Exercise - Signup / Login" in browser.title, "Test Failed: Checkout page not opened"
    logger.info('Verified that the checkout page is opened')

    """Login to the account using Invalid data"""
    logger.info('Entering email and password')
    run_test.enter_invalidemail().input('myemail@gmail.com')
    run_test.enter_invalidpassword().input('thisispassword')

    logger.info('Clicking the login button')
    login_button = run_test.login_button()
    login_button.click()

    # Assert that the login failed (check for error message)
    assert "Your email or password is incorrect!" in browser.page_source, "Test Failed: Invalid login message not displayed"
    logger.info('Login attempt made with invalid credentials')

