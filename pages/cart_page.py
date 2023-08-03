import allure

from locators.locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    @allure.step("Проверяем, что корзина пуста")
    def cart_should_be_empty(self) -> None:
        assert self.element_is_present(CartPageLocators.MESSAGE_EMPTY), "Cart isn't empty"

    @allure.step("Проверяем, что корзина не пуста")
    def cart_shouldnt_be_empty(self) -> None:
        cart_items = self.find_elements(CartPageLocators.CART_ITEMS)
        assert len(cart_items) > 0, "Cart is empty"

    @allure.step("Проверяем, что счетчик равен количеству товаров в корзине")
    def counter_should_be_equal_to_quantity(self) -> None:
        quantity = self.find_element(CartPageLocators.QUANTITY)
        counter = self.find_element(CartPageLocators.COUNTER)
        assert quantity.get_attribute("value") == counter.text.strip(
            "()"), "Counter isn't equal to number of quantity"

    @allure.step("Проверяем, что отображается общая стоимость")
    def should_be_total_price(self) -> None:
        assert self.element_is_present(CartPageLocators.TOTAL_CASH), "There is not total price on the page"
