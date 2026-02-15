Level 1: The Warm-Up (Dasar Class & Object)
Studi Kasus: Sistem Nilai Mahasiswa Poltek

Buatlah class bernama Mahasiswa yang memiliki spesifikasi berikut:

1. Attributes (__init__):
    1. nama (string)
    2. nim (string)
    3. nilai_tugas (list of integers, contoh: [80, 90, 75])

2. Method tambah_nilai(angka):
    1. Menambahkan satu angka nilai ke dalam list nilai_tugas.
    2. Method hitung_rata_rata():
    3. Mengembalikan nilai rata-rata dari semua tugas.

3. Method cek_status():
    1. Jika rata-rata >= 75, return "LULUS".
    2. Jika di bawah itu, return "REMEDIAL".
    3. Tantangan: Buat 1 objek mahasiswa, tambah 3 nilai, lalu print status kelulusannya.