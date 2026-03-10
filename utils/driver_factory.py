import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
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
            options.add_argument("--remote-debugging-port=9222")
            options.add_experimental_option(
                "excludeSwitches", ["enable-logging"]
            )

            chromedriver_path = os.environ.get("CHROMEWEBDRIVER", "")
            if chromedriver_path:
                driver_exe = os.path.join(chromedriver_path, "chromedriver.exe")
                service = ChromeService(executable_path=driver_exe)
            else:
                service = ChromeService()

            driver = webdriver.Chrome(service=service, options=options)

        else:
            raise ValueError(f"Navigateur non supporte: {browser}")

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver