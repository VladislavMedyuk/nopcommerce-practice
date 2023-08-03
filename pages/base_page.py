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

    def open(self) -> None:
        self.browser.get(self.url)

    def find_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.browser, Resources.TIMEOUT).until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator: tuple, text: str) -> None:
        element = self.find_element(locator)
        element.send_keys(text)

    def find_elements(self, locator: tuple) -> list:
        try:
            elements = WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements
        except NoSuchElementException:
            return []

    def elements_are_present(self, locator: tuple) -> bool:
        elements = self.find_elements(locator)
        return len(elements) > 0

    def element_is_present(self, locator: tuple) -> bool:
        try:
            return WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except NoSuchElementException:
            return False

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
