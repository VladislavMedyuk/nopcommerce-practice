
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from resources.env import Resources


class TestCartPage:
    def test_user_can_see_shopping_cart(self, browser):
        main_page = MainPage(browser, Resources.MAIN_LINK)
        main_page.open()
        main_page.should_be_shopping_cart()

    def test_user_can_go_to_shopping_cart(self, browser):
        main_page = MainPage(browser, Resources.MAIN_LINK)
        main_page.open()
        main_page.go_to_shopping_cart()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.cart_should_be_empty()

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
