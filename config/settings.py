# config/settings.py
# ─────────────────────────────────────────────────────────────
# Konfigurasi global untuk OrangeHRM Regression Test Suite
# ─────────────────────────────────────────────────────────────

BASE_URL    = "https://opensource-demo.orangehrmlive.com/web/index.php"
LOGIN_URL   = f"{BASE_URL}/auth/login"
DASHBOARD_URL = f"{BASE_URL}/dashboard/index"

VALID_USER  = "Admin"
VALID_PASS  = "admin123"

# Timeout (detik)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15

# Mode headless (True = tanpa tampilan browser)
HEADLESS = True
