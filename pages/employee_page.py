import time
import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config


class EmployeePage(BasePage):
    PIM_URL          = f"{Config.BASE_URL}/web/index.php/pim/viewEmployeeList"
    ADD_EMPLOYEE_URL = f"{Config.BASE_URL}/web/index.php/pim/addEmployee"

    ADD_EMPLOYEE_BTN     = (By.CSS_SELECTOR, "button.oxd-button--secondary")
    SEARCH_BUTTON        = (By.CSS_SELECTOR, "button[type='submit']")
    EMPLOYEE_ROWS        = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
    EMPLOYEE_NAME_CELLS  = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row .oxd-table-cell:nth-child(3)")
    CONFIRM_DELETE_BTN   = (By.CSS_SELECTOR, ".oxd-button--label-danger")

    FIRST_NAME_INPUT     = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT    = (By.NAME, "middleName")
    LAST_NAME_INPUT      = (By.NAME, "lastName")
    PHOTO_INPUT          = (By.CSS_SELECTOR, "input[type='file']")
    SAVE_BUTTON          = (By.CSS_SELECTOR, "button[type='submit']")

    PERSONAL_FIRST       = (By.NAME, "firstName")
    PERSONAL_LAST        = (By.NAME, "lastName")

    def go_to_employee_list(self):
        self.navigate_to(self.PIM_URL)
        self.wait_loading()
        return self

    def go_to_add_employee(self):
        self.navigate_to(self.ADD_EMPLOYEE_URL)
        self.wait_loading()
        return self

    def fill_basic_info(self, first_name, last_name, middle_name=""):
        self.helper.safe_type(self.FIRST_NAME_INPUT, first_name)
        if middle_name:
            self.helper.safe_type(self.MIDDLE_NAME_INPUT, middle_name)
        self.helper.safe_type(self.LAST_NAME_INPUT, last_name)
        return self

    def upload_photo(self, photo_path):
        if os.path.exists(photo_path):
            photo_input = self.driver.find_element(*self.PHOTO_INPUT)
            photo_input.send_keys(os.path.abspath(photo_path))
            time.sleep(1)
        return self

    def save_employee(self):
        self.helper.safe_click(self.SAVE_BUTTON)
        self.wait_loading()
        time.sleep(2)
        return self

    def search_employee_by_name(self, name):
        self.go_to_employee_list()
        time.sleep(1)
        search_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input.oxd-input")
        if len(search_inputs) > 1:
            search_inputs[1].clear()
            search_inputs[1].send_keys(name)
            time.sleep(1)
        self.helper.safe_click(self.SEARCH_BUTTON)
        self.wait_loading()
        time.sleep(2)
        return self

    def get_employee_names_in_list(self):
        rows = self.driver.find_elements(*self.EMPLOYEE_NAME_CELLS)
        return [r.text.strip() for r in rows if r.text.strip()]

    def is_employee_in_list(self, full_name):
        names = self.get_employee_names_in_list()
        return any(full_name.lower() in n.lower() for n in names)

    def get_record_count(self):
        rows = self.driver.find_elements(*self.EMPLOYEE_ROWS)
        return len([r for r in rows if r.text.strip()])

    def click_edit_first_result(self):
        edit_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
        if edit_buttons:
            first_row = edit_buttons[0]
            pencil = first_row.find_element(By.CSS_SELECTOR, "button i.bi-pencil-fill")
            pencil.click()
            self.wait_loading()
            time.sleep(1)
        return self

    def update_first_name(self, new_first_name):
        field = self.helper.wait_for_visible(self.PERSONAL_FIRST)
        field.clear()
        field.send_keys(new_first_name)
        return self

    def save_personal_details(self):
        save_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
        if save_buttons:
            save_buttons[0].click()
            self.wait_loading()
            time.sleep(2)
        return self

    def delete_first_employee_in_list(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
        if rows:
            trash = rows[0].find_element(By.CSS_SELECTOR, "button i.bi-trash")
            trash.click()
            time.sleep(1)
            self.helper.safe_click(self.CONFIRM_DELETE_BTN)
            self.wait_loading()
            time.sleep(2)
        return self

    def is_no_records_found(self):
        spans = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-text")
        return any("No Records Found" in s.text for s in spans)

    def filter_by_department(self, department_name):
        self.go_to_employee_list()
        time.sleep(1)
        dropdowns = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-select-text-input")
        if len(dropdowns) >= 2:
            dropdowns[1].click()
            time.sleep(0.5)
            options = self.driver.find_elements(
                By.CSS_SELECTOR, ".oxd-select-dropdown .oxd-select-option"
            )
            for opt in options:
                if department_name.lower() in opt.text.lower():
                    opt.click()
                    break
        self.helper.safe_click(self.SEARCH_BUTTON)
        self.wait_loading()
        time.sleep(2)
        return self
