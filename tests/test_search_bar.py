import allure

from pages.main_page import MainPage
from pages.search_page import SearchPage
from resources.env import Resources


@allure.step("Тест: Поиск существующего товара")
def test_search_for_an_existing_product(browser):
    main_page = MainPage(browser, Resources.MAIN_LINK)
    main_page.open()
    main_page.should_be_search_bar()
    main_page.search_for_a_product(Resources.EXISTING_PRODUCT)
    search_page = SearchPage(browser, browser.current_url)
    search_page.should_be_search_results()
    search_page.result_should_contain_information_about_the_products()
    search_page.search_results_should_be_unique()


@allure.step("Тест: Поиск несуществующего товара")
def test_search_for_a_nonexistent_product(browser):
    main_page = MainPage(browser, Resources.MAIN_LINK)
    main_page.open()
    main_page.should_be_search_bar()
    main_page.search_for_a_product(Resources.NONEXISTENT_PRODUCT)
    search_page = SearchPage(browser, browser.current_url)
    search_page.should_be_message_about_the_absence_of_products()


@allure.step("Тест: Поиск с пустым запросом")
def test_search_with_an_empty_request(browser):
    main_page = MainPage(browser, Resources.MAIN_LINK)
    main_page.open()
    main_page.should_be_search_bar()
    main_page.search_for_a_product(Resources.EMPTY_REQUEST)
    main_page.should_be_a_popup_alert()
