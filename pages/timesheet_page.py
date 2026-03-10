import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config


class TimesheetPage(BasePage):
    MY_TIMESHEET_URL       = f"{Config.BASE_URL}/web/index.php/time/viewMyTimesheets"
    EMPLOYEE_TIMESHEET_URL = f"{Config.BASE_URL}/web/index.php/time/viewEmployeeTimesheet"

    ADD_TIMESHEET_BTN = (By.CSS_SELECTOR, "button.oxd-button--secondary")

    def go_to_my_timesheet(self):
        self.navigate_to(self.MY_TIMESHEET_URL)
        self.wait_loading()
        time.sleep(1)
        return self

    def go_to_employee_timesheets(self):
        self.navigate_to(self.EMPLOYEE_TIMESHEET_URL)
        self.wait_loading()
        time.sleep(1)
        return self

    def create_timesheet_for_current_week(self):
        self.go_to_my_timesheet()
        if self.helper.is_element_present(self.ADD_TIMESHEET_BTN):
            self.helper.safe_click(self.ADD_TIMESHEET_BTN)
            self.wait_loading()
            time.sleep(1)
        return self

    def enter_hours(self, hours="8"):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input.oxd-input")
        editable = [
            i for i in inputs
            if not i.get_attribute("disabled") and not i.get_attribute("readonly")
        ]
        if editable:
            editable[0].clear()
            editable[0].send_keys(hours)
        return self

    def submit_timesheet(self):
        submit_btns = self.driver.find_elements(
            By.XPATH, "//button[contains(., 'Submit')]"
        )
        if submit_btns:
            submit_btns[0].click()
            self.wait_loading()
            time.sleep(2)
        return self

    def save_timesheet(self):
        save_btns = self.driver.find_elements(
            By.XPATH, "//button[contains(., 'Save')]"
        )
        if save_btns:
            save_btns[0].click()
            self.wait_loading()
            time.sleep(2)
        return self

    def get_timesheet_status(self):
        badges = self.driver.find_elements(
            By.CSS_SELECTOR, ".oxd-chip, .orangehrm-timesheet-status span, .oxd-badge"
        )
        for b in badges:
            if b.text.strip():
                return b.text.strip()
        status_texts = self.driver.find_elements(
            By.XPATH,
            "//*[contains(text(),'Submitted') or contains(text(),'Approved') or contains(text(),'Not Submitted')]"
        )
        if status_texts:
            return status_texts[0].text.strip()
        return ""

    def approve_employee_timesheet(self, employee_name=None):
        self.go_to_employee_timesheets()
        time.sleep(1)
        if employee_name:
            inputs = self.driver.find_elements(By.CSS_SELECTOR, "input.oxd-input")
            for inp in inputs:
                placeholder = inp.get_attribute("placeholder") or ""
                if "hint" in placeholder.lower() or "name" in placeholder.lower():
                    inp.clear()
                    inp.send_keys(employee_name)
                    time.sleep(1)
                    break
            search_btns = self.driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
            if search_btns:
                search_btns[0].click()
                self.wait_loading()
                time.sleep(1)

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
        if rows:
            view_btn = rows[0].find_elements(
                By.CSS_SELECTOR, "button i.bi-eye-fill, button.oxd-icon-button"
            )
            if view_btn:
                view_btn[0].click()
                self.wait_loading()
                time.sleep(1)

        approve_btns = self.driver.find_elements(
            By.XPATH, "//button[contains(., 'Approve')]"
        )
        if approve_btns:
            approve_btns[0].click()
            self.wait_loading()
            time.sleep(2)
        return self
