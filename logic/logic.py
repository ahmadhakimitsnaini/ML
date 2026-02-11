"""
MODULE: PYTHON LOGIC EXERCISES
------------------------------
Deskripsi : Kumpulan latihan logika dasar Python mencakup autentikasi, 
            klasifikasi sensor, perhitungan finansial, dan filtering data.
Author    : [Ahmadhakimitsnaini]
Created   : 2026-02-11
Version   : 1.0.1
"""

# ==============================================================================
# 1. LOGIKA AKSES (AUTHENTICATION)
# ==============================================================================

def cek_akses(username: str, role: str) -> None:
    """
    Memvalidasi hak akses pengguna berdasarkan peran (role).

    Parameters:
        username (str): Nama pengguna.
        role (str): Peran pengguna ('admin' atau 'user').
    """
    # Menggunakan .lower() agar input 'Admin', 'ADMIN', 'admin' dianggap sama
    normalized_role = role.lower()

    if normalized_role == "admin":
        print(f"[ACCESS] Akses penuh diberikan kepada {username}.")
    elif normalized_role == "user" and username:
        print(f"[ACCESS] Akses terbatas diberikan kepada {username}.")
    else:
        print(f"[ACCESS] Akses ditolak untuk {username}.")

# --- Eksekusi Soal 1 ---
print("\n--- SOAL 1: AUTHENTICATION ---")
input_user = input("Masukkan Username      : ")
input_role = input("Masukkan Role Pengguna : ")
cek_akses(input_user, input_role)
cek_akses("Sani", "Admin") # Contoh pemanggilan langsung


# ==============================================================================
# 2. KLASIFIKASI DATA SENSOR
# ==============================================================================

def klasifikasi_suhu(suhu: float) -> str:
    """
    Mengklasifikasikan status berdasarkan input suhu sensor.

    Parameters:
        suhu (float): Nilai suhu dalam derajat celcius.
    
    Returns:
        str: Status suhu ('Membeku', 'Normal', 'Panas', atau 'Rusak').
    """
    if suhu > 100:
        return "Peringatan: Sensor Rusak!"
    elif suhu > 30:
        return "Panas"
    elif 0 <= suhu <= 30:
        return "Normal"
    else:
        # Menangani suhu < 0
        return "Membeku"

# --- Eksekusi Soal 2 ---
print("\n--- SOAL 2: SENSOR DATA ---")
input_suhu = 105 # Contoh input hardcode, bisa diganti input()
status_suhu = klasifikasi_suhu(input_suhu)
print(f"Suhu: {input_suhu}°C -> Status: {status_suhu}")


# ==============================================================================
# 3. LOGIKA DISKON E-COMMERCE
# ==============================================================================

def hitung_harga_akhir(total_belanja: int) -> float:
    """
    Menghitung harga akhir setelah potongan diskon bertingkat.
    
    Aturan Diskon:
    - Belanja > 500rb : Diskon 10%
    - Belanja 200rb - 500rb : Diskon 5%
    - Belanja < 200rb : Tidak ada diskon

    Returns:
        float: Harga akhir yang harus dibayar.
    """
    diskon = 0.0
    
    if total_belanja > 500000:
        diskon = 0.10 # 10%
    elif 200000 <= total_belanja <= 500000:
        diskon = 0.05 # 5% (Note: Kode lama 0.5 itu 50%, sudah dikoreksi)
    
    potongan = total_belanja * diskon
    harga_akhir = total_belanja - potongan
    
    print(f"Total: Rp{total_belanja:,} | Diskon: {int(diskon*100)}% | Bayar: Rp{harga_akhir:,.0f}")
    return harga_akhir

# --- Eksekusi Soal 3 ---
print("\n--- SOAL 3: DISKON SHOPEE ---")
belanjaan = 600000
hitung_harga_akhir(belanjaan)


# ==============================================================================
# 4. TANTANGAN "JUST-IN-TIME" (DATA FILTERING)
# ==============================================================================

def filter_kelulusan(daftar_nilai: list) -> dict:
    """
    Memisahkan nilai mahasiswa menjadi kategori Lulus dan Gagal.
    Threshold kelulusan: > 65.

    Returns:
        dict: Dictionary berisi list 'lulus' dan 'gagal'.
    """
    lulus = []
    gagal = []

    # Cara 1: Standard Loop (Sesuai kode asli Anda)
    for nilai in daftar_nilai:
        if nilai > 65:
            lulus.append(nilai)
        else:
            gagal.append(nilai)
    
    # Cara 2: List Comprehension (Advanced - Sesuai request soal)
    # lulus = [n for n in daftar_nilai if n > 65]
    # gagal = [n for n in daftar_nilai if n <= 65]

    return {"Lulus": lulus, "Gagal": gagal}

# --- Eksekusi Soal 4 ---
print("\n--- SOAL 4: STUDENT GRADES ---")
nilai_praktikum = [60, 80, 45, 90, 70, 55]
hasil_seleksi = filter_kelulusan(nilai_praktikum)

print(f"Data Awal   : {nilai_praktikum}")
print(f"Siswa Lulus : {hasil_seleksi['Lulus']}")
print(f"Siswa Gagal : {hasil_seleksi['Gagal']}")