# tests/test_admin.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Admin & User Management (6 Test Case)
# TC_ADM_01_POS  TC_ADM_02_NEG  TC_ADM_03_POS
# TC_ADM_04_NEG  TC_ADM_05_POS  TC_ADM_06_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from config.settings import VALID_USER, VALID_PASS


class TestAdmin(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_ADM_01_POS: Halaman System Users berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_ADM_01_POS_access_system_users_page(self):
        """Memastikan menu Admin dapat diakses dan menampilkan daftar System Users."""
        self._do_login()
        ap = AdminPage(self.driver)
        ap.open_system_users()
        self.assertIn("viewSystemUsers", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_ADM_02_NEG: Tambah user tanpa mengisi field apapun
    # ─────────────────────────────────────────────
    def test_TC_ADM_02_NEG_add_user_all_fields_empty(self):
        """Memastikan sistem menolak penambahan user baru jika semua field kosong."""
        self._do_login()
        ap = AdminPage(self.driver)
        ap.open_add_user_form()
        ap.submit_empty_form()
        errors = ap.get_required_errors()
        self.assertGreater(len(errors), 0)

    # ─────────────────────────────────────────────
    # TC_ADM_03_POS: Halaman Job Titles berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_ADM_03_POS_access_job_title_list(self):
        """Memastikan halaman daftar Job Title di modul Admin dapat diakses."""
        self._do_login()
        ap = AdminPage(self.driver)
        ap.open_job_title_list()
        self.assertIn("viewJobTitleList", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_ADM_04_NEG: Akses halaman Admin tanpa login
    # ─────────────────────────────────────────────
    def test_TC_ADM_04_NEG_access_admin_without_login(self):
        """Memastikan akses halaman Admin tanpa login diredirect ke halaman login."""
        ap = AdminPage(self.driver)
        ap.open_system_users()
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_ADM_05_POS: Halaman Add System User form berhasil dimuat
    # ─────────────────────────────────────────────
    def test_TC_ADM_05_POS_add_system_user_form_loads(self):
        """Memastikan form tambah System User berhasil dimuat."""
        self._do_login()
        ap = AdminPage(self.driver)
        ap.open_add_user_form()
        self.assertIn("saveSystemUser", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_ADM_06_NEG: Akses halaman Job Title tanpa login
    # ─────────────────────────────────────────────
    def test_TC_ADM_06_NEG_access_job_title_without_login(self):
        """Memastikan akses halaman Job Title tanpa login diredirect ke halaman login."""
        ap = AdminPage(self.driver)
        ap.open_job_title_list()
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)
