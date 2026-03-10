import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config


class LeavePage(BasePage):
    APPLY_LEAVE_URL  = f"{Config.BASE_URL}/web/index.php/leave/applyLeave"
    MY_LEAVE_URL     = f"{Config.BASE_URL}/web/index.php/leave/viewMyLeaveList"
    LEAVE_LIST_URL   = f"{Config.BASE_URL}/web/index.php/leave/viewLeaveList"

    LEAVE_TYPE_DROPDOWN = (By.CSS_SELECTOR, ".oxd-select-text-input")
    APPLY_BUTTON        = (By.CSS_SELECTOR, "button[type='submit']")
    STATUS_CELLS        = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row .oxd-table-cell:nth-child(5) .oxd-chip")
    LEAVE_ROWS          = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-row")
    DROPDOWN_OPTIONS    = (By.CSS_SELECTOR, ".oxd-select-dropdown .oxd-select-option")

    def go_to_apply_leave(self):
        self.navigate_to(self.APPLY_LEAVE_URL)
        self.wait_loading()
        time.sleep(1)
        return self

    def go_to_my_leave_list(self):
        self.navigate_to(self.MY_LEAVE_URL)
        self.wait_loading()
        time.sleep(1)
        return self

    def go_to_leave_list(self):
        self.navigate_to(self.LEAVE_LIST_URL)
        self.wait_loading()
        time.sleep(1)
        return self

    def select_leave_type(self, leave_type=None):
        dropdown = self.helper.wait_for_clickable(self.LEAVE_TYPE_DROPDOWN)
        dropdown.click()
        time.sleep(0.5)
        options = self.driver.find_elements(*self.DROPDOWN_OPTIONS)
        if options:
            if leave_type:
                for opt in options:
                    if leave_type.lower() in opt.text.lower():
                        opt.click()
                        return self
            for opt in options:
                if opt.text.strip() and "Select" not in opt.text:
                    opt.click()
                    break
        time.sleep(0.5)
        return self

    def set_from_date(self, date):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input.oxd-input")
        date_inputs = [
            i for i in inputs
            if i.get_attribute("placeholder") and "yyyy" in i.get_attribute("placeholder")
        ]
        if date_inputs:
            date_inputs[0].clear()
            date_inputs[0].send_keys(date)
        time.sleep(0.5)
        return self

    def set_to_date(self, date):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input.oxd-input")
        date_inputs = [
            i for i in inputs
            if i.get_attribute("placeholder") and "yyyy" in i.get_attribute("placeholder")
        ]
        if len(date_inputs) >= 2:
            date_inputs[1].clear()
            date_inputs[1].send_keys(date)
        time.sleep(0.5)
        return self

    def add_comment(self, comment):
        textarea = self.driver.find_elements(By.CSS_SELECTOR, "textarea")
        if textarea:
            textarea[0].clear()
            textarea[0].send_keys(comment)
        return self

    def click_apply(self):
        self.helper.safe_click(self.APPLY_BUTTON)
        self.wait_loading()
        time.sleep(2)
        return self

    def apply_leave(self, from_date, to_date, comment="Test leave"):
        self.go_to_apply_leave()
        self.select_leave_type()
        self.set_from_date(from_date)
        self.set_to_date(to_date)
        self.add_comment(comment)
        self.click_apply()
        return self

    def get_first_leave_status(self):
        self.go_to_my_leave_list()
        chips = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-chip")
        if chips:
            return chips[0].text.strip()
        rows = self.driver.find_elements(*self.LEAVE_ROWS)
        if rows:
            cells = rows[0].find_elements(By.CSS_SELECTOR, ".oxd-table-cell")
            if len(cells) >= 5:
                return cells[4].text.strip()
        return ""

    def approve_first_pending_leave(self):
        self.go_to_leave_list()
        time.sleep(1)
        rows = self.driver.find_elements(*self.LEAVE_ROWS)
        for row in rows:
            chips = row.find_elements(By.CSS_SELECTOR, ".oxd-chip")
            pending = any("Pending" in c.text or "En attente" in c.text for c in chips)
            if pending:
                approve_btns = row.find_elements(By.CSS_SELECTOR, "button i.bi-check")
                if approve_btns:
                    approve_btns[0].click()
                    self.wait_loading()
                    time.sleep(2)
                    return self
        return self

    def get_first_leave_status_from_list(self):
        rows = self.driver.find_elements(*self.LEAVE_ROWS)
        if rows:
            chips = rows[0].find_elements(By.CSS_SELECTOR, ".oxd-chip")
            if chips:
                return chips[0].text.strip()
        return ""
