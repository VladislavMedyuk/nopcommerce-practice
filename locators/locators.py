import random

from selenium.webdriver.common.by import By


class CartPageLocators:
    MESSAGE_EMPTY = (By.CLASS_NAME, "no-data")
    TOTAL_CASH = (By.CSS_SELECTOR, "span.value-summary strong")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "button-1 checkout-button")
    CART_ITEMS = (By.CSS_SELECTOR, ".table-wrapper tbody tr")
    QUANTITY = (By.XPATH, "//*[@class='qty-input']")
    COUNTER = (By.CSS_SELECTOR, "span.cart-qty")
    DELETE_BUTTON = (By.CLASS_NAME, "remove-btn")
    PRICE = (By.CLASS_NAME, "product-unit-price")


class MainPageLocators:
    SHOPPING_CART = (By.CLASS_NAME, "cart-label")
    SEARCH_BAR = (By.NAME, "q")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='bar-notification'] //p")
    PRODUCT_NAME = (By.CSS_SELECTOR, f".item-box:nth-child({random.randint(1, 4)}) .details a")
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")
    MY_ACCOUNT_LINK = (By.CLASS_NAME, "ico-account")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-box-button")


class ProductPageLocators:
    REQUIRED_FIELDS = ".giftcard span.required"
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-name']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart-panel .button-1")
    POP_UP_MESSAGE = (By.XPATH, "//*[@id='bar-notification'] //p")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#bar-notification .bar-notification")
    SHOPPING_CART = (By.CLASS_NAME, "cart-label")

    RECIPIENT_NAME_FIELD = (By.CLASS_NAME, "recipient-name")
    RECIPIENT_EMAIL_FIELD = (By.CLASS_NAME, "recipient-email")
    SENDER_NAME_FIELD = (By.CLASS_NAME, "sender-name")
    SENDER_EMAIL_FIELD = (By.CLASS_NAME, "sender-email")

    RADIO_BUTTONS = (By.XPATH, "//input[@type='radio']")
    CHECKBOXES = (By.XPATH, "//ul[@class='option-list']//input[@type='checkbox']")
    SELECT_LIST = [(By.XPATH, "//*[@id='product_attribute_1']"), (By.XPATH, "//*[@id='product_attribute_2']")]


class RegisterPageLocators:
    REGISTER_BUTTON = (By.ID, "register-button")
    GENDER = (By.CSS_SELECTOR, f"#gender span:nth-of-type({random.randint(1, 2)}) input")
    FIRST_NAME = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME = (By.CSS_SELECTOR, "#LastName")
    EMAIL = (By.CSS_SELECTOR, "#Email")
    COMPANY = (By.CSS_SELECTOR, "#Company")
    NEWSLETTER = (By.CSS_SELECTOR, ".inputs #Newsletter")
    PASSWORD = (By.CSS_SELECTOR, "[type = 'Password']")
    SUCCESS_REGISTRATION = (By.CSS_SELECTOR, ".page-body .result")
    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".field-validation-error span")


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "returning-wrapper")
    EMAIL_BAR = (By.CSS_SELECTOR, ".email")
    PASSWORD_BAR = (By.CSS_SELECTOR, ".password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")


class SearchPageLocators:
    PRODUCT_ITEMS = (By.CLASS_NAME, "product-item")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "img[title]")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-title a")
    PRODUCT_PRICE = (By.CLASS_NAME, "actual-price")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".products-wrapper .picture")
    ERROR_MESSAGE = (By.CLASS_NAME, "no-result")
