# EXERCISE LIST IN PYTHON

# Level 1: Dasar & Slicing

# Question Number 1
"""
    1. Tiga nilai pertama.
    2. Dua nilai terakhir.
    3. Nilai yang berada tepat di tengah (angka 65).
"""
nilai = [70, 85, 90, 65, 80, 95, 100]

print(nilai[:3])
print(nilai[-2 :])
print(nilai[3])

# Question Number 2
"""
    Balik Urutan: Buatlah fungsi yang menerima list nama streetwear 
    (misal: ['Off-White', 'Stussy', 'Supreme']) dan 
    mengembalikannya dalam urutan terbalik tanpa menggunakan fungsi .reverse().
"""
def reverseBrand(brand):
    return brand[::-1]

Brand = ["off white", "vans", "Nike", "Adidas", "New Balance"]
print(reverseBrand(Brand))


# Level 2: Logika & Transformasi

# Question Number 3
"""
    Normalisasi Sederhana: Dalam AI, kita sering mengubah skala data. 
    Diberikan list data = [10, 20, 30, 40, 50]. 
    Buatlah list baru di mana setiap elemennya dibagi dengan nilai maksimal (50).

    Hasil yang diharapkan: [0.2, 0.4, 0.6, 0.8, 1.0].
"""
data = [10, 20, 30, 40, 50]
maxData = max(data)
dataFinal = []

for x in data :
    divided = x / maxData
    dataFinal.append(divided)

print(dataFinal)

# Question Number 4
"""
    Filter Data Ganjil: Buatlah fungsi yang menerima list angka dan hanya mengembalikan
    angka-angka yang genap saja menggunakan List Comprehension.
"""
def filterAngka(filterData) : 
    return [y for y in filterData if y % 2 == 0]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filterAngka(data))
    







