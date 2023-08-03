from locators.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def should_be_shopping_cart(self) -> None:
        assert self.element_is_present(MainPageLocators.SHOPPING_CART), "Shopping cart is not present"

    def go_to_shopping_cart(self) -> None:
        shopping_cart = self.find_element(MainPageLocators.SHOPPING_CART)
        shopping_cart.click()

    def should_be_product_name(self) -> None:
        assert self.element_is_present(MainPageLocators.PRODUCT_NAME)

    def go_to_product_page(self) -> None:
        product_name = self.find_element(MainPageLocators.PRODUCT_NAME)
        product_name.click()
