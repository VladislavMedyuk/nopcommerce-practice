from pages.main_page import MainPage
from pages.search_page import SearchPage
from resources.env import Resources


def test_search_for_an_existing_product(browser):
    main_page = MainPage(browser, Resources.MAIN_LINK)
    main_page.open()
    main_page.should_be_search_bar()
    main_page.search_for_a_product(Resources.EXISTING_PRODUCT)
    search_page = SearchPage(browser, browser.current_url)
    search_page.should_be_search_results()
    search_page.result_should_contain_information_about_the_products()
    search_page.products_should_have_name_price_and_image()
