from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login'), 'Current url error'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM_WHOLLY)
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM_USERNAME)
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD)
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD_RESET)
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BUTTON)

        except NoSuchElementException:
            assert False, 'Login form error.'
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_WHOLLY)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)

        except NoSuchElementException:
            assert False, 'Register form error.'
        assert True

    def register_new_user(self, email, password):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON).click()
        except NoSuchElementException:
            assert False, 'Register new user error.'
        assert True
