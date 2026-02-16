# ---------------------------------------------------------
# LANGKAH 0: IMPORT LIBRARY
# ---------------------------------------------------------
# Kita mengimpor library pandas dan memberinya nama alias 'pd'.
# Alias ini memudahkan kita agar tidak perlu mengetik 'pandas' terus-menerus.
import pandas as pd

# ---------------------------------------------------------
# LANGKAH 1: PERSIAPAN DATA (DATA PREPARATION)
# ---------------------------------------------------------
# Kita membuat data mentah menggunakan Python Dictionary.
# - 'Key' (kiri) akan menjadi Nama Kolom (Header).
# - 'Value' (kanan) adalah List yang menjadi baris data.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [50000, 60000, 55000, 70000]
}

# ---------------------------------------------------------
# LANGKAH 2: MEMBUAT DATAFRAME
# ---------------------------------------------------------
# Fungsi pd.DataFrame() mengubah dictionary di atas menjadi tabel terstruktur.
# DataFrame adalah struktur data utama Pandas (mirip lembar kerja Excel).
df = pd.DataFrame(data)

# ---------------------------------------------------------
# LANGKAH 3: MENAMPILKAN DATA
# ---------------------------------------------------------
print("--- Tabel Karyawan (DataFrame) ---")
# Mencetak seluruh tabel ke layar.
print(df)

# ---------------------------------------------------------
# LANGKAH 4: OPERASI DATA DASAR
# ---------------------------------------------------------

# A. Agregasi (Menghitung Rata-rata)
print("\n--- Rata-rata Umur ---")
# df['Age'] memilih kolom 'Age'.
# .mean() adalah fungsi statistik bawaan untuk menghitung rata-rata.
average_age = df['Age'].mean()
print(f"Rata-rata umur adalah: {average_age}")

# B. Filtering (Menyaring Data)
print("\n--- Filter: Karyawan di atas 25 tahun ---")
# Logika Filtering:
# 1. df['Age'] > 25 menghasilkan serangkaian True/False.
# 2. df[...] membungkus kondisi tersebut untuk hanya menampilkan baris yang True.
older_employees = df[df['Age'] > 25]
print(older_employees)

# C. Menambah Kolom Baru (Vectorized Operation)
print("\n--- Menambah Kolom Baru (Bonus) ---")
# Kita tidak perlu menggunakan "For Loop".
# Pandas memungkinkan kita mengalikan seluruh kolom 'Salary' dengan 0.10 sekaligus.
# Hasilnya langsung dimasukkan ke kolom baru bernama 'Bonus'.
df['Bonus'] = df['Salary'] * 0.10

# Tampilkan hasil akhir tabel yang sudah dimodifikasi
print(df)