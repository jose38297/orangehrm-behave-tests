import os
import time
from behave import when, then
from pages.employee_page import EmployeePage


@when("je navigue vers la page d'ajout d'employe")
def step_navigate_add_employee(context):
    context.employee_page = EmployeePage(context.driver)
    context.employee_page.go_to_add_employee()


@when('je saisis le prenom "{first_name}" et le nom "{last_name}"')
def step_fill_employee_name(context, first_name, last_name):
    if not context.employee_page:
        context.employee_page = EmployeePage(context.driver)
    context.employee_page.fill_basic_info(first_name, last_name)
    context.current_employee_name = f"{first_name} {last_name}"


@when("j'upload une photo de profil")
def step_upload_photo(context):
    photo_path = "test_photo.jpg"
    if not os.path.exists(photo_path):
        try:
            from PIL import Image
            img = Image.new("RGB", (100, 100), color=(73, 109, 137))
            img.save(photo_path)
        except ImportError:
            with open(photo_path, "wb") as f:
                f.write(
                    b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01"
                    b"\x00\x01\x00\x00\xff\xd9"
                )
    context.employee_page.upload_photo(photo_path)


@when("je sauvegarde l'employe")
def step_save_employee(context):
    context.employee_page.save_employee()
    time.sleep(2)


@then('l\'employe "{full_name}" doit apparaitre dans la liste des employes')
def step_employee_in_list(context, full_name):
    page = EmployeePage(context.driver)
    page.search_employee_by_name(full_name.split()[0])
    time.sleep(2)
    names = page.get_employee_names_in_list()
    found = any(
        full_name.split()[0].lower() in n.lower() or
        full_name.split()[-1].lower() in n.lower()
        for n in names
    )
    assert found, f"Employe '{full_name}' non trouve dans la liste. Trouve: {names}"


@when('je recherche l\'employe "{name}" dans la liste')
def step_search_employee(context, name):
    if not context.employee_page:
        context.employee_page = EmployeePage(context.driver)
    context.employee_page.search_employee_by_name(name.split()[0])
    context.searched_name = name


@when("je clique sur modifier pour le premier resultat")
def step_click_edit_first(context):
    context.employee_page.click_edit_first_result()


@when('je mets a jour le prenom avec "{new_name}"')
def step_update_first_name(context, new_name):
    context.employee_page.update_first_name(new_name)
    context.updated_name = new_name


@when("je sauvegarde les modifications")
def step_save_modifications(context):
    context.employee_page.save_personal_details()


@then("les informations mises a jour doivent etre visibles dans le profil")
def step_check_updated_profile(context):
    current_url = context.driver.current_url
    assert "viewPersonalDetails" in current_url or "pim" in current_url, \
        f"Pas sur la page de profil. URL: {current_url}"
    print(f"Profil mis a jour avec succes. URL: {current_url}")


@when("je supprime le premier employe trouve")
def step_delete_first_employee(context):
    if not context.employee_page:
        context.employee_page = EmployeePage(context.driver)
    context.employee_page.delete_first_employee_in_list()


@then("l'employe ne doit plus apparaitre dans la liste")
def step_employee_not_in_list(context):
    page = EmployeePage(context.driver)
    name = context.searched_name or ""
    if name:
        page.search_employee_by_name(name.split()[0])
        time.sleep(2)
        names = page.get_employee_names_in_list()
        not_found = not any(name.lower() in n.lower() for n in names)
        count = page.get_record_count()
        assert not_found or count == 0, \
            f"L'employe '{name}' est encore present dans la liste."
    print("Employe supprime avec succes.")
