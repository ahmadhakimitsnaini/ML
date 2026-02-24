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