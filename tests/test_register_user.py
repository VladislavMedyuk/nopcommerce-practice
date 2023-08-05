from pages.register_page import RegisterPage
from resources.env import Resources


class TestRegisterNewUser:
    def test_register_new_user(self, browser):
        register_page = RegisterPage(browser, Resources.REGISTER_LINK)
        register_page.open()
        email, first_name, last_name, company, password = register_page.generate_random_user()
        register_page.register_new_user(email, first_name, last_name, company, password)
        register_page.should_be_success_registration()
