import allure

from locators.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Проверяем, что отображается кнопка 'Корзина'")
    def should_be_shopping_cart(self) -> None:
        assert self.element_is_present(MainPageLocators.SHOPPING_CART), "Shopping cart is not present"

    @allure.step("Переходим в корзину")
    def go_to_shopping_cart(self) -> None:
        shopping_cart = self.find_element(MainPageLocators.SHOPPING_CART)
        shopping_cart.click()

    @allure.step("Проверяем, что отображается название продукта")
    def should_be_product_name(self) -> None:
        assert self.element_is_present(MainPageLocators.PRODUCT_NAME), "Product name is not present"

    @allure.step("Переходим на страницу продукта")
    def go_to_product_page(self) -> None:
        product_name = self.find_element(MainPageLocators.PRODUCT_NAME)
        product_name.click()

    @allure.step("Проверяем есть ли ссылка на страницу регистрации")
    def should_be_register_link(self) -> None:
        assert self.element_is_present(MainPageLocators.REGISTER_LINK), "Register link is not present"

    @allure.step("Переходим на страницу регистрации пользователя")
    def go_to_register_page(self) -> None:
        register_link = self.find_element(MainPageLocators.REGISTER_LINK)
        register_link.click()

    @allure.step("Проверяем, что пользователь успешно зарегистрирован")
    def should_be_authorized_user(self) -> None:
        assert self.element_is_present(MainPageLocators.MY_ACCOUNT_LINK), "User is not authorized, but he should be"
