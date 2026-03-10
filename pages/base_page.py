from selenium.webdriver.common.by import By
from utils.helpers import Helpers
from utils.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = Helpers(driver)

    TOAST_SUCCESS = (By.CSS_SELECTOR, ".oxd-toast--success")
    TOAST_ERROR   = (By.CSS_SELECTOR, ".oxd-toast--error")
    SPINNER       = (By.CSS_SELECTOR, ".oxd-loading-spinner")

    def get_success_toast(self):
        return self.helper.get_text(self.TOAST_SUCCESS)

    def get_error_toast(self):
        return self.helper.get_text(self.TOAST_ERROR)

    def wait_loading(self):
        self.helper.wait_for_spinner_disappear()
        self.helper.wait_for_page_load()

    def navigate_to(self, url):
        self.driver.get(url)
        self.wait_loading()
