from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base_page import BasePage


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
            self.browser.find_element(By.CSS_SELECTOR, "#login_form")
            self.browser.find_element(By.CSS_SELECTOR, ".form-control#id_login-username")
            self.browser.find_element(By.CSS_SELECTOR, ".form-control#id_login-password")
            self.browser.find_element(By.CSS_SELECTOR, "#login_form > p > a")
            self.browser.find_element(By.CSS_SELECTOR, "#login_form > button")

        except NoSuchElementException:
            assert False, 'Login form error.'
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#register_form")
            self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
            self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
            self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
            self.browser.find_element(By.CSS_SELECTOR, "#register_form > button")

        except NoSuchElementException:
            assert False, 'Register form error.'
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email").send_keys(email)
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2").send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, "#register_form > button").click()