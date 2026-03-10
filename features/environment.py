import os
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage


def before_all(context):
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports/junit", exist_ok=True)
    context.base_url = "https://opensource-demo.orangehrmlive.com"


def before_scenario(context, scenario):
    context.driver = DriverFactory.get_driver()
    context.login_page = LoginPage(context.driver)
    context.current_employee_name = None
    context.employee_page = None
    context.leave_page = None
    context.timesheet_page = None
    context.searched_name = None


def after_scenario(context, scenario):
    if scenario.status == "failed":
        safe_name = scenario.name.replace(" ", "_").replace("/", "-")[:50]
        screenshot_path = f"reports/screenshots/FAIL_{safe_name}.png"
        try:
            context.driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot enregistre: {screenshot_path}")
        except Exception as e:
            print(f"Impossible de capturer le screenshot: {e}")

    if hasattr(context, "driver") and context.driver:
        context.driver.quit()


def after_all(context):
    print("\nSuite de tests terminee.")
