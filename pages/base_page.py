import allure
from faker import Faker
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from resources.env import Resources


class BasePage:
    def __init__(self, browser: webdriver, url: str) -> None:
        self.__browser = browser
        self.__url = url

    @property
    def browser(self) -> webdriver:
        return self.__browser

    @browser.setter
    def browser(self, browser: webdriver) -> None:
        self.__browser = browser

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str) -> None:
        self.__url = url

    @allure.step("Открываем страницу")
    def open(self) -> None:
        self.browser.get(self.url)

    @allure.step("Находим элемент по локатору")
    def find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.browser, Resources.TIMEOUT).until(EC.visibility_of_element_located(locator))

    @allure.step("Вводим текст в элемент")
    def send_keys(self, locator: tuple, text: str) -> None:
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step("Находим все элементы по локатору")
    def find_elements(self, locator: tuple) -> list:
        try:
            elements = WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements
        except NoSuchElementException:
            return []

    @allure.step("Проверяем, что элементы присутствуют на странице")
    def elements_are_present(self, locator: tuple) -> bool:
        elements = self.find_elements(locator)
        return len(elements) > 0

    @allure.step("Проверяем, что элемент присутствует на странице")
    def element_is_present(self, locator: tuple) -> bool:
        try:
            return WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except NoSuchElementException:
            return False

    @allure.step("Проверяем, что элемент отсутствует на странице")
    def element_is_not_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    @staticmethod
    def generate_random_data() -> dict:
        fake = Faker()
        data = {"RecipientName": fake.name(),
                "RecipientEmail": fake.email(),
                "SenderName": fake.name(),
                "SenderEmail": fake.email()}
        return data
