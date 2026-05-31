# pages/employee_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Modul Employee (PIM) OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import BASE_URL, EXPLICIT_WAIT


class EmployeePage:
    FIRST_NAME_INPUT   = (By.NAME, "firstName")
    LAST_NAME_INPUT    = (By.NAME, "lastName")
    SUBMIT_BUTTON      = (By.XPATH, "//button[@type='submit']")
    SEARCH_NAME_INPUT  = (By.XPATH, "//input[@placeholder='Type for hints...']")
    REQUIRED_SPANS     = (By.XPATH, "//span[text()='Required']")
    TABLE_ROWS         = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    NO_RECORDS         = (By.XPATH, "//span[text()='No Records Found']")

    ADD_URL    = f"{BASE_URL}/pim/addEmployee"
    LIST_URL   = f"{BASE_URL}/pim/viewEmployeeList"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    # ── Add Employee ──────────────────────────────────────────

    def open_add_form(self):
        self.driver.get(self.ADD_URL)
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT))

    def fill_first_name(self, name: str):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(name)

    def fill_last_name(self, name: str):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(name)

    def submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(2)

    def get_required_errors(self) -> list:
        time.sleep(1)
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    # ── Employee List / Search ────────────────────────────────

    def open_list(self):
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.presence_of_element_located(self.SEARCH_NAME_INPUT))

    def search_employee(self, name: str):
        field = self.driver.find_element(*self.SEARCH_NAME_INPUT)
        field.send_keys(name)
        time.sleep(2)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(2)

    def get_result_rows(self) -> list:
        return self.driver.find_elements(*self.TABLE_ROWS)

    def get_no_records_element(self):
        return self.wait.until(EC.presence_of_element_located(self.NO_RECORDS))
