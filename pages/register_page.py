from faker import Faker

from locators.locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    @staticmethod
    def generate_random_user() -> tuple:
        faker = Faker()
        email = faker.email()
        first_name = faker.first_name()
        last_name = faker.last_name()
        password = faker.password()
        company = faker.company()
        return email, first_name, last_name, company, password

    def register_new_user(self, email, first_name, last_name, company, password):
        gender = self.find_element(RegisterPageLocators.GENDER)
        gender.click()
        first_name_bar = self.find_element(RegisterPageLocators.FIRST_NAME)
        first_name_bar.send_keys(first_name)
        last_name_bar = self.find_element(RegisterPageLocators.LAST_NAME)
        last_name_bar.send_keys(last_name)
        email_bar = self.find_element(RegisterPageLocators.EMAIL)
        email_bar.send_keys(email)
        company_bar = self.find_element(RegisterPageLocators.COMPANY)
        company_bar.send_keys(company)
        passwords = self.find_elements(RegisterPageLocators.PASSWORD)
        for parole in passwords:
            parole.send_keys(password)
        register_button = self.find_element(RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_success_registration(self):
        assert self.element_is_present(
            RegisterPageLocators.SUCCESS_REGISTRATION), "There should be a message about successful registration, but this does not happen "
