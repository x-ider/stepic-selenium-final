from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Cart should be empty, but it's not"

    def cart_is_empty_text_exists(self):
        text = self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE_ELEMENT).text
        assert text == "Your basket is empty. Continue shopping"
