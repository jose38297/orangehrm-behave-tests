import os


class Config:
    BASE_URL = os.environ.get(
        "BASE_URL",
        "https://opensource-demo.orangehrmlive.com"
    )
    LOGIN_URL = f"{BASE_URL}/web/index.php/auth/login"

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")
    EMPLOYEE_USERNAME = os.environ.get("EMPLOYEE_USERNAME", "Paul.T")
    EMPLOYEE_PASSWORD = os.environ.get("EMPLOYEE_PASSWORD", "Supervisor@1")
    MANAGER_USERNAME = os.environ.get("MANAGER_USERNAME", "Paul.T")
    MANAGER_PASSWORD = os.environ.get("MANAGER_PASSWORD", "Supervisor@1")

    BROWSER = os.environ.get("BROWSER", "chrome")
    HEADLESS = os.environ.get("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = int(os.environ.get("IMPLICIT_WAIT", 10))
    EXPLICIT_WAIT = int(os.environ.get("EXPLICIT_WAIT", 20))