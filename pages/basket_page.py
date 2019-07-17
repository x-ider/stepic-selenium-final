from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty, but it's not"

    def basket_is_empty_text_exists(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE_ELEMENT).text
        assert text == "Your basket is empty. Continue shopping"
