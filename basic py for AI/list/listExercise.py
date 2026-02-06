# EXERCISE LIST IN PYTHON

# Question number 1
"""
    1. Tiga nilai pertama.
    2. Dua nilai terakhir.
    3. Nilai yang berada tepat di tengah (angka 65).
"""
nilai = [70, 85, 90, 65, 80, 95, 100]

print(nilai[:3])
print(nilai[-2 :])
print(nilai[3])


# Question number 2
"""
    Balik Urutan: Buatlah fungsi yang menerima list nama streetwear 
    (misal: ['Off-White', 'Stussy', 'Supreme']) dan 
    mengembalikannya dalam urutan terbalik tanpa menggunakan fungsi .reverse().
"""
def reverseBrand(brand):
    return brand[::-1]

Brand = ["off white", "vans", "Nike", "Adidas", "New Balance"]
print(reverseBrand(Brand))
