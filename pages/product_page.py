import random

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import ProductPageLocators
from pages.base_page import BasePage
from resources.env import Resources


class ProductPage(BasePage):

    def add_to_cart(self) -> None:
        add_button = self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    def get_product_name(self) -> str:
        product_name = self.find_element(ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def go_to_shopping_cart(self) -> None:
        shopping_cart = self.find_element(ProductPageLocators.SHOPPING_CART)
        shopping_cart.click()

    def should_be_product_name_and_add_to_cart_button(self) -> None:
        assert self.element_is_present(
            ProductPageLocators.PRODUCT_NAME), "There is not product name on the page"
        assert self.element_is_present(
            ProductPageLocators.ADD_TO_CART_BUTTON), "There is not add to cart button on the page"

    def should_be_success_message(self) -> None:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(ProductPageLocators.POP_UP_MESSAGE)
            )
        except TimeoutException:
            raise AssertionError("Success message is not displayed")

    def success_message_is_disappeared(self) -> None:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until_not(
                EC.presence_of_element_located(ProductPageLocators.POP_UP_MESSAGE)
            )
        except TimeoutException:
            raise AssertionError("Success message is still displayed")

    def click_add_to_cart_without_action(self) -> None:
        self.add_to_cart()
        assert self.element_is_present(
            ProductPageLocators.ERROR_MESSAGE), "A error message should have appeared, but it didn't"

    def fill_gift_form_and_add_to_cart(self) -> None:
        data = self.generate_random_data()

        self.send_keys(ProductPageLocators.RECIPIENT_NAME_FIELD, data["RecipientName"])
        self.send_keys(ProductPageLocators.RECIPIENT_EMAIL_FIELD, data["RecipientEmail"])
        self.send_keys(ProductPageLocators.SENDER_NAME_FIELD, data["SenderName"])
        self.send_keys(ProductPageLocators.SENDER_EMAIL_FIELD, data["SenderEmail"])

        self.add_to_cart()
        assert self.element_is_not_present(
            ProductPageLocators.ERROR_MESSAGE), "An error message is present, but it shouldn't"

    def click_radio_buttons(self) -> None:
        radio_buttons = self.find_elements(ProductPageLocators.RADIO_BUTTONS)
        for radio in radio_buttons:
            rand_click = random.choice([True, False])
            if rand_click:
                radio.click()

    def click_checkboxes(self):
        checkboxes = self.find_elements(ProductPageLocators.CHECKBOXES)
        for check in checkboxes:
            rand_click = random.choice([True, False])
            if rand_click:
                check.click()

    def select_random_option(self, select_list):
        def select_random_option_in_list(locator):
            selects = self.find_elements(locator)
            for select in selects:
                dropdown = Select(select)
                options = dropdown.options
                random_index = random.randint(1, len(options) - 1)
                option_text = options[random_index].text
                dropdown.select_by_visible_text(option_text)

        for select_locator in select_list:
            select_random_option_in_list(select_locator)
