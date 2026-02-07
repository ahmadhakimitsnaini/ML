# EXERCISE PYTHON LOGIC

# Soal 1: Logika Akses (Authentication)
"""
    1. Buatlah fungsi cek_akses(username, role) yang menerima dua parameter string.
    2. Jika role adalah "admin", cetak "Akses penuh diberikan".
    3. Jika role adalah "user" dan username tidak kosong, cetak "Akses terbatas diberikan".
    4. Selain itu, cetak "Akses ditolak".
       (Latihan ini relevan untuk rencana Anda membangun sistem login atau dashboard e-commerce)
"""

# username = str(input("Masukkan Username       : "))
# role =     str(input ("Masukkan Role Pengguna  : "))
def auth(username, role) : 
    if role == "Admin" or role == "admin" :
        print("Akses penuh diberikan")
    elif role == "user" or role == "User" : 
        print("Akses Terbatas Di Berikan")
    else :
        print("Akses Di Tolak")

# auth(username, role)


# Soal 2: Klasifikasi Data Sensor
"""
    Dalam proyek IT, seringkali kita menerima data sensor. Buatlah logika untuk mengklasifikasikan suhu:

    1. Suhu < 0     : "Membeku"
    2. Suhu 0 - 30  : "Normal"
    3. Suhu > 30    : "Panas"
    Tambahkan pengecekan: Jika suhu di atas 100, cetak "Peringatan: Sensor Rusak!".
"""
inputSuhu = int(input ("Masukkan suhu : "))
if inputSuhu < 0 :
    print("Membeku")
elif inputSuhu <= 30 :
    print("Normal")
elif inputSuhu >= 30 and inputSuhu <= 100 :
    print("Panas")
elif inputSuhu > 100:
    print("Peringatan : Sensor Rusak!")
else : 
    print("Maaf suhu tidak terdeteksi")