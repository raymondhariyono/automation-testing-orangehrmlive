# tests/test_employee.py
# ─────────────────────────────────────────────────────────────
# Modul Test: Employee Management / PIM (8 Test Case)
# TC_EMP_01_POS  TC_EMP_02_NEG  TC_EMP_03_POS  TC_EMP_04_NEG
# TC_EMP_05_POS  TC_EMP_06_NEG  TC_EMP_07_POS  TC_EMP_08_NEG
# ─────────────────────────────────────────────────────────────

from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.employee_page import EmployeePage
from config.settings import VALID_USER, VALID_PASS


class TestEmployee(BaseTest):

    def _do_login(self):
        lp = LoginPage(self.driver)
        lp.login(VALID_USER, VALID_PASS)
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.url_contains("dashboard"))

    # ─────────────────────────────────────────────
    # TC_EMP_01_POS: Tambah employee dengan data lengkap
    # ─────────────────────────────────────────────
    def test_TC_EMP_01_POS_add_employee_with_full_data(self):
        """Memastikan admin dapat menambahkan data employee baru dengan data lengkap."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_add_form()
        ep.fill_first_name("Raymond")
        ep.fill_last_name("TestUser")
        ep.submit()
        self.assertIn("viewPersonalDetails", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_EMP_02_NEG: Tambah employee tanpa First Name
    # ─────────────────────────────────────────────
    def test_TC_EMP_02_NEG_add_employee_empty_firstname(self):
        """Memastikan sistem menolak penambahan employee jika First Name dikosongkan."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_add_form()
        ep.fill_last_name("TestOnly")
        ep.submit()
        errors = ep.get_required_errors()
        self.assertGreater(len(errors), 0)

    # ─────────────────────────────────────────────
    # TC_EMP_03_POS: Cari employee yang ada di sistem
    # ─────────────────────────────────────────────
    def test_TC_EMP_03_POS_search_existing_employee(self):
        """Memastikan fitur pencarian employee menampilkan hasil yang sesuai."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_list()
        ep.search_employee("Admin")
        rows = ep.get_result_rows()
        self.assertGreater(len(rows), 0)

    # ─────────────────────────────────────────────
    # TC_EMP_04_NEG: Cari employee yang tidak ada
    # ─────────────────────────────────────────────
    def test_TC_EMP_04_NEG_search_nonexistent_employee(self):
        """Memastikan sistem menampilkan 'No Records Found' saat employee tidak ada."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_list()
        ep.search_employee("XYZNOTEXIST999")
        no_record = ep.get_no_records_element()
        self.assertIsNotNone(no_record)

    # ─────────────────────────────────────────────
    # TC_EMP_05_POS: Halaman Employee List berhasil dimuat
    # ─────────────────────────────────────────────
    def test_TC_EMP_05_POS_employee_list_page_loads(self):
        """Memastikan halaman daftar employee berhasil dimuat setelah login."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_list()
        self.assertIn("viewEmployeeList", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_EMP_06_NEG: Tambah employee dengan First Name dan Last Name keduanya kosong
    # ─────────────────────────────────────────────
    def test_TC_EMP_06_NEG_add_employee_all_fields_empty(self):
        """Memastikan sistem menolak penambahan employee jika semua field wajib kosong."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_add_form()
        ep.submit()
        errors = ep.get_required_errors()
        self.assertGreaterEqual(len(errors), 1)

    # ─────────────────────────────────────────────
    # TC_EMP_07_POS: Halaman Add Employee form berhasil dimuat
    # ─────────────────────────────────────────────
    def test_TC_EMP_07_POS_add_employee_form_loads(self):
        """Memastikan form tambah employee berhasil diakses dan field tersedia."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_add_form()
        self.assertIn("addEmployee", self.driver.current_url)

    # ─────────────────────────────────────────────
    # TC_EMP_08_NEG: Search employee dengan input spesial karakter
    # ─────────────────────────────────────────────
    def test_TC_EMP_08_NEG_search_employee_special_characters(self):
        """Memastikan pencarian employee dengan karakter spesial tidak menghasilkan error."""
        self._do_login()
        ep = EmployeePage(self.driver)
        ep.open_list()
        ep.search_employee("!@#$%^&*()")
        # Tidak boleh crash — halaman harus tetap ada atau tampil No Records
        self.assertIn("viewEmployeeList", self.driver.current_url)
