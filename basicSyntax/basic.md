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