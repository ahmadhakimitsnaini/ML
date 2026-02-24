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



