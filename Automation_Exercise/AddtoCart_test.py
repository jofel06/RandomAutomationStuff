import pytest
from selenium import webdriver
from Page_Locator import AddToCart

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get('https://automationexercise.com/')
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_to_cart(browser):
    #Start the Test by opening the browser
    run_test = AddToCart(browser)
    run_test.Productslink().click()
    browser.execute_script('window.scrollBy(0, 300)')

    #Assert that the product page is opened (check for a unique element)
    assert "Automation Exercise - All Products" in browser.title, "Test Failed: Products page not opened"

    """Add to Cart the first product"""
    ChooseProduct1 = run_test.Product1()
    ChooseProduct1.hover_to()
    Product1_AddToCart = run_test.Product1_AddToCart()
    Product1_AddToCart.click()

    #Assert that the 'Continue Shopping' button appears after adding the product to the cart
    ContinueShopping_button = run_test.ContinueShoppingButton()
    assert ContinueShopping_button.is_displayed(), "Test Failed: Continue Shopping button not displayed"
    ContinueShopping_button.click()


    """View the 2nd product and change the Quantity"""
    run_test.ViewProduct_2().click()
    ChangeQuantity = run_test.ChangeQuantity()
    ChangeQuantity.hover_to()
    browser.execute_script("arguments[0].stepUp();", ChangeQuantity.web_element) # Use JavaScript to change the quantity (step up to increase is, down to decrease)

    # Assert that the quantity was updated
    updated_quantity = ChangeQuantity.get_attribute('value')
    assert int(updated_quantity) == 2, "Test Failed: Quantity not updated"


    """Write Review"""
    run_test.EnterName().input('My name')
    run_test.EnterEmail().input('sample@gmail.com')
    run_test.AddReview().input('This is my Review\n'
                               'This is the 2nd line of Review\n'
                               '3rd line of Review')
    browser.execute_script('window.scrollBy(0, 800)')
    SubmitReview = run_test.SubmitReview()
    SubmitReview.click()

    # Assert that the review was submitted (check for success message)
    assert "Thank you for your review." in browser.page_source, "Test Failed: Review not submitted"


    """Add to Cart and view cart"""
    AddToCartButton = run_test.AddtoCartButton()
    AddToCartButton.click()
    ViewCartLink = run_test.ViewCart()
    ViewCartLink.click()

    # Assert that the cart page is opened
    assert "Automation Exercise - Checkout" in browser.title, "Test Failed: Cart page not opened"


    """Delete an item from the cart and then checkout"""
    DeleteFromCart_button = run_test.DeleteItemfromCart()
    DeleteFromCart_button.click()

    """Proceed to Checkout"""
    ProceedToCheckout_button = run_test.ProceedToCheckout()
    ProceedToCheckout_button.click()
    CheckoutRegisterLogin_link = run_test.CheckoutRegister_Login()
    CheckoutRegisterLogin_link.click()
    # Assert that the checkout page opened
    assert "Automation Exercise - Signup / Login" in browser.title, "Test Failed: Checkout page not opened"

    """Login to the account using Invalid data"""
    run_test.enter_invalidemail().input('myemail@gmail.com')
    run_test.enter_invalidpassword().input('thisispassword')
    login_button = run_test.login_button()
    login_button.click()

    # Assert that the login failed (check for error message)
    assert "Your email or password is incorrect!" in browser.page_source, "Test Failed: Invalid login message not displayed"



