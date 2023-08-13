from locators.locators import SearchPageLocators
from pages.base_page import BasePage


class SearchPage(BasePage):
    def should_be_search_results(self):
        assert self.elements_are_present(
            SearchPageLocators.PRODUCT_ITEMS), "The search results are not displayed, but they should"

    def result_should_contain_information_about_the_products(self):
        assert self.element_is_present(
            SearchPageLocators.PRODUCT_TITLE), "Product information is not displayed, but it should be on the page"

    def products_should_have_name_price_and_image(self):
        results = self.find_elements(SearchPageLocators.PRODUCT_ITEMS)
        for result in results:
            assert result.find_element(SearchPageLocators.PRODUCT_IMAGE), "1"
            assert result.find_element(SearchPageLocators.PRODUCT_NAME), "2"
            assert result.find_element(SearchPageLocators.PRODUCT_PRICE), "3"

    def search_results_should_be_unique(self):
        product_elements = self.find_elements(SearchPageLocators.PRODUCT_NAME)
        names = []
        for product in product_elements:
            names.append(product.text)
        assert len(names) == len(set(names)), "The product name is repeated, but it should not"

    def should_be_message_about_the_absence_of_products(self):
        assert self.element_is_present(
            SearchPageLocators.ERROR_MESSAGE), "There are some product on the search page, but they shouldn't"
