# tests/test_leave.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Leave Management (6 Test Case)
# TC_LVE_01_POS  TC_LVE_02_NEG  TC_LVE_03_POS
# TC_LVE_04_NEG  TC_LVE_05_POS  TC_LVE_06_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.leave_page import LeavePage
from config.settings import VALID_USER, VALID_PASS


class TestLeave(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_LVE_01_POS: Halaman Leave List berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_LVE_01_POS_access_leave_list(self):
        """Memastikan halaman daftar Leave dapat diakses setelah login."""
        self._do_login()
        lp = LeavePage(self.driver)
        lp.open_leave_list()
        header = lp.get_header_text()
        self.assertTrue(len(header) > 0)

    # ─────────────────────────────────────────────
    # TC_LVE_02_NEG: Apply leave tanggal End < Start
    # ─────────────────────────────────────────────
    def test_TC_LVE_02_NEG_apply_leave_invalid_date_range(self):
        """Memastikan sistem menolak pengajuan leave jika tanggal End sebelum tanggal Start."""
        self._do_login()
        lp = LeavePage(self.driver)
        lp.open_apply_leave()
        lp.apply_with_invalid_date_range("2026-12-31", "2026-12-01")
        self.assertTrue(lp.is_success_message_absent())

    # ─────────────────────────────────────────────
    # TC_LVE_03_POS: URL halaman Leave List benar
    # ─────────────────────────────────────────────
    def test_TC_LVE_03_POS_leave_list_url_correct(self):
        """Memastikan URL halaman Leave List sesuai dengan yang diharapkan."""
        self._do_login()
        lp = LeavePage(self.driver)
        lp.open_leave_list()
        self.assertIn("viewLeaveList", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_LVE_04_NEG: Apply leave tanpa memilih Leave Type
    # ─────────────────────────────────────────────
    def test_TC_LVE_04_NEG_apply_leave_without_leave_type(self):
        """Memastikan sistem menampilkan validasi saat Leave Type tidak dipilih."""
        self._do_login()
        lp = LeavePage(self.driver)
        lp.open_apply_leave()
        lp.apply_leave_without_leave_type()
        errors = lp.get_required_errors()
        self.assertGreater(len(errors), 0)

    # ─────────────────────────────────────────────
    # TC_LVE_05_POS: Halaman Apply Leave berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_LVE_05_POS_apply_leave_page_loads(self):
        """Memastikan halaman Apply Leave berhasil dimuat setelah login."""
        self._do_login()
        lp = LeavePage(self.driver)
        lp.open_apply_leave()
        self.assertIn("applyLeave", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_LVE_06_NEG: Akses halaman Leave tanpa login
    # ─────────────────────────────────────────────
    def test_TC_LVE_06_NEG_access_leave_without_login(self):
        """Memastikan akses halaman Leave tanpa login diredirect ke halaman login."""
        lp = LeavePage(self.driver)
        lp.open_leave_list()
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)
