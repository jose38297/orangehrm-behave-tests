from behave import given, when
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage


@given("je suis connecte en tant qu'admin")
def step_login_admin(context):
    login_page = LoginPage(context.driver)
    login_page.login_as_admin()
    current_url = context.driver.current_url
    assert "dashboard" in current_url.lower() or "index" in current_url.lower(), \
        f"Connexion admin echouee. URL: {current_url}"


@given("je suis connecte en tant qu'employe")
def step_login_employee(context):
    login_page = LoginPage(context.driver)
    login_page.login_as_employee()
    current_url = context.driver.current_url
    assert "dashboard" in current_url.lower() or "index" in current_url.lower(), \
        f"Connexion employe echouee. URL: {current_url}"


@given("je suis connecte en tant que manager")
def step_login_manager(context):
    login_page = LoginPage(context.driver)
    login_page.login_as_manager()
    current_url = context.driver.current_url
    assert "dashboard" in current_url.lower() or "index" in current_url.lower(), \
        f"Connexion manager echouee. URL: {current_url}"


@given("je navigue vers la liste des employes")
@when("je navigue vers la liste des employes")
def step_navigate_employee_list(context):
    page = EmployeePage(context.driver)
    page.go_to_employee_list()
    context.employee_page = page
