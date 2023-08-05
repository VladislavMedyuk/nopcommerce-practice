from pages.main_page import MainPage
from pages.register_page import RegisterPage
from resources.env import Resources


class TestRegisterNewUser:
    def test_register_new_user(self, browser):
        main_page = MainPage(browser, Resources.MAIN_LINK)
        main_page.open()
        main_page.should_be_register_link()
        main_page.go_to_register_page()
        register_page = RegisterPage(browser, Resources.REGISTER_LINK)
        email, first_name, last_name, company, password = register_page.generate_random_user()
        register_page.register_new_user(email, first_name, last_name, company, password)
        register_page.should_be_success_registration()
