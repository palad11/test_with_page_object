from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
