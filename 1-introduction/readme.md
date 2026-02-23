# 🧠 Machine Learning Fundamentals

Repositori ini berisi dokumentasi dan catatan pembelajaran mengenai konsep dasar *Machine Learning* (ML). Dibuat sebagai referensi cepat untuk memahami apa itu ML, pentingnya keadilan (*fairness*) dalam pengembangan AI, serta teknik-teknik utama yang digunakan untuk melatih model algoritma.

---

## 1. Introduction to Machine Learning


*Machine Learning* adalah cabang dari Kecerdasan Buatan (AI) yang berfokus pada pengembangan sistem yang mampu belajar dari data, mengidentifikasi pola, dan membuat keputusan dengan intervensi manusia yang seminimal mungkin.

Perbedaan mendasar ML dengan pemrograman konvensional:
* **Pemrograman Tradisional:** *Programmer* memasukkan **Data** dan **Aturan (Logika If-Else)** ke dalam komputer untuk menghasilkan **Jawaban**.
* **Machine Learning:** *Engineer* memasukkan **Data** dan **Jawaban (Label)** ke dalam komputer, lalu algoritma ML akan mencari dan merumuskan **Aturan (Model)** secara otomatis.

Algoritma ML digunakan untuk menyelesaikan masalah yang terlalu kompleks jika menggunakan logika manual, seperti pengenalan gambar (Computer Vision), pemrosesan bahasa (NLP), dan sistem rekomendasi.

---

## 2. Fairness in Machine Learning


*Fairness* (Keadilan) adalah salah satu prinsip etika paling krusial dalam pengembangan sistem AI modern. Model Machine Learning sangat bergantung pada data historis. Jika data yang digunakan untuk melatih model mengandung bias (baik disengaja maupun tidak), model akan meniru dan bahkan memperkuat bias tersebut pada hasil prediksinya.

**Mengapa Fairness Sangat Penting?**
* **Menghindari Diskriminasi:** Mencegah algoritma mengambil keputusan yang merugikan kelompok tertentu (berdasarkan ras, gender, atau latar belakang sosial). Misalnya, algoritma rekrutmen (HR) yang menolak kandidat tertentu karena bias pada data masa lalu.
* **Membangun Kepercayaan:** Pengguna dan industri hanya akan mengadopsi sistem AI jika mereka yakin sistem tersebut mengambil keputusan secara objektif dan transparan.
* **Tanggung Jawab Data:** Memastikan bahwa himpunan data (*dataset*) yang digunakan sangat representatif dan model dievaluasi menggunakan metrik *fairness*, bukan sekadar melihat tingkat akurasi umum.

---