# 🐍 Python Core Concepts: Study Guide

Repository ini berisi catatan dan skrip latihan untuk mempelajari ulang struktur data dasar (List & Dictionary) serta konsep fungsi tingkat lanjut (Lambda & Rekursi) di Python.

## 📌 Daftar Modul Belajar
1. [List & Operasinya](#1-list--operasinya)
2. [Dictionary (Kamus Data)](#2-dictionary-kamus-data)
3. [Fungsi Lanjutan (Lambda & Rekursi)](#3-fungsi-lanjutan-lambda--rekursi)

---

## 1. List & Operasinya

File referensi: `list.py`

List adalah struktur data yang dapat menyimpan berbagai macam tipe data sekaligus dalam satu variabel.

* **Indexing & Slicing:**
  * Mengakses elemen pertama menggunakan index `[0]`, dan elemen terakhir menggunakan index `[-1]`.
  * Slicing digunakan untuk memotong list, contoh: `[0:-1]` (dari awal hingga sebelum terakhir), `[:15]` (index awal sampai 14), atau `[-5:]` (5 elemen terakhir).
* **Memanipulasi Data:**
  * Elemen list dapat diubah secara langsung menggunakan index, contoh: `listSeveral[14] = "H"`.
  * Beberapa elemen dapat diganti sekaligus menggunakan slicing, contoh: `listSeveral[10:] = ["F", "G", "H", "I", "J"]`.
* **Fungsi Bawaan (Built-in Functions):**
  * `len()` untuk mengetahui jumlah total item di dalam list.
  * `sum()`, `min()`, dan `max()` digunakan untuk operasi matematika pada list berisi angka.
  * *Catatan Penting:* Fungsi `sorted()` akan menghasilkan error jika digunakan pada list yang berisi campuran tipe data (seperti angka dan huruf).
* **Metode List & Pencarian:**
  * `.append("F")` menambahkan elemen "F" di akhir list, dan `.pop()` menghapus elemen paling akhir.
  * `.index('H')` mencari di index ke berapa elemen "H" berada, sedangkan operator `in` (contoh: `"H" in listSeveral`) akan menghasilkan nilai boolean True/False.

---

## 2. Dictionary (Kamus Data)

File referensi: `dic.py`

Dictionary digunakan untuk menyimpan data dalam format pasangan `key:value`. Sifat utamanya adalah: tidak berurutan (sebelum Python 3.7), nilainya dapat diubah (changeable), dan tidak boleh ada duplikasi *key*.

* **Cara Mengakses Data:**
  * Menggunakan kurung siku `[]`: `thisCar["brand"]`.
  * Menggunakan method `.get()`: `thisCar.get("brand")`. Ini lebih aman karena jika *key* tidak ditemukan, program akan mengembalikan nilai `None` alih-alih mengalami error.
* **Cek Keberadaan & Update Data:**
  * Gunakan sintaks `if "brand" in thisCar:` untuk memastikan sebuah *key* ada di dalam dictionary.
  * Gunakan method `.update({"universitas" : "Politeknik Negeri Madiun"})` untuk mengedit data lama atau menambahkan data baru sekaligus.
* **Menghapus Data:**
  * `.pop("job")` menghapus *key* spesifik dan mengembalikan *value* yang dihapus.
  * `del biodata["job"]` menghapus item spesifik menggunakan *keyword* bawaan Python.
* **Looping (Iterasi):**
  * Untuk mendapatkan *key* dan *value* secara bersamaan saat *looping*, gunakan method `.items()`: `for x, y in biodata.items():`.

---

## 3. Fungsi Lanjutan (Lambda & Rekursi)

File referensi: `func.py`

### A. Lambda Functions (Fungsi Anonim)
Lambda adalah fungsi anonim dalam satu baris dengan sintaks `lambda arguments : expression`.
* Lambda bisa memiliki satu atau beberapa parameter, contoh: `lambda x, y : x * y`.
* Sangat kuat saat digunakan di dalam fungsi lain sebagai fungsi anonim.
* Sering dikombinasikan dengan fungsi bawaan:
  * `map()`: Menerapkan fungsi lambda ke setiap elemen list (contoh: menggandakan nilai angka).
  * `filter()`: Menyaring elemen list berdasarkan kondisi lambda (contoh: mencari bilangan ganjil dengan `y % 2 != 0`).
  * `sorted()`: Mengurutkan list, contohnya mengurutkan kata berdasarkan panjang karakternya menggunakan `key = lambda x : len(x)`.

### B. Recursion (Fungsi Rekursif)
Rekursi terjadi ketika sebuah fungsi memanggil dirinya sendiri, yang merupakan konsep penting dalam matematika dan pemrograman.
* **Dua Komponen Utama Rekursi:**
  * *Base Case*: Kondisi untuk menghentikan rekursi (sangat penting untuk mencegah error *stack overflow*).
  * *Recursive Case*: Kondisi di mana fungsi memanggil dirinya sendiri dengan argumen yang sudah dimodifikasi.
* **Contoh Kasus Penggunaan:**
  * Menghitung nilai Faktorial dan deret Fibonacci (Rumus: `F(n) = F(n−1) + F(n−2)`).
  * Memproses List: Mencari total jumlahan (`sumList`), nilai maksimum (`find_max`), dan nilai minimum (`find_minim`) dalam sebuah list dengan cara membandingkan elemen pertama dengan sisa elemen di list (`[1:]`).

---

*Dokumentasi ini dibuat untuk keperluan review dan pembelajaran mandiri.*