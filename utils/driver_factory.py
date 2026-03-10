import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
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
            options.add_argument("--remote-debugging-port=9222")
            options.add_argument("--disable-extensions")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            # Supprime le ChromeDriver du PATH pour eviter les conflits de version
            clean_path = os.environ.get("PATH", "")
            filtered = [
                p for p in clean_path.split(os.pathsep)
                if "SeleniumWebDrivers" not in p and "chromedriver" not in p.lower()
            ]
            os.environ["PATH"] = os.pathsep.join(filtered)

            # Telecharge le bon ChromeDriver automatiquement
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        else:
            raise ValueError(f"Navigateur non supporte: {browser}")

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver