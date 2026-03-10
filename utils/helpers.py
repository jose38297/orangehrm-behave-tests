import time
import os
import random
import string
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.config import Config


class Helpers:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.timeout = Config.EXPLICIT_WAIT

    def wait_for_element(self, locator, timeout=None):
        t = timeout or Config.EXPLICIT_WAIT
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=None):
        t = timeout or Config.EXPLICIT_WAIT
        return WebDriverWait(self.driver, t).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_visible(self, locator, timeout=None):
        t = timeout or Config.EXPLICIT_WAIT
        return WebDriverWait(self.driver, t).until(
            EC.visibility_of_element_located(locator)
        )

    def safe_click(self, locator, timeout=None):
        element = self.wait_for_clickable(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)
        element.click()
        return element

    def safe_type(self, locator, text, clear=True):
        element = self.wait_for_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        return self.wait_for_visible(locator).text.strip()

    def take_screenshot(self, name=None):
        os.makedirs("reports/screenshots", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reports/screenshots/{name or 'screenshot'}_{ts}.png"
        self.driver.save_screenshot(filename)
        return filename

    def wait_for_page_load(self, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_for_spinner_disappear(self, timeout=30):
        try:
            spinner = (By.CSS_SELECTOR, ".oxd-loading-spinner")
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(spinner)
            )
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(spinner)
            )
        except TimeoutException:
            pass

    @staticmethod
    def generate_random_name(prefix="Test"):
        suffix = ''.join(random.choices(string.ascii_uppercase, k=5))
        return f"{prefix}{suffix}"

    @staticmethod
    def generate_random_string(length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
