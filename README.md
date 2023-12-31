# Sistem Manajemen Parkir Dengan Deteksi Ketersediaan Tempat Parkir Berbasis Kamera

<p align="center">
<img src="https://drive.google.com/uc?id=1JuSMITXgxpVsnIv-qJIOxs_H-B1MWJkC" alt="milestone" width="500">
</p>

## Masalah
Mencari tempat parkir seringkali menjadi masalah yang sulit dihadapi, terutama di kota-kota besar di mana kepadatan kendaraan sangat tinggi dan ruang terbatas. Ketersediaan lahan parkir yang terbatas menyebabkan waktu yang banyak terbuang dalam mencari tempat parkir yang tersedia. Oleh karena itu, dibutuhkan solusi yang efektif untuk mengatasi masalah sulitnya mencari tempat parkir.

## Solusi
Deteksi ketersediaan tempat parker dengan kamera, sistem mendeteksi secara real-time tempat parkir dan menampilkan jumlah parkir yang tersedia dan mengarahkan tempat parkir yang harus ditempati oleh pengendara.

## Requirements dan Instalasi
1.	OpenCV (cv2)

Pustaka perangkat lunak open-source yang berfokus pada pemrosesan gambar dan visi komputer.

```
pip install opencv-python
```

2.	NumPy

Paket fundamental untuk komputasi numerik menggunakan bahasa pemrograman Python.

```
pip install numpy
```

3.	Cvzone

Library tambahan untuk OpenCV yang menyediakan berbagai alat dan fungsi tambahan untuk membantu dalam tugas pemrosesan gambar dan analisis video.

```
pip install cvzone
```

4.	PySerial

Digunakan untuk berkomunikasi dengan port serial.

```
pip install pyserial
```

## Cara Menggunakan Program
1.	Tangkap satu frame gambar pada kamera yang dipasang
2.	Masukkan file image tersebut ke folder detection
3.	Jalankan program PosisiParkir.py
```
python PosisiParkir.py
```
4.	Buat kotak-kotak parkir dengan klik kiri untuk menggambar dan klik kanan untuk menghapus
5.	Arahkan kamera ke tempat parker yang ingin dideteksi
6.	Kotak-kotak parkir sudah dibuat, lalu jalankan program main.py
```
python main.py
```
7.	Warna hijau menandakan parkir tersedia dan warna merah parkir terisi
8.	Jika terhubung dengan Arduino seperti program yang dibuat pada repo ini, maka data akan dikirimkan melalui serial. Saat button diklik, maka palang parkir terbuka dan pengguna parkir akan diarahkan ke parkiran yang kosong. Informasi jumlah parkir yang tersedia akan ditampilkan pada lcd secara real-time.

## Demonstrasi Program
[Link Demonstrasi](https://drive.google.com/drive/folders/1PETzjhlq0cf07AJ41RG7I8qPaSvyFDwo?usp=sharing)


## Anggota Kelompok dan Kontribusi

Programming

1.	Randy Verdian - 19622202
2.	Satriadhikara Panji Yudisthira – 19622274
3.	Juan Sohuturon Arauna Siagian – 19622148
4.	Francesco Michael Kusuma - 19622063

Prototyping

1.	Muhammad Al Thariq Fairuz – 19622026
2.	Thea Josephine Halim – 19622062
3.	Hanan Fitra Salam – 19622277
4.	M. Kasyfil Aziz – 19622238
5.	Filbert – 19622041
6.	Diero Arga Purnama – 19622153

Content

1.	Nasywaa Anggun Athiefah – 19622309
2.	Adinda Khairunnisa Indraputri – 19622229
3.	Muhammad Rafi Dhiyaulhaq – 19622158 
