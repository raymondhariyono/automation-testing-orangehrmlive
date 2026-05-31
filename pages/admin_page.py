# pages/admin_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Modul Admin OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import BASE_URL, EXPLICIT_WAIT


class AdminPage:
    HEADER_H5       = (By.TAG_NAME, "h5")
    SUBMIT_BUTTON   = (By.XPATH, "//button[@type='submit']")
    REQUIRED_SPANS  = (By.XPATH, "//span[text()='Required']")
    ADD_USER_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    JOB_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")

    USERS_URL     = f"{BASE_URL}/admin/viewSystemUsers"
    ADD_USER_URL  = f"{BASE_URL}/admin/saveSystemUser"
    JOB_TITLE_URL = f"{BASE_URL}/admin/viewJobTitleList"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_system_users(self):
        self.driver.get(self.USERS_URL)
        self.wait.until(EC.presence_of_element_located(self.HEADER_H5))

    def open_add_user_form(self):
        self.driver.get(self.ADD_USER_URL)
        self.wait.until(EC.presence_of_element_located(self.SUBMIT_BUTTON))

    def open_job_title_list(self):
        import time
        from selenium.webdriver.support import expected_conditions as EC
        self.driver.get(self.JOB_TITLE_URL)
        self.wait.until(EC.url_contains("viewJobTitleList"))
        time.sleep(2) # Tambahan jeda agar aman

    def submit_empty_form(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(1)

    def get_required_errors(self) -> list:
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    def get_header_text(self) -> str:
        return self.driver.find_element(*self.HEADER_H5).text
