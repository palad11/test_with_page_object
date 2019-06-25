import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.CART)
        cart.click()

    def should_be_item_added(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME).text == self.browser.find_element(
            *ProductPageLocators.SHOW_ITEM_NAME).text, "Name is not the same"

    def should_be_same_price(self):
        assert self.browser.find_element(*ProductPageLocators.IN_CART_PRICE).text == self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE).text, "Price is not the same"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_hide(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"
