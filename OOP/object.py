"""
MODUL: DASAR OOP PYTHON
-----------------------
Panduan praktis memahami konsep dasar Object-Oriented Programming (OOP):
1. Class & Object (Cetak biru & Hasil)
2. Atribut & Method (Data & Fungsi)
3. Magic Methods (__init__, __str__)
4. Inheritance (Pewarisan sifat)

Author: Ahmadhakimitsnaini
Created: 11-02-2026
"""

# ==============================================================================
# BAGIAN 1: DEFINISI CLASS (Cetak Biru)
# ==============================================================================

class Employee:
    """
    Class ini adalah 'cetakan' untuk membuat data karyawan.
    Menggabungkan data (nama, umur) dan kemampuan (method) jadi satu.
    """

    # __init__ adalah fungsi yang JALAN OTOMATIS saat objek dibuat.
    def __init__(self, name: str, age: int, university: str):
        self.name = name          # Menyimpan nama ke dalam objek
        self.age = age            # Menyimpan umur
        self.university = university # Menyimpan asal kampus

    # Method: Fungsi yang dimiliki oleh objek
    def get_biodata(self) -> str:
        return f"{self.name}, {self.age} tahun, alumni {self.university}."
    
    # Method dengan parameter tambahan
    def show_talent(self, talent: str) -> str:
        return f"{self.name} punya bakat tersembunyi: {talent}."


# --- Contoh Eksekusi 1 ---
print("\n--- DEMO CLASS EMPLOYEE ---")

# Membuat Object (Realisasi dari cetak biru)
employee1 = Employee("Ahmadhakimitsnaini", 20, "Politeknik Negeri Madiun")

# Menggunakan fitur (method) milik objek
print(employee1.get_biodata())
print(employee1.show_talent("Python Coding"))


# ==============================================================================
# BAGIAN 2: MAGIC METHODS (Dunder Methods)
# ==============================================================================

class Car:
    """Class untuk mendemonstrasikan fungsi spesial Python."""

    def __init__(self, name, color):
        self.name = name
        self.color = color

    # __str__ mengatur tampilan teks saat objek di-print.
    # Jika tidak ada ini, hasil print hanya berupa kode memori yang aneh.
    def __str__(self) -> str:
        return f"Mobil: {self.name} | Warna: {self.color}"

# --- Contoh Eksekusi 2 ---
print("\n--- DEMO MAGIC METHOD ---")

my_car = Car("BMW M3", "Merah")

# Saat diprint, Python otomatis mencari method __str__
print(my_car) 


# ==============================================================================
# BAGIAN 3: INHERITANCE (Pewarisan)
# ==============================================================================
# Konsep: Anak (Child) mewarisi semua sifat & fitur Orang Tua (Parent).
# Kita tidak perlu menulis ulang kode yang sama.



# [Image of OOP inheritance diagram]


# UgmPerson adalah ANAK dari Employee (Parent)
class UgmPerson(Employee): 
    pass  # 'pass' artinya: "Ikuti saja semua fitur orang tua, tidak ada tambahan."

class ItbPerson(Employee): 
    pass 

# --- Contoh Eksekusi 3 ---
print("\n--- DEMO INHERITANCE ---")

# Kita bisa isi data nama/umur karena mewarisi __init__ milik Employee
itb_student = ItbPerson("Ahmad Hakim", 20, "ITB")
ugm_student = UgmPerson("Sani", 21, "UGM")

# 1. Memanggil method warisan
print(f"Info ITB: {itb_student.get_biodata()}")

# 2. Cek Hubungan Keluarga (isinstance)
print("\n--- CEK HUBUNGAN ---")
# Apakah itb_student termasuk Employee? -> True (Karena dia turunan Employee)
print(f"Apakah mahasiswa ITB seorang Employee? : {isinstance(itb_student, Employee)}")