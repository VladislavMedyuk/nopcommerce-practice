import allure

from locators.locators import SearchPageLocators
from pages.base_page import BasePage


class SearchPage(BasePage):
    @allure.step("Проверяем есть ли результаты поиска на странице")
    def should_be_search_results(self) -> None:
        assert self.elements_are_present(
            SearchPageLocators.PRODUCT_ITEMS), "The search results are not displayed, but they should"

    @allure.step("Проверяем что результаты поиска содержат информацию о продукте")
    def result_should_contain_information_about_the_products(self) -> None:
        assert self.element_is_present(
            SearchPageLocators.PRODUCT_TITLE), "Product information is not displayed, but it should be on the page"

    @allure.step("Проверяем, что все результаты поиска уникальны")
    def search_results_should_be_unique(self) -> None:
        product_elements = self.find_elements(SearchPageLocators.PRODUCT_NAME)
        names = []
        for product in product_elements:
            names.append(product.text)
        assert len(names) == len(set(names)), "The product name is repeated, but it should not"

    @allure.step("Проверяем результат поиска на предмет отсутствия товаров")
    def should_be_message_about_the_absence_of_products(self) -> None:
        assert self.element_is_present(
            SearchPageLocators.ERROR_MESSAGE), "There are some product on the search page, but they shouldn't"
