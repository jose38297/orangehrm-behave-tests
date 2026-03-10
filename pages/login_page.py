from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE  = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def open(self):
        self.navigate_to(Config.LOGIN_URL)
        return self

    def enter_username(self, username):
        self.helper.safe_type(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password):
        self.helper.safe_type(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        self.helper.safe_click(self.LOGIN_BUTTON)
        self.wait_loading()
        return self

    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def login_as_admin(self):
        return self.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)

    def login_as_employee(self):
        return self.login(Config.EMPLOYEE_USERNAME, Config.EMPLOYEE_PASSWORD)

    def login_as_manager(self):
        return self.login(Config.MANAGER_USERNAME, Config.MANAGER_PASSWORD)

    def get_error_message(self):
        return self.helper.get_text(self.ERROR_MESSAGE)

    def is_login_page(self):
        return self.helper.is_element_present(self.LOGIN_BUTTON)
