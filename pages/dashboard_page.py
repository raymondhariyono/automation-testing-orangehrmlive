# pages/dashboard_page.py
# ─────────────────────────────────────────────────────────────
# Page Object: Halaman Dashboard OrangeHRM
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.settings import EXPLICIT_WAIT


class DashboardPage:
    USER_DROPDOWN   = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BUTTON   = (By.XPATH, "//a[text()='Logout']")
    SEARCH_BAR      = (By.XPATH, "//input[@placeholder='Search']")
    SEARCH_RESULTS  = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, EXPLICIT_WAIT)

    def wait_for_dashboard(self):
        self.wait.until(EC.url_contains("dashboard"))

    def logout(self):
        import time
        self.driver.find_element(*self.USER_DROPDOWN).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        self.wait.until(EC.url_contains("auth/login"))

    def search_global(self, keyword: str):
        import time
        search = self.wait.until(EC.presence_of_element_located(self.SEARCH_BAR))
        search.click()
        search.send_keys(keyword)
        time.sleep(4)

    def get_search_suggestions(self) -> list:
        return self.driver.find_elements(*self.SEARCH_RESULTS)
