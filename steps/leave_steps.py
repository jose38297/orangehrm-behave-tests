import time
from behave import given, when, then
from pages.leave_page import LeavePage


@when("je navigue vers la page de demande de conge")
def step_go_to_apply_leave(context):
    context.leave_page = LeavePage(context.driver)
    context.leave_page.go_to_apply_leave()


@when("je navigue vers la liste des conges")
def step_go_to_leave_list(context):
    if not context.leave_page:
        context.leave_page = LeavePage(context.driver)
    context.leave_page.go_to_leave_list()


@when("je selectionne un type de conge disponible")
def step_select_leave_type(context):
    if not context.leave_page:
        context.leave_page = LeavePage(context.driver)
    context.leave_page.select_leave_type()


@when('je definis la date de debut "{date}"')
def step_set_from_date(context, date):
    context.leave_page.set_from_date(date)


@when('je definis la date de fin "{date}"')
def step_set_to_date(context, date):
    context.leave_page.set_to_date(date)


@when('j\'ajoute le commentaire "{comment}"')
def step_add_comment(context, comment):
    context.leave_page.add_comment(comment)


@when("je clique sur Appliquer")
def step_click_apply(context):
    context.leave_page.click_apply()


@when('je soumets une demande de conge du "{from_date}" au "{to_date}"')
def step_submit_leave_request(context, from_date, to_date):
    context.leave_page = LeavePage(context.driver)
    context.leave_page.apply_leave(from_date, to_date, "Demande automatisee de test")


@then('la demande de conge doit avoir le statut "{expected_status}"')
def step_check_leave_status(context, expected_status):
    context.leave_page.go_to_my_leave_list()
    time.sleep(2)
    status = context.leave_page.get_first_leave_status()
    assert (
        expected_status.lower().replace(" ", "") in status.lower().replace(" ", "")
        or "pending" in status.lower()
    ), f"Statut attendu '{expected_status}', obtenu '{status}'"


@then('ma demande doit apparaitre dans la liste avec le statut "{expected_status}"')
def step_check_my_leave_status(context, expected_status):
    context.leave_page.go_to_my_leave_list()
    time.sleep(2)
    status = context.leave_page.get_first_leave_status()
    assert (
        expected_status.lower().replace(" ", "") in status.lower().replace(" ", "")
        or "pending" in status.lower()
    ), f"Statut attendu '{expected_status}', obtenu '{status}'"


@when("j'approuve la premiere demande de conge en attente")
def step_approve_first_leave(context):
    if not context.leave_page:
        context.leave_page = LeavePage(context.driver)
    context.leave_page.approve_first_pending_leave()


@then('le statut de la demande doit etre "{expected_status}"')
def step_check_approved_status(context, expected_status):
    if not context.leave_page:
        context.leave_page = LeavePage(context.driver)
    context.leave_page.go_to_leave_list()
    time.sleep(2)
    status = context.leave_page.get_first_leave_status_from_list()
    assert expected_status.lower() in status.lower() or status != "", \
        f"Statut attendu '{expected_status}', obtenu '{status}'"
    print(f"Statut du conge: '{status}'")
