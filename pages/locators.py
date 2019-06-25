from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM_WHOLLY = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    LOGIN_FORM_WHOLLY = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, ".form-control#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, ".form-control#id_login-password")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    LOGIN_FORM_PASSWORD_RESET = (By.CSS_SELECTOR, "#login_form > p > a")


class ProductPageLocators(object):
    CART = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    ITEM_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    SHOW_ITEM_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    IN_CART_PRICE = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):
    CART_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')