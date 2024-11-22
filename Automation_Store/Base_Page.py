class BasePage(object):
    url = None
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        """Navigate to the Training Ground page."""
        self.driver.get(self.url)
