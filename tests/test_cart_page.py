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
