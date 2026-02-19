"""
PANDAS DASAR: DATAFRAME & OPERASI UMUM
--------------------------------------
Skrip ini mendemonstrasikan:
1. Pembuatan DataFrame dari Dictionary
2. Agregasi (Menghitung rata-rata)
3. Filtering (Penyaringan kondisi)
4. Vectorized Operation (Membuat kolom baru)
"""

import pandas as pd

# ==========================================
# 1. PERSIAPAN DATA & DATAFRAME
# ==========================================
# Membuat DataFrame (struktur tabel mirip Excel) dari Python Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Salary': [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

print("--- Tabel Karyawan ---")
print(df)

# ==========================================
# 2. AGREGASI DATA
# ==========================================
# Menghitung nilai rata-rata dari kolom 'Age' menggunakan .mean()
print("\n--- Rata-rata Umur ---")
average_age = df['Age'].mean()
print(f"Rata-rata umur: {average_age}")

# ==========================================
# 3. FILTERING (PENYARINGAN)
# ==========================================
# Mengambil baris data yang hanya memenuhi kondisi (Umur > 25)
print("\n--- Karyawan > 25 Tahun ---")
older_employees = df[df['Age'] > 25]
print(older_employees)

# ==========================================
# 4. MEMBUAT KOLOM BARU (VECTORIZED)
# ==========================================
# Menghitung bonus 10% dari gaji dan langsung menyimpannya ke kolom baru
print("\n--- Tabel dengan Kolom Bonus Baru ---")
df['Bonus'] = df['Salary'] * 0.10
print(df)