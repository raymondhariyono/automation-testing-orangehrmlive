# tests/test_time.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Time & Attendance (4 Test Case)
# TC_TIM_01_POS  TC_TIM_02_NEG  TC_TIM_03_POS  TC_TIM_04_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.time_page import TimePage
from config.settings import VALID_USER, VALID_PASS


class TestTime(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_TIM_01_POS: Halaman Employee Timesheet berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_TIM_01_POS_access_timesheet_page(self):
        """Memastikan halaman Time & Attendance (Employee Timesheet) dapat diakses."""
        self._do_login()
        tp = TimePage(self.driver)
        tp.open_timesheet()
        self.assertIn("time", self.driver.current_url.lower())

    # ─────────────────────────────────────────────
    # TC_TIM_02_NEG: Submit Project Report Form tanpa data → validasi muncul
    # ─────────────────────────────────────────────
    def test_TC_TIM_02_NEG_project_report_empty_form(self):
        """Memastikan sistem menampilkan validasi jika Project Report disubmit tanpa data."""
        self._do_login()
        tp = TimePage(self.driver)
        tp.open_project_report()
        tp.submit_empty_project_report()
        errors = tp.get_required_errors()
        self.assertGreater(len(errors), 0)

    # ─────────────────────────────────────────────
    # TC_TIM_03_POS: Header halaman Timesheet terisi dengan benar
    # ─────────────────────────────────────────────
    def test_TC_TIM_03_POS_timesheet_page_has_valid_header(self):
        """Memastikan halaman Timesheet memiliki header yang valid dan tidak kosong."""
        self._do_login()
        tp = TimePage(self.driver)
        tp.open_timesheet()
        header = tp.get_header_text()
        self.assertTrue(len(header) > 0)

    # ─────────────────────────────────────────────
    # TC_TIM_04_NEG: Akses halaman Time tanpa login → redirect ke login
    # ─────────────────────────────────────────────
    def test_TC_TIM_04_NEG_access_timesheet_without_login(self):
        """Memastikan akses halaman Timesheet tanpa login diredirect ke halaman login."""
        tp = TimePage(self.driver)
        tp.open_timesheet()
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)
