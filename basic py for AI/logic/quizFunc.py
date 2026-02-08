# ------------- QUESTIONS ABOUT FUNCTION -------------

# Bagian 1: Penggunaan Bersama Fungsi Higher-Order
"""
    Transformasi Data (map): Gunakan map() dan lambda untuk 
    mengubah list harga produk berikut menjadi list baru yang sudah ditambah pajak sebesar 10%:
"""
harga_asli = [1000, 2000, 3000, 4000]
new_list = list(map(lambda x : x + (x * 0.1), harga_asli))
print(new_list)


"""
    Penyaringan Data (filter): Diberikan list data sensor suhu: suhu_ruangan = [25, 32, 18, 40, 22, 35]. 
    Gunakan filter() dan lambda untuk mengambil hanya suhu yang di atas 30 derajat saja.
"""
suhu_ruangan = [25, 32, 18, 40, 22, 35]
filterSuhu = list(filter(lambda y : y > 30, suhu_ruangan))  # Using filter for searching number greather than 30
print(filterSuhu)

