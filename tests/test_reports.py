# tests/test_reports.py
# ─────────────────────────────────────────────────────────────
# Modul Test: PIM Reports (4 Test Case)
# TC_RPT_01_POS  TC_RPT_02_NEG  TC_RPT_03_POS  TC_RPT_04_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.reports_page import ReportsPage
from config.settings import VALID_USER, VALID_PASS


class TestReports(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_RPT_01_POS: Halaman PIM Reports berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_RPT_01_POS_access_reports_page(self):
        """Memastikan halaman daftar PIM Reports dapat diakses setelah login."""
        self._do_login()
        rp = ReportsPage(self.driver)
        rp.open_report_list()
        self.assertIn("viewDefinedReportList", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_RPT_02_NEG: Tambah report tanpa mengisi Report Name
    # ─────────────────────────────────────────────
    def test_TC_RPT_02_NEG_add_report_empty_name(self):
        """Memastikan sistem menolak penambahan report jika Report Name dikosongkan."""
        self._do_login()
        rp = ReportsPage(self.driver)
        rp.open_add_report_form()
        rp.submit_empty_form()
        errors = rp.get_required_errors()
        self.assertGreater(len(errors), 0)

    # ─────────────────────────────────────────────
    # TC_RPT_03_POS: Header halaman Reports terisi dengan benar
    # ─────────────────────────────────────────────
    def test_TC_RPT_03_POS_reports_page_has_valid_header(self):
        """Memastikan halaman Reports menampilkan header yang valid."""
        self._do_login()
        rp = ReportsPage(self.driver)
        rp.open_report_list()
        header = rp.get_header_text()
        self.assertTrue(len(header) > 0)

    # ─────────────────────────────────────────────
    # TC_RPT_04_NEG: Akses halaman Reports tanpa login
    # ─────────────────────────────────────────────
    def test_TC_RPT_04_NEG_access_reports_without_login(self):
        """Memastikan akses halaman Reports tanpa login diredirect ke halaman login."""
        rp = ReportsPage(self.driver)
        rp.open_report_list()
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)
