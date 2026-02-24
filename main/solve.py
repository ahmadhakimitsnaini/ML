"""
TANTANGAN LOGIKA MACHINE LEARNING
Topik: Algoritma 1-Nearest Neighbor (Mencari Tetangga Terdekat)
"""

import math

print("=== PROGRAM AI TEBAK STATUS TANAMAN ===")

# 1. DATASET (Data Historis/Latih)
# Format: [Suhu, Kelembaban], "Status"
data_historis = [
    ([28.0, 60.0], "Sehat"),
    ([36.0, 30.0], "Sakit"),
    ([29.5, 55.0], "Sehat"),
    ([38.0, 25.0], "Sakit")
]

# 2. DATA BARU (Data sensor yang baru masuk dan belum tahu statusnya)
sensor_baru = [35.0, 32.0]

# =====================================================================
# TUGAS 1: Buat fungsi untuk menghitung jarak antara 2 titik
# Rumus Euclidean Distance: Akar dari ((suhu1 - suhu2)^2 + (kel1 - kel2)^2)
# =====================================================================
def hitung_jarak(titik1, titik2):
    suhu1, kel1 = titik1
    suhu2, kel2 = titik2
    
    # TODO 1: Tulis rumus matematika di bawah ini untuk mencari jarak!
    # Gunakan math.sqrt() untuk akar kuadrat, dan ** 2 untuk pangkat dua.
    jarak = 0.0 # <--- UBAH BARIS INI
    
    return jarak


# =====================================================================
# TUGAS 2: Cari data historis mana yang jaraknya PALING DEKAT
# =====================================================================
def tebak_status(data_baru, dataset):
    jarak_terdekat = float('inf') # Set jarak awal dengan nilai tak terhingga
    tebakan_terbaik = "Belum tahu"
    
    # Looping satu per satu data di dalam dataset
    for data in dataset:
        titik_lama = data[0]  # Mengambil list [Suhu, Kelembaban]
        label_lama = data[1]  # Mengambil teks "Sehat" atau "Sakit"
        
        # Panggil fungsi hitung_jarak yang sudah kamu buat di Tugas 1
        jarak_sekarang = hitung_jarak(data_baru, titik_lama)
        
        print(f"Jarak ke {label_lama} ({titik_lama}): {jarak_sekarang:.2f}")
        
        # TODO 2: Buat logika IF (Jika) di sini!
        # JIKA jarak_sekarang LEBIH KECIL dari jarak_terdekat, maka:
        # 1. Ubah jarak_terdekat menjadi jarak_sekarang
        # 2. Ubah tebakan_terbaik menjadi label_lama
        
        # --- Penulisan logic if ---
        
        
    return tebakan_terbaik
