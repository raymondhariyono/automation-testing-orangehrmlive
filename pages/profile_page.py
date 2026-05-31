# pages/profile_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Modul Profile (My Info) OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import BASE_URL, EXPLICIT_WAIT


class ProfilePage:
    HEADER_H6       = (By.TAG_NAME, "h6")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    SUBMIT_BUTTON   = (By.XPATH, "//button[@type='submit']")
    REQUIRED_SPANS  = (By.XPATH, "//span[text()='Required']")
    NICKNAME_INPUT  = (By.XPATH, "//label[text()='Nickname']/following::input[1]")

    MY_INFO_URL = f"{BASE_URL}/pim/viewMyDetails"

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open_my_info(self):
        self.driver.get(self.MY_INFO_URL)
        self.wait.until(EC.presence_of_element_located(self.HEADER_H6))

    def clear_first_name(self):
        field = self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT))
        field.clear()

    def save(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(1)

    def get_required_errors(self) -> list:
        return self.driver.find_elements(*self.REQUIRED_SPANS)

    def get_header_text(self) -> str:
        return self.driver.find_element(*self.HEADER_H6).text
