from selenium.webdriver.common.by import By
from .locators import CartPageLocators
from .base_page import BasePage


class CartPage(BasePage):
    def should_be_cart_empty(self):
        assert self.browser.find_element(*CartPageLocators.CART_EMPTY_TEXT), "Cart is not empty"

    def should_be_text_about_empty(self):
        assert len(self.browser.find_element(*CartPageLocators.CART_EMPTY_TEXT).text) != 0, 'Text is empty'
