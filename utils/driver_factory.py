# utils/driver_factory.py
# ─────────────────────────────────────────────────────────────
# Factory untuk membuat instance WebDriver Chrome
# ─────────────────────────────────────────────────────────────

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import IMPLICIT_WAIT, HEADLESS


def get_driver() -> webdriver.Chrome:
    """Membuat dan mengembalikan instance Chrome WebDriver."""
    options = Options()
    if HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    return driver
