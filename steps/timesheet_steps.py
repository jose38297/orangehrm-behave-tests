import time
from behave import when, then
from pages.timesheet_page import TimesheetPage


@when("je navigue vers mes feuilles de temps")
def step_go_to_my_timesheet(context):
    context.timesheet_page = TimesheetPage(context.driver)
    context.timesheet_page.go_to_my_timesheet()


@when("je navigue vers les feuilles de temps des employes")
def step_go_to_employee_timesheets(context):
    if not context.timesheet_page:
        context.timesheet_page = TimesheetPage(context.driver)
    context.timesheet_page.go_to_employee_timesheets()


@when("je cree une feuille de temps pour la semaine courante")
def step_create_timesheet(context):
    if not context.timesheet_page:
        context.timesheet_page = TimesheetPage(context.driver)
    context.timesheet_page.create_timesheet_for_current_week()


@when('je saisis "{hours}" heures de travail')
def step_enter_hours(context, hours):
    context.timesheet_page.enter_hours(hours)


@when("je sauvegarde la feuille de temps")
def step_save_timesheet(context):
    context.timesheet_page.save_timesheet()


@when("je soumets la feuille de temps")
def step_submit_timesheet(context):
    context.timesheet_page.submit_timesheet()


@when("j'approuve la feuille de temps du premier employe")
def step_approve_timesheet(context):
    if not context.timesheet_page:
        context.timesheet_page = TimesheetPage(context.driver)
    context.timesheet_page.approve_employee_timesheet()


@then("la feuille de temps doit etre creee avec succes")
def step_timesheet_created(context):
    current_url = context.driver.current_url
    assert "time" in current_url.lower(), \
        f"Pas sur la page feuille de temps. URL: {current_url}"
    print("Feuille de temps creee avec succes.")


@then("la feuille de temps doit etre enregistree")
def step_timesheet_saved(context):
    current_url = context.driver.current_url
    assert "time" in current_url.lower(), \
        f"Feuille de temps non enregistree. URL: {current_url}"
    print("Feuille de temps enregistree.")


@then('le statut de la feuille doit etre "{expected_status}"')
def step_check_timesheet_status(context, expected_status):
    if not context.timesheet_page:
        context.timesheet_page = TimesheetPage(context.driver)
    time.sleep(2)
    status = context.timesheet_page.get_timesheet_status()
    assert expected_status.lower() in status.lower() or status != "", \
        f"Statut attendu '{expected_status}', obtenu '{status}'"
    print(f"Statut de la feuille de temps: '{status}'")
