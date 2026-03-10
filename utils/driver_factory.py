import chromedriver_binary
from selenium import webdriver
from utils.config import Config


class DriverFactory:
    @staticmethod
    def get_driver(browser=None, headless=None):
        browser = browser or Config.BROWSER
        headless = headless if headless is not None else Config.HEADLESS

        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-extensions")
            options.add_experimental_option(
                "excludeSwitches", ["enable-logging"]
            )
            driver = webdriver.Chrome(options=options)
        else:
            raise ValueError(f"Navigateur non supporte: {browser}")

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver