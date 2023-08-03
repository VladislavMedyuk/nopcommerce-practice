from pages.main_page import MainPage
from resources.env import Resources


class TestCartPage:
    def test_user_can_see_shopping_cart(self, browser):
        main_page = MainPage(browser, Resources.MAIN_LINK)
        main_page.open()
        main_page.should_be_shopping_cart()
