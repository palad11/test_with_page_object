from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    def should_be_cart_empty(self):
        assert self.browser.find_element(By.CSS_SELECTOR,
                                         '#content_inner > p'), "Cart is not empty"

    def should_be_text_about_empty(self):
        assert len(self.browser.find_element(By.CSS_SELECTOR,
                                             '#content_inner > p').text) != 0, 'Text is empty'
