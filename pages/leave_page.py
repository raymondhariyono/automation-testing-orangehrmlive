# pages/leave_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Modul Leave OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import BASE_URL, EXPLICIT_WAIT


class LeavePage:
    HEADER_H5       = (By.TAG_NAME, "h5")
    DATE_FIELDS     = (By.XPATH, "//input[@placeholder='yyyy-dd-mm']")
    SUBMIT_BUTTON   = (By.XPATH, "//button[@type='submit']")
    LEAVE_TYPE_DD   = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
    REQUIRED_SPANS  = (By.XPATH, "//span[text()='Required']")

    LIST_URL  = f"{BASE_URL}/leave/viewLeaveList"
    APPLY_URL = f"{BASE_URL}/leave/applyLeave"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_leave_list(self):
        self.driver.get(self.LIST_URL)
        self.wait.until(EC.presence_of_element_located(self.HEADER_H5))

    def open_apply_leave(self):
        self.driver.get(self.APPLY_URL)
        time.sleep(2)

    def apply_with_invalid_date_range(self, from_date: str, to_date: str):
        """Isi tanggal Start dan End yang tidak valid lalu submit."""
        date_fields = self.driver.find_elements(*self.DATE_FIELDS)
        if len(date_fields) >= 2:
            date_fields[0].send_keys(from_date)
            date_fields[1].send_keys(to_date)
            time.sleep(1)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(2)

    def apply_leave_without_leave_type(self):
        import time
        btn = self.driver.find_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

    def get_required_errors(self) -> list:
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    def is_success_message_absent(self) -> bool:
        return "Leave applied successfully" not in self.driver.page_source

    def get_header_text(self) -> str:
        return self.driver.find_element(*self.HEADER_H5).text
