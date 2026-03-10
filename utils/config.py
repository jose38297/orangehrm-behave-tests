import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
    LOGIN_URL = f"{BASE_URL}/web/index.php/auth/login"

    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
    EMPLOYEE_USERNAME = os.getenv("EMPLOYEE_USERNAME", "Paul.T")
    EMPLOYEE_PASSWORD = os.getenv("EMPLOYEE_PASSWORD", "Supervisor@1")
    MANAGER_USERNAME = os.getenv("MANAGER_USERNAME", "Paul.T")
    MANAGER_PASSWORD = os.getenv("MANAGER_PASSWORD", "Supervisor@1")

    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 20))
