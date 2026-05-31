# utils/base_test.py
# ─────────────────────────────────────────────────────────────
# Base class untuk semua test — setUp, tearDown, dan helper wait
# ─────────────────────────────────────────────────────────────

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from utils.driver_factory import get_driver
from config.settings import EXPLICIT_WAIT


class BaseTest(unittest.TestCase):
    """Base test class yang menyediakan driver dan WebDriverWait."""

    def setUp(self):
        self.driver = get_driver()
        self.wait = WebDriverWait(self.driver, EXPLICIT_WAIT)

    def tearDown(self):
        self.driver.quit()
