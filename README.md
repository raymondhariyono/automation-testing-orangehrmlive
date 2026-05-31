# 🧪 OrangeHRM Regression Test — Automation Testing with Selenium

> Tugas 5 Individu — Pengujian dan Penjaminan Kualitas Perangkat Lunak
> **Raymond Hariyono** | NIM 2310817210007 | 2026

---

## 📋 Deskripsi

Repository ini berisi automation regression test untuk aplikasi **OrangeHRM Demo**
(`https://opensource-demo.orangehrmlive.com`) menggunakan **Python** dan **Selenium WebDriver**.

Pengujian mencakup **40 skenario (20 skenario × positif + negatif)** yang meliputi modul:
Login, Employee Management, Leave, Admin, Search, Profile, Reports, dan Time.

Proyek ini menggunakan arsitektur **Page Object Model (POM)** dengan struktur modular per-modul
sehingga kode bersih, mudah dimaintain, dan mudah dikembangkan.

---

## 🗂️ Struktur Project

```
orangehrm-regression-test/
│
├── config/
│   ├── __init__.py
│   └── settings.py             # Konstanta global (URL, kredensial, timeout)
│
├── pages/                      # Page Object Model — satu file per halaman
│   ├── __init__.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── employee_page.py
│   ├── leave_page.py
│   ├── admin_page.py
│   ├── profile_page.py
│   ├── reports_page.py
│   └── time_page.py
│
├── tests/                      # Test case — satu file per modul
│   ├── __init__.py
│   ├── test_login.py           # 8 test case (Login & Auth)
│   ├── test_employee.py        # 8 test case (Employee Management)
│   ├── test_leave.py           # 6 test case (Leave)
│   ├── test_admin.py           # 6 test case (Admin)
│   ├── test_search.py          # 4 test case (Global Search)
│   ├── test_profile.py         # 4 test case (Profile / My Info)
│   ├── test_reports.py         # 4 test case (Reports)
│   └── test_time.py            # 4 test case (Time & Attendance)
│  (total: 40 test case)
│
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py       # Factory untuk WebDriver Chrome
│   └── base_test.py            # Base class dengan setUp/tearDown
│
├── requirements.txt
└── README.md
```

---

## ✅ Daftar 40 Test Case

### 🔐 Login & Autentikasi — `tests/test_login.py` (8 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 1  | TC_LGN_01_POS   | Positif  | Login dengan kredensial valid → masuk Dashboard          |
| 2  | TC_LGN_02_NEG   | Negatif  | Login password salah → muncul "Invalid credentials"      |
| 3  | TC_LGN_03_NEG   | Negatif  | Login semua field kosong → muncul validasi "Required"    |
| 4  | TC_LGN_04_POS   | Positif  | Logout berhasil → diarahkan ke halaman login             |
| 5  | TC_LGN_05_NEG   | Negatif  | Akses dashboard tanpa login → redirect ke login          |
| 6  | TC_LGN_06_POS   | Positif  | Setelah login URL dashboard valid dan HTTPS              |
| 7  | TC_LGN_07_NEG   | Negatif  | Login username tidak terdaftar → "Invalid credentials"   |
| 8  | TC_LGN_08_NEG   | Negatif  | Login hanya isi username, password kosong → validasi     |

### 👤 Employee Management — `tests/test_employee.py` (8 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 9  | TC_EMP_01_POS   | Positif  | Tambah employee data lengkap → berhasil tersimpan        |
| 10 | TC_EMP_02_NEG   | Negatif  | Tambah employee tanpa First Name → validasi muncul       |
| 11 | TC_EMP_03_POS   | Positif  | Cari employee yang ada → hasil ditemukan                 |
| 12 | TC_EMP_04_NEG   | Negatif  | Cari employee tidak ada → "No Records Found"             |
| 13 | TC_EMP_05_POS   | Positif  | Halaman Employee List berhasil dimuat                    |
| 14 | TC_EMP_06_NEG   | Negatif  | Submit form employee semua field kosong → validasi       |
| 15 | TC_EMP_07_POS   | Positif  | Halaman Add Employee form berhasil diakses               |
| 16 | TC_EMP_08_NEG   | Negatif  | Search employee dengan karakter spesial → tidak crash    |

### 🗓️ Leave Management — `tests/test_leave.py` (6 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 17 | TC_LVE_01_POS   | Positif  | Halaman Leave List berhasil diakses                      |
| 18 | TC_LVE_02_NEG   | Negatif  | Apply leave tanggal End < Start → ditolak sistem         |
| 19 | TC_LVE_03_POS   | Positif  | URL halaman Leave List benar                             |
| 20 | TC_LVE_04_NEG   | Negatif  | Apply leave tanpa Leave Type → validasi muncul           |
| 21 | TC_LVE_05_POS   | Positif  | Halaman Apply Leave berhasil diakses                     |
| 22 | TC_LVE_06_NEG   | Negatif  | Akses Leave tanpa login → redirect ke login              |

### ⚙️ Admin & User Management — `tests/test_admin.py` (6 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 23 | TC_ADM_01_POS   | Positif  | Halaman System Users berhasil diakses                    |
| 24 | TC_ADM_02_NEG   | Negatif  | Tambah user semua field kosong → validasi muncul         |
| 25 | TC_ADM_03_POS   | Positif  | Halaman Job Titles berhasil diakses                      |
| 26 | TC_ADM_04_NEG   | Negatif  | Akses Admin tanpa login → redirect ke login              |
| 27 | TC_ADM_05_POS   | Positif  | Form Add System User berhasil dimuat                     |
| 28 | TC_ADM_06_NEG   | Negatif  | Akses Job Title tanpa login → redirect ke login          |

### 🔍 Global Search — `tests/test_search.py` (4 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 29 | TC_SCH_01_POS   | Positif  | Search "Leave" → saran menu muncul                       |
| 30 | TC_SCH_02_NEG   | Negatif  | Search kata tidak relevan → tidak ada saran menu         |
| 31 | TC_SCH_03_POS   | Positif  | Search "Admin" → saran menu Admin muncul                 |
| 32 | TC_SCH_04_NEG   | Negatif  | Search angka acak → tidak ada saran menu                 |

### 🧑 Profile / My Info — `tests/test_profile.py` (4 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 33 | TC_PRF_01_POS   | Positif  | Halaman My Info berhasil diakses                         |
| 34 | TC_PRF_02_NEG   | Negatif  | Simpan profil tanpa First Name → validasi muncul         |
| 35 | TC_PRF_03_POS   | Positif  | Header halaman My Info terisi dengan benar               |
| 36 | TC_PRF_04_NEG   | Negatif  | Akses My Info tanpa login → redirect ke login            |

### 📊 Reports — `tests/test_reports.py` (4 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 37 | TC_RPT_01_POS   | Positif  | Halaman PIM Reports berhasil diakses                     |
| 38 | TC_RPT_02_NEG   | Negatif  | Tambah report tanpa Report Name → validasi muncul        |
| 39 | TC_RPT_03_POS   | Positif  | Header halaman Reports valid                             |
| 40 | TC_RPT_04_NEG   | Negatif  | Akses Reports tanpa login → redirect ke login            |

### ⏱️ Time & Attendance — `tests/test_time.py` (4 Test)

| No | TestCase ID     | Tipe     | Deskripsi Singkat                                        |
|----|-----------------|----------|----------------------------------------------------------|
| 41 | TC_TIM_01_POS   | Positif  | Halaman Employee Timesheet berhasil diakses              |
| 42 | TC_TIM_02_NEG   | Negatif  | Submit Project Report form kosong → validasi muncul      |
| 43 | TC_TIM_03_POS   | Positif  | Header halaman Timesheet valid                           |
| 44 | TC_TIM_04_NEG   | Negatif  | Akses Timesheet tanpa login → redirect ke login          |

---

## ⚙️ Setup & Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/<username>/orangehrm-regression-test.git
cd orangehrm-regression-test
```

### 2. Install Dependensi

```bash
pip install -r requirements.txt
```

### 3. Pastikan ChromeDriver Terinstall

Gunakan `webdriver-manager` agar versi ChromeDriver otomatis menyesuaikan Chrome:

```bash
pip install webdriver-manager
```

Lalu update `utils/driver_factory.py`:

```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver
```

### 4. Jalankan Semua Test (40 Test Case)

```bash
python -m pytest tests/ -v
```

### 5. Jalankan Per Modul

```bash
python -m pytest tests/test_login.py    -v   # Login (8 test)
python -m pytest tests/test_employee.py -v   # Employee (8 test)
python -m pytest tests/test_leave.py    -v   # Leave (6 test)
python -m pytest tests/test_admin.py    -v   # Admin (6 test)
python -m pytest tests/test_search.py   -v   # Search (4 test)
python -m pytest tests/test_profile.py  -v   # Profile (4 test)
python -m pytest tests/test_reports.py  -v   # Reports (4 test)
python -m pytest tests/test_time.py     -v   # Time (4 test)
```

### 6. Filter Positif / Negatif

```bash
python -m pytest tests/ -k "POS" -v   # Semua skenario Positif
python -m pytest tests/ -k "NEG" -v   # Semua skenario Negatif
```

### 7. Generate Laporan HTML

```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

---

## 🔧 Konfigurasi

### Mode Visual (non-headless)

Edit `config/settings.py`:

```python
HEADLESS = False  # Ganti True menjadi False
```

### Kredensial & URL

Ubah di `config/settings.py`:

```python
BASE_URL   = "https://opensource-demo.orangehrmlive.com/web/index.php"
VALID_USER = "Admin"
VALID_PASS = "admin123"
```

---

## 🏛️ Arsitektur Page Object Model (POM)

```
config/settings.py      ← semua konstanta di satu tempat
utils/driver_factory.py ← cara membuat WebDriver
utils/base_test.py      ← setUp/tearDown untuk semua test
pages/*.py              ← interaksi per halaman (locator + metode)
tests/*.py              ← assertion & skenario test
```

Keuntungan arsitektur ini:
- **Modular**: setiap file punya tanggung jawab tunggal
- **DRY**: locator dan aksi halaman hanya ditulis sekali di `pages/`
- **Mudah dimaintain**: jika UI berubah, cukup update file `pages/` yang relevan
- **Scalable**: tambah modul baru cukup buat `pages/modul_page.py` + `tests/test_modul.py`

---

## 👤 Author

**Raymond Hariyono**
NIM: 2310817210007
Mata Kuliah: Pengujian dan Penjaminan Kualitas Perangkat Lunak
Tahun: 2026
