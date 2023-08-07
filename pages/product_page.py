import random

import allure
from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import ProductPageLocators
from pages.base_page import BasePage
from resources.env import Resources


class ProductPage(BasePage):
    @staticmethod
    def generate_random_data() -> dict:
        fake = Faker()
        data = {"RecipientName": fake.name(),
                "RecipientEmail": fake.email()}
        return data

    @allure.step("Добавляем продукт в корзину")
    def add_to_cart(self) -> None:
        add_button = self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()

    @allure.step("Получаем название продукта")
    def get_product_name(self) -> str:
        product_name = self.find_element(ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    @allure.step("Переходим в корзину")
    def go_to_shopping_cart(self) -> None:
        shopping_cart = self.find_element(ProductPageLocators.SHOPPING_CART)
        shopping_cart.click()

    @allure.step("Проверяем, что отображается название продукта и кнопка 'Добавить в корзину'")
    def should_be_product_name_and_add_to_cart_button(self) -> None:
        assert self.element_is_present(
            ProductPageLocators.PRODUCT_NAME), "There is not product name on the page"
        assert self.element_is_present(
            ProductPageLocators.ADD_TO_CART_BUTTON), "There is not add to cart button on the page"

    @allure.step("Проверяем, что отображается сообщение об успешном добавлении в корзину")
    def should_be_success_message(self) -> None:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(ProductPageLocators.POP_UP_MESSAGE)
            )
        except TimeoutException:
            raise AssertionError("Success message is not displayed")

    @allure.step("Проверяем, что сообщение об успешном добавлении в корзину исчезает")
    def success_message_is_disappeared(self) -> None:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until_not(
                EC.presence_of_element_located(ProductPageLocators.POP_UP_MESSAGE)
            )
        except TimeoutException:
            raise AssertionError("Success message is still displayed")

    @allure.step("Кликаем на кнопку 'Добавить в корзину' без выполнения других действий")
    def click_add_to_cart_without_action(self) -> None:
        self.add_to_cart()
        assert self.element_is_present(
            ProductPageLocators.ERROR_MESSAGE), "A error message should have appeared, but it didn't"

    @allure.step("Заполняем форму для подарочной карты и добавляем в корзину")
    def fill_gift_form_and_add_to_cart(self) -> None:
        data = self.generate_random_data()

        self.send_keys(ProductPageLocators.RECIPIENT_NAME_FIELD, data["RecipientName"])
        self.send_keys(ProductPageLocators.RECIPIENT_EMAIL_FIELD, data["RecipientEmail"])

        self.add_to_cart()
        assert self.element_is_not_present(
            ProductPageLocators.ERROR_MESSAGE), "An error message is present, but it shouldn't"

    @allure.step("Кликаем на случайные радиокнопки")
    def click_radio_buttons(self) -> None:
        radio_buttons = self.find_elements(ProductPageLocators.RADIO_BUTTONS)
        for radio in radio_buttons:
            rand_click = random.choice([True, False])
            if rand_click:
                radio.click()

    @allure.step("Кликаем на случайные чекбоксы")
    def click_checkboxes(self) -> None:
        checkboxes = self.find_elements(ProductPageLocators.CHECKBOXES)
        for check in checkboxes:
            rand_click = random.choice([True, False])
            if rand_click:
                check.click()

    @allure.step("Выбираем случайные значения в выпадающих списках")
    def select_random_option(self, select_list) -> None:
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

    @allure.step("Выполняем действия для продукта 'Компьютер'")
    def action_for_pc(self) -> None:
        self.click_add_to_cart_without_action()
        self.browser.refresh()
        self.select_random_option(ProductPageLocators.SELECT_LIST)
        self.click_radio_buttons()
        self.click_checkboxes()
        self.add_to_cart()
        self.should_be_success_message()
        self.success_message_is_disappeared()

    @allure.step("Выполняем действия для продукта 'Ноутбук'")
    def action_for_macbook(self) -> None:
        self.add_to_cart()
        self.should_be_success_message()
        self.success_message_is_disappeared()

    @allure.step("Выполняем действия для продукта 'Телефон'")
    def action_for_phone(self) -> None:
        self.add_to_cart()
        self.should_be_success_message()
        self.success_message_is_disappeared()

    @allure.step("Выполняем действия для продукта 'Подарочная карта'")
    def action_for_gift(self) -> None:
        self.click_add_to_cart_without_action()
        self.browser.refresh()
        self.fill_gift_form_and_add_to_cart()
        self.should_be_success_message()
        self.success_message_is_disappeared()

    @allure.step("Выполняем действия в зависимости от продукта")
    def perform_actions_based_on_product(self) -> None:
        product_name = self.get_product_name()
        if product_name == Resources.PC_PAGE_NAME:
            self.action_for_pc()
        elif product_name == Resources.MACBOOK_PAGE_NAME:
            self.action_for_macbook()
        elif product_name == Resources.GIFT_PAGE_NAME:
            self.action_for_gift()
        elif product_name == Resources.PHONE_PAGE_NAME:
            self.action_for_phone()
        else:
            print(f"Unknown product: {product_name}")
