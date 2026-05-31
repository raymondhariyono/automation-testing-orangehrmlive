# pages/time_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Modul Time & Attendance OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import BASE_URL, EXPLICIT_WAIT


class TimePage:
    HEADER_H5         = (By.TAG_NAME, "h5")
    SUBMIT_BUTTON     = (By.XPATH, "//button[@type='submit']")
    REQUIRED_SPANS    = (By.XPATH, "//span[text()='Required']")
    PROJECT_REPORTS_LINK = (By.XPATH, "//a[contains(@href,'viewProjectReportCriteria')]")

    TIMESHEET_URL    = f"{BASE_URL}/time/viewEmployeeTimesheet"
    PROJECT_RPT_URL  = f"{BASE_URL}/time/viewProjectReportCriteria"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_timesheet(self):
        self.driver.get(self.TIMESHEET_URL)
        self.wait.until(EC.presence_of_element_located(self.HEADER_H5))

    def open_project_report(self):
        self.driver.get(self.PROJECT_RPT_URL)
        time.sleep(2)

    def submit_empty_project_report(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(1)

    def get_required_errors(self) -> list:
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    def get_header_text(self) -> str:
        return self.driver.find_element(*self.HEADER_H5).text
