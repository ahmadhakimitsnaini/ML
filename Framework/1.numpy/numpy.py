"""
PANDUAN DASAR NUMPY
-------------------
Skrip ini mendemonstrasikan operasi dasar:
1. Pembuatan Array
2. Operasi Matematika (Broadcasting)
3. Statistik Dasar
4. Reshaping (Mengubah Dimensi)
"""

import numpy as np

# ==============================
# 1. MEMBUAT ARRAY
# ==============================
# Membuat array dari list Python biasa
data = np.array([10, 20, 30, 40, 50])
print("Array Asli:", data)


# ==============================
# 2. OPERASI MATEMATIKA
# ==============================
# Operasi langsung diterapkan ke SEMUA elemen (tanpa looping)
print("Ditambah 5:", data + 5)
print("Dikali 2  :", data * 2)


# ==============================
# 3. STATISTIK DASAR
# ==============================
print("Rata-rata:", np.mean(data))
print("Maksimum :", np.max(data))
print("Minimum  :", np.min(data))
print("Total    :", np.sum(data))


# ==============================
# 4. RESHAPING (UBAH DIMENSI)
# ==============================
# Membuat angka 0-9, lalu diubah jadi matrix 2 Baris x 5 Kolom
matrix = np.arange(10).reshape(2, 5)
print("Matrix 2x5:\n", matrix)