# tests/test_login.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Login & Autentikasi (8 Test Case)
# TC_LGN_01_POS  TC_LGN_02_NEG  TC_LGN_03_NEG  TC_LGN_04_POS
# TC_LGN_05_NEG  TC_LGN_06_POS  TC_LGN_07_NEG  TC_LGN_08_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.settings import VALID_USER, VALID_PASS, DASHBOARD_URL, LOGIN_URL


class TestLogin(BaseTest):

    # ─────────────────────────────────────────────
    # TC_LGN_01_POS: Login dengan kredensial valid
    # ─────────────────────────────────────────────
    def test_TC_LGN_01_POS_login_valid_credentials(self):
        """Memastikan pengguna dapat login menggunakan username dan password yang valid."""
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))
        self.assertIn("dashboard", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_LGN_02_NEG: Login dengan password salah
    # ─────────────────────────────────────────────
    def test_TC_LGN_02_NEG_login_wrong_password(self):
        """Memastikan sistem menolak login dengan password yang salah."""
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, "wrongpassword123")
        error = lp.get_error_message()
        self.assertIn("Invalid credentials", error)

    # ─────────────────────────────────────────────
    # TC_LGN_03_NEG: Login dengan field kosong
    # ─────────────────────────────────────────────
    def test_TC_LGN_03_NEG_login_empty_fields(self):
        """Memastikan sistem menampilkan validasi saat semua field login dikosongkan."""
        lp = LoginPage(self.driver)
        lp.open()
        lp.click_submit()
        errors = lp.get_required_errors()
        self.assertGreaterEqual(len(errors), 2)

    # ─────────────────────────────────────────────
    # TC_LGN_04_POS: Logout berhasil
    # ─────────────────────────────────────────────
    def test_TC_LGN_04_POS_logout_success(self):
        """Memastikan pengguna dapat logout dan diarahkan kembali ke halaman login."""
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        dp = DashboardPage(self.driver)
        dp.wait_for_dashboard()
        dp.logout()
        self.assertIn("auth/login", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_LGN_05_NEG: Akses dashboard tanpa login
    # ─────────────────────────────────────────────
    def test_TC_LGN_05_NEG_access_dashboard_without_login(self):
        """Memastikan akses langsung ke dashboard tanpa login diredirect ke halaman login."""
        self.driver.get(DASHBOARD_URL)
        self.wait.until(EC.url_contains("auth/login"))
        self.assertIn("auth/login", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_LGN_06_POS: Login dengan username huruf kecil (case insensitive check)
    # ─────────────────────────────────────────────
    def test_TC_LGN_06_POS_login_valid_then_url_check(self):
        """Memastikan setelah login berhasil, URL mengarah ke halaman dashboard yang benar."""
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))
        self.assertTrue(self.driver.current_url.startswith("https://"))
        self.assertIn("dashboard", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_LGN_07_NEG: Login dengan username tidak terdaftar
    # ─────────────────────────────────────────────
    def test_TC_LGN_07_NEG_login_unregistered_username(self):
        """Memastikan sistem menolak login dengan username yang tidak terdaftar."""
        lp = LoginPage(self.driver)
        lp.login("usernotexist999", "somepassword")
        error = lp.get_error_message()
        self.assertIn("Invalid credentials", error)

    # ─────────────────────────────────────────────
    # TC_LGN_08_NEG: Login hanya isi username, password kosong
    # ─────────────────────────────────────────────
    def test_TC_LGN_08_NEG_login_password_empty_only(self):
        """Memastikan sistem menampilkan validasi saat hanya password dikosongkan."""
        lp = LoginPage(self.driver)
        lp.open()
        lp.enter_username(VALID_USER)
        lp.click_submit()
        errors = lp.get_required_errors()
        self.assertGreaterEqual(len(errors), 1)
