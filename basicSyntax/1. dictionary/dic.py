# ==========================================
# DICTIONARY (Kamus Data)
# ==========================================
# Dictionary digunakan untuk menyimpan data dalam pasangan key:value.
# Sifatnya: Unordered (sebelum Python 3.7), Changeable, dan No Duplicates.

thisCar = {
    "brand" : "bmw",
    "color" : "Black",
    "engine" : "V3"
}
# print(thisCar["brand"])

# ------------------------------------------
# 1. Mengakses Item (Accessing Items)
# ------------------------------------------
# Cara 1: Menggunakan kurung siku []
x = thisCar["brand"] 

# Cara 2: Menggunakan method .get()
# Kelebihannya: Jika key tidak ditemukan, ia tidak akan error, melainkan return None.
x = thisCar.get("brand") 

# ------------------------------------------
# 2. Melihat & Mengubah Data
# ------------------------------------------
# Mengambil daftar pasangan (key, value) sebagai view object
x = thisCar.items()

# Mengubah value dari key yang sudah ada
thisCar["engine"] = "V5"

# Menambah key baru dan value-nya
thisCar["Country"] = "Europe"

# ------------------------------------------
# 3. Cek Keberadaan Key (Check Key Existence)
# ------------------------------------------
if "brand" in thisCar :
    print("Key 'brand' tersedia di dalam dictionary")

# ------------------------------------------
# 4. Update Dictionary
# ------------------------------------------
biodata = {
    "nama" : "ahmadhakimitsnaini",
    "umur" : 20,
    "universitas" : "politeknik negeri madiun"
}

# .update() bisa untuk mengedit data lama ATAU menambah data baru
biodata.update({"universitas" : "Politeknik Negeri Madiun"}) # Memperbaiki kapitalisasi
biodata["nama"] = "Ahmad Hakim Itsnaini" # Cara langsung

# ------------------------------------------
# 5. Menambah & Menghapus Item
# ------------------------------------------
# Menambah item baru
biodata["job"] = "Data Science"

# Menghapus item spesifik menggunakan .pop() (mengembalikan value yang dihapus)
biodata.pop("job")

# Menambah lagi untuk contoh penghapusan berikutnya
biodata.update({"job" : "Data Science"})

# Menghapus item terakhir yang dimasukkan (LIFO - Last In First Out)
# biodata.popitem() 

# Menghapus item spesifik menggunakan keyword del
del biodata["job"]

# Menghapus seluruh dictionary dari memori (akan error jika dipanggil setelah ini)
# del biodata 

# ------------------------------------------
# 6. Looping Dictionary
# ------------------------------------------
# Melakukan iterasi untuk mendapatkan key (x) dan value (y)
for x, y in biodata.items() : 
    print(x , y)