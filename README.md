# Tugas Kecil 2 IF2211 Strategi Algoritma
## Semester 2 (Genap) Tahun 2022/2023
## Pencarian Sepasang Titik Terdekat pada Ruang N-Dimensi dengan Algoritma Divide and Conquer

## Deskripsi Program

Program menerima input berupa n dimensi (n > 0) dan jumlah titik k (k > 1). Akan dicari
sepasang titik dari himpunan titik n-dimensi yang dibangkitkan secara acak sejumlah k dengan 
jarak terdekat d menggunakan rumus Euclidean Distance. Program menggunakan algoritma Divide and 
Conquer kemudian dibandingkan dengan algoritma Brute Force. Program juga akan menampilkan visualisasi
dari titik-titik tersebut.
Algoritma Divide and Conquer secara singkat dilakukan dengan langkah:
1. Masukan berupa larik bertipe titik di ruang N-Dimensi yang telah terurut berdasarkan nilai sumbu-x atau u11 (lihat laporan).
2. Kasus basisnya adalah ketika hanya terdapat dua titik dimana jaraknya dapat langsung dihitung dengan rumus Euclidean, atau tiga titik yang jarak terdekatnya juga dapat langsung dihitung dalam tiga perhitungan Euclidean.
3. Jika belum mencapai kasus basis, rekursi dilakukan dengan membagi larik menjadi dua bagian/daerah sama rata secara terus-menerus.
4. Masing-masing bagian/daerah akan dicari untuk jarak terkecil dari titik-titiknya, dan diambil nilai minimum dari kedua bagian daerah.
5. Akan diambil nilai delta, yaitu nilai jarak minimum dari kedua bagian daerah. Ditarik sebuah daerah dari pembagi sejauh delta. Titik yang berada di daerah tersebut (daerah dengan jarak delta dari pembagi) dicari jarak terkecilnya.
6. Dilakukan berulang kali secara rekursif hingga mendapat jarak terkecil dari himpunan titik tersebut.

## Requirement
- [Python3](https://www.python.org/downloads/) 
- matplotlib
- Library time, platform, random, math (standard library, sehingga seharusnya sudah disertakan saat meng-install python)

## Cara Clone Program
Agar program dapat dijalankan pada mesin Anda, clone repository program dengan cara

```sh
git clone https://github.com/rayhanp1402/Tucil2_13521112
```

## Cara Run Program
Jalankan main.py. Apabila menggunakan command-line, masuk ke folder root repository dan jalankan perintah berikut

```sh
cd Tucil2_13521112/src

python main.py
```
## Dibuat oleh
Nama : Rayhan Hanif Maulana Pradana

NIM : 13521112