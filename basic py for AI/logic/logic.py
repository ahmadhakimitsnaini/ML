# EXERCISE PYTHON LOGIC

# Soal 1: Logika Akses (Authentication)
"""
    1. Buatlah fungsi cek_akses(username, role) yang menerima dua parameter string.
    2. Jika role adalah "admin", cetak "Akses penuh diberikan".
    3. Jika role adalah "user" dan username tidak kosong, cetak "Akses terbatas diberikan".
    4. Selain itu, cetak "Akses ditolak".
       (Latihan ini relevan untuk rencana Anda membangun sistem login atau dashboard e-commerce)
"""

username = str(input("Masukkan Username       : "))
role =     str(input ("Masukkan Role Pengguna  : "))
def auth(username, role) : 
    if role == "Admin" or role == "admin" :
        print("Akses penuh diberikan")
    elif role == "user" or role == "User" : 
        print("Akses Terbatas Di Berikan")
    else :
        print("Akses Di Tolak")

auth(username, role)


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


# Soal 3: Logika Diskon Shopee
"""
    Bayangkan Anda sedang mengatur logika untuk toko "alwaystous" di Shopee. Buat fungsi hitung_harga(total_belanja):

    1. Jika belanja lebih dari Rp500.000, berikan diskon 10%. 
    2. Jika belanja antara Rp200.000 - Rp500.000, berikan diskon 5%.
    3. Jika di bawah Rp200.000, tidak ada diskon.

    Kembalikan nilai harga akhir yang harus dibayar.
"""
def hitung_harga(totalBelanja) : 
    if totalBelanja > 500000 : 
        harga = totalBelanja - (totalBelanja * 0.10) # Rumus mencari diskon 
        print(harga)
    elif totalBelanja >= 200000 and totalBelanja <= 500000 : 
        harga = totalBelanja - (totalBelanja * 0.5)
        print(harga)
    elif totalBelanja < 200000 : 
        harga = totalBelanja
        print(harga)
    else : 
        print("Tidak ada diskon yang tersedia")
    
belanjaan = 600000
print(hitung_harga(belanjaan))


# 4. Tantangan "Just-in-Time" (Advanced)
"""
    Soal: Diberikan list nilai mahasiswa nilai_praktikum = [60, 80, 45, 90, 70, 55].
    Buatlah list baru berisi status "Lulus" jika nilai > 65 dan "Gagal" jika nilai < 65.
    Gunakan List Comprehension seperti pada jawaban nomor 4 sebelumnya.
"""
nilai_praktikum = [60, 80, 45, 90, 70, 55]
lulus = []
gagal = []
for x in nilai_praktikum : 
    if x >= 65 : 
        lulus.append(x) # append method use for add item to list
        
    elif x <= 65 : 
        gagal.append(x)
        
print(f"Nilai yang lulus = {lulus}")
print(f"Nilai yang gagal = {gagal}")