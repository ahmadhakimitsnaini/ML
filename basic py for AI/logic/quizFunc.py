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

# Bagian 2: Studi Kasus (Logika AI)
"""
    Sorting Data Kompleks: Diberikan list berisi koordinat titik dalam bentuk tuple :
    titik = [(1, 2), (4, 1), (2, 10), (10, 5)]. 
    Gunakan fungsi sort() atau sorted() bersama dengan lambda sebagai kunci (key) 
    untuk mengurutkan list tersebut berdasarkan elemen kedua (nilai y) dari masing-masing tuple.
"""
titik = [(1, 2), (4, 1), (2, 10), (10, 5)]
sorting = sorted(titik, key = lambda x : x[1])
print(sorting)

