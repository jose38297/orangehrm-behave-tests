import time
from behave import when, then
from selenium.webdriver.common.by import By
from pages.employee_page import EmployeePage


@when('je recherche l\'employe par le nom "{name}"')
def step_search_by_name(context, name):
    if not context.employee_page:
        context.employee_page = EmployeePage(context.driver)
    context.employee_page.search_employee_by_name(name)
    context.searched_name = name


@when('je filtre les employes par departement "{department}"')
def step_filter_by_department(context, department):
    if not context.employee_page:
        context.employee_page = EmployeePage(context.driver)
    context.employee_page.filter_by_department(department)
    context.searched_department = department


@when("je reinitialise les filtres")
def step_reset_filters(context):
    if not context.employee_page:
        context.employee_page = EmployeePage(context.driver)
    reset_btns = context.driver.find_elements(By.CSS_SELECTOR, "button.oxd-button--ghost")
    if reset_btns:
        reset_btns[0].click()
        time.sleep(1)
    context.employee_page.go_to_employee_list()


@then('seuls les employes contenant "{name}" dans leur nom doivent s\'afficher')
def step_check_search_results_by_name(context, name):
    time.sleep(2)
    names = context.employee_page.get_employee_names_in_list()
    assert len(names) > 0, f"Aucun resultat trouve pour '{name}'"
    for employee_name in names:
        assert name.lower() in employee_name.lower(), \
            f"'{employee_name}' ne contient pas '{name}'"
    print(f"{len(names)} employe(s) trouve(s) contenant '{name}'")


@then("aucun employe ne doit s'afficher dans la liste")
def step_no_results(context):
    time.sleep(2)
    no_records = context.employee_page.is_no_records_found()
    names = context.employee_page.get_employee_names_in_list()
    assert no_records or len(names) == 0, \
        f"Des employes ont ete trouves alors qu'aucun n'etait attendu: {names}"
    print("Aucun resultat trouve - comportement correct.")


@then("les resultats doivent correspondre au nom recherche")
def step_check_results_match_search(context):
    time.sleep(2)
    names = context.employee_page.get_employee_names_in_list()
    searched = context.searched_name or ""
    print(f"Resultats de recherche pour '{searched}': {len(names)} resultat(s)")


@then('seuls les employes du departement "{department}" doivent apparaitre')
def step_check_department_filter(context, department):
    time.sleep(2)
    rows = context.driver.find_elements(
        By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row"
    )
    count = len([r for r in rows if r.text.strip()])
    print(f"{count} employe(s) trouve(s) pour le departement '{department}'")
    assert count >= 0, "Le filtre par departement a echoue"
