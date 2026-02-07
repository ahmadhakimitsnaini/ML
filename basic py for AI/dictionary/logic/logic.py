# EXERCISE PYTHON LOGIC

"""
    Soal 1: Logika Akses (Authentication)
    Buatlah fungsi cek_akses(username, role) yang menerima dua parameter string.

    Jika role adalah "admin", cetak "Akses penuh diberikan".

    Jika role adalah "user" dan username tidak kosong, cetak "Akses terbatas diberikan".

    Selain itu, cetak "Akses ditolak".
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