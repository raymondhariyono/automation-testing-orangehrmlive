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
    HEADER_H6         = (By.TAG_NAME, "h6")
    SUBMIT_BUTTON     = (By.XPATH, "//button[@type='submit']")
    REQUIRED_SPANS    = (By.XPATH, "//span[text()='Required']")
    PROJECT_REPORTS_LINK = (By.XPATH, "//a[contains(@href,'viewProjectReportCriteria')]")

    TIMESHEET_URL    = f"{BASE_URL}/time/viewEmployeeTimesheet"
    PROJECT_RPT_URL  = f"{BASE_URL}/time/displayProjectReportCriteria"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_timesheet(self):
        import time
        self.driver.get(self.TIMESHEET_URL)
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located(self.HEADER_H6))

    def open_project_report(self):
        self.driver.get(self.PROJECT_RPT_URL)
        time.sleep(2)

    def submit_empty_project_report(self):
        import time
        btn = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn) 
        time.sleep(2)

    def get_required_errors(self) -> list:
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    def get_header_text(self) -> str:
        return self.driver.find_element(*self.HEADER_H6).text
