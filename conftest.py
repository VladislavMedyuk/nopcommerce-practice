import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
