from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_form(self) -> None:
        assert self.element_is_present(
            LoginPageLocators.LOGIN_FORM), "There is not login form om this page, but it should be"

    def login_new_user(self, email, password) -> None:
        email_bar = self.find_element(LoginPageLocators.EMAIL_BAR)
        email_bar.send_keys(email)
        password_bar = self.find_element(LoginPageLocators.PASSWORD_BAR)
        password_bar.send_keys(password)
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
