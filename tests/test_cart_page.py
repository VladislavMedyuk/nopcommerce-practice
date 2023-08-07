import allure
import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage
from resources.env import Resources


class TestCartPage:
    @pytest.fixture(scope="session", autouse=True)
    def setup(self, browser):
        register_page = RegisterPage(browser, Resources.REGISTER_LINK)
        register_page.open()
        email, first_name, last_name, company, password = register_page.generate_random_user()
        register_page.register_new_user(email, first_name, last_name, company, password)
        register_page.should_be_success_registration()
        register_page.should_be_login_link()
        register_page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()
        login_page.login_new_user(email, password)

    @allure.step("Тест: С главной страницы добавляем товар в корзину, проверяем есть ли товар в корзине")
    def test_user_can_add_product_to_cart(self, browser):
        main_page = MainPage(browser, Resources.MAIN_LINK)
        main_page.open()
        main_page.should_be_product_name()
        main_page.go_to_product_page()

        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_product_name_and_add_to_cart_button()
        product_page.perform_actions_based_on_product()
        product_page.go_to_shopping_cart()

        cart_page = CartPage(browser, browser.current_url)
        cart_page.cart_shouldnt_be_empty()
        cart_page.should_be_total_price()
        cart_page.counter_should_be_equal_to_quantity()

    def test_checking_the_cost_and_total_sum_of_the_order(self, browser):
        cart_page = CartPage(browser, Resources.CART_LINK)
        cart_page.open()
        cart_page.should_be_product_price()
        cart_page.should_be_total_price()
        cart_page.product_price_should_be_equal_to_total_price()

    def test_user_can_delete_product_from_cart(self, browser):
        cart_page = CartPage(browser, Resources.CART_LINK)
        cart_page.open()
        cart_page.cart_shouldnt_be_empty()
        cart_page.delete_product_from_cart()
        cart_page.cart_should_be_empty()
        cart_page.counter_should_be_equal_to_zero()


@allure.step("Тест: На главной странице должна быть кнопка добавить в корзину")
def test_user_can_see_shopping_cart(browser):
    main_page = MainPage(browser, Resources.MAIN_LINK)
    main_page.open()
    main_page.should_be_shopping_cart()


@allure.step("Тест: Переходим в корзину с главной страницы, корзина должна быть пуста")
def test_user_can_go_to_shopping_cart(browser):
    main_page = MainPage(browser, Resources.MAIN_LINK)
    main_page.open()
    main_page.go_to_shopping_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
