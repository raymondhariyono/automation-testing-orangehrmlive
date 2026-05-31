# pages/reports_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Modul Reports OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import BASE_URL, EXPLICIT_WAIT


class ReportsPage:
    HEADER_H5       = (By.TAG_NAME, "h5")
    ADD_BUTTON      = (By.XPATH, "//button[normalize-space()='Add']")
    REPORT_NAME_INPUT = (By.XPATH, "//label[text()='Report Name']/following::input[1]")
    SUBMIT_BUTTON   = (By.XPATH, "//button[@type='submit']")
    REQUIRED_SPANS  = (By.XPATH, "//span[text()='Required']")

    REPORT_LIST_URL = f"{BASE_URL}/pim/viewDefinedReportList"
    ADD_REPORT_URL  = f"{BASE_URL}/pim/defineReport"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_report_list(self):
        self.driver.get(self.REPORT_LIST_URL)
        self.wait.until(EC.presence_of_element_located(self.HEADER_H5))

    def open_add_report_form(self):
        self.driver.get(self.ADD_REPORT_URL)
        time.sleep(2)

    def submit_empty_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(1)

    def get_required_errors(self) -> list:
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    def get_header_text(self) -> str:
        return self.driver.find_element(*self.HEADER_H5).text
