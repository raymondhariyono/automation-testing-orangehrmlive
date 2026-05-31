# tests/test_profile.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Profile / My Info (4 Test Case)
# TC_PRF_01_POS  TC_PRF_02_NEG  TC_PRF_03_POS  TC_PRF_04_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from config.settings import VALID_USER, VALID_PASS


class TestProfile(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_PRF_01_POS: Halaman My Info berhasil diakses
    # ─────────────────────────────────────────────
    def test_TC_PRF_01_POS_my_info_page_accessible(self):
        """Memastikan halaman My Info (profil pengguna) dapat diakses setelah login."""
        self._do_login()
        pp = ProfilePage(self.driver)
        pp.open_my_info()
        self.assertIn("viewMyDetails", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_PRF_02_NEG: Simpan profil dengan First Name kosong → validasi muncul
    # ─────────────────────────────────────────────
    def test_TC_PRF_02_NEG_save_profile_empty_firstname(self):
        """Memastikan sistem menolak penyimpanan profil jika field First Name dikosongkan."""
        self._do_login()
        pp = ProfilePage(self.driver)
        pp.open_my_info()
        pp.clear_first_name()
        pp.save()
        errors = pp.get_required_errors()
        self.assertGreater(len(errors), 0)

    # ─────────────────────────────────────────────
    # TC_PRF_03_POS: Header halaman My Info terisi dengan benar
    # ─────────────────────────────────────────────
    def test_TC_PRF_03_POS_my_info_has_valid_header(self):
        """Memastikan halaman My Info memiliki header yang valid dan tidak kosong."""
        self._do_login()
        pp = ProfilePage(self.driver)
        pp.open_my_info()
        header = pp.get_header_text()
        self.assertTrue(len(header) > 0)

    # ─────────────────────────────────────────────
    # TC_PRF_04_NEG: Akses My Info tanpa login → redirect ke login
    # ─────────────────────────────────────────────
    def test_TC_PRF_04_NEG_access_my_info_without_login(self):
        """Memastikan akses halaman My Info tanpa login diredirect ke halaman login."""
        pp = ProfilePage(self.driver)
        pp.open_my_info()
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)
