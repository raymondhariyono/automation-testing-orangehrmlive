# tests/test_search.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Global Search (4 Test Case)
# TC_SCH_01_POS  TC_SCH_02_NEG  TC_SCH_03_POS  TC_SCH_04_NEG
# ─────────────────────────────────────────────────────────────

from selenium.webdriver.support import expected_conditions as EC
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.settings import VALID_USER, VALID_PASS


class TestSearch(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_SCH_01_POS: Search global "Leave" menampilkan saran menu
    # ─────────────────────────────────────────────
    def test_TC_SCH_01_POS_global_search_leave_shows_suggestions(self):
        """Memastikan fitur pencarian global menampilkan saran menu yang relevan."""
        self._do_login()
        dp = DashboardPage(self.driver)
        dp.search_global("Leave")
        suggestions = dp.get_search_suggestions()
        self.assertGreater(len(suggestions), 0)

    # ─────────────────────────────────────────────
    # TC_SCH_02_NEG: Search global kata tidak relevan → tidak ada hasil
    # ─────────────────────────────────────────────
    def test_TC_SCH_02_NEG_global_search_irrelevant_keyword_no_result(self):
        """Memastikan pencarian global dengan kata tidak relevan tidak menampilkan menu."""
        self._do_login()
        dp = DashboardPage(self.driver)
        dp.search_global("xyznotexistmenu")
        suggestions = dp.get_search_suggestions()
        self.assertEqual(len(suggestions), 0)

    # ─────────────────────────────────────────────
    # TC_SCH_03_POS: Search global "Admin" menampilkan saran menu Admin
    # ─────────────────────────────────────────────
    def test_TC_SCH_03_POS_global_search_admin_shows_suggestions(self):
        """Memastikan pencarian global kata 'Admin' memunculkan saran menu terkait Admin."""
        self._do_login()
        dp = DashboardPage(self.driver)
        dp.search_global("Admin")
        suggestions = dp.get_search_suggestions()
        self.assertGreater(len(suggestions), 0)

    # ─────────────────────────────────────────────
    # TC_SCH_04_NEG: Search global dengan input angka tidak relevan
    # ─────────────────────────────────────────────
    def test_TC_SCH_04_NEG_global_search_numbers_no_result(self):
        """Memastikan pencarian global dengan input angka tidak menampilkan saran menu."""
        self._do_login()
        dp = DashboardPage(self.driver)
        dp.search_global("99999999")
        suggestions = dp.get_search_suggestions()
        self.assertEqual(len(suggestions), 0)
