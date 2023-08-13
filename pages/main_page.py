import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import MainPageLocators
from pages.base_page import BasePage
from resources.env import Resources


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

    def should_be_search_bar(self) -> None:
        assert self.element_is_present(MainPageLocators.SEARCH_BAR), ""

    def search_for_a_product(self, name) -> None:
        search_bar = self.find_element(MainPageLocators.SEARCH_BAR)
        search_bar.send_keys(name)

        search_button = self.find_element(MainPageLocators.SEARCH_BUTTON)
        search_button.click()

    def should_be_a_popup_alert(self):
        alert = WebDriverWait(self.browser, Resources.TIMEOUT).until(EC.alert_is_present())
        alert_text = alert.text
        assert alert_text in Resources.ALERT_TEXT, "This is not the expected text in the response"
