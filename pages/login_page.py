# pages/login_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Halaman Login OrangeHRM
# ─────────────────────────────────────────────────────────────

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import LOGIN_URL, EXPLICIT_WAIT


class LoginPage:
    # Locators
    USERNAME_INPUT  = (By.NAME, "username")
    PASSWORD_INPUT  = (By.NAME, "password")
    SUBMIT_BUTTON   = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE   = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
    REQUIRED_SPANS  = (By.XPATH, "//span[text()='Required']")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def open(self):
        self.driver.get(LOGIN_URL)
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))

    def enter_username(self, username: str):
        field = self.driver.find_element(*self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password: str):
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def login(self, username: str, password: str):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        time.sleep(2)

    def get_error_message(self) -> str:
        el = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        return el.text

    def get_required_errors(self) -> list:
        return self.wait.until(
            EC.presence_of_all_elements_located(self.REQUIRED_SPANS)
        )
