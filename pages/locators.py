from selenium.webdriver.common.by import By


class BasePageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, ".header span>a.btn-default.btn")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FORM_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class CartPageLocators(object):
    CART_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_CART_MESSAGE_ELEMENT = (By.CSS_SELECTOR, "#content_inner p")


class ProductPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_ALERT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
