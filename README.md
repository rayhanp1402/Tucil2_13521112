# Tugas Kecil 2 IF2211 Strategi Algoritma
## Semester 2 (Genap) Tahun 2022/2023
### Pencarian Sepasang Titik Terdekat pada Ruang N-Dimensi dengan Algoritma Divide and Conquer

### Deskripsi Program

Program menerima input berupa n dimensi (n > 0) dan jumlah titik k (k > 1). Akan dicari
sepasang titik dari himpunan titik n-dimensi yang dibangkitkan secara acak sejumlah k dengan 
jarak terdekat d menggunakan rumus Euclidean Distance. Program menggunakan algoritma Divide and 
Conquer kemudian dibandingkan dengan algoritma Brute Force. Program juga akan menampilkan visualisasi
dari titik-titik tersebut.
Algoritma Divide and Conquer secara singkat dilakukan dengan langkah:
1. Masukan berupa larik bertipe titik di ruang N-Dimensi yang telah terurut berdasarkan nilai sumbu-x atau u11.
2. Kasus basisnya adalah ketika hanya terdapat dua titik dimana jaraknya dapat langsung dihitung dengan rumus Euclidean, atau tiga titik yang jarak terdekatnya juga dapat langsung dihitung dalam tiga perhitungan Euclidean.
3. Jika belum mencapai kasus basis, rekursi dilakukan dengan membagi larik menjadi dua bagian/daerah sama rata secara terus-menerus.
4. Masing-masing bagian/daerah akan dicari untuk jarak terkecil dari titik-titiknya, dan diambil nilai minimum dari kedua bagian daerah.
5. Akan diambil nilai delta, yaitu nilai jarak minimum dari kedua bagian daerah. Ditarik sebuah daerah dari pembagi sejauh delta. Titik yang berada di daerah tersebut (daerah dengan jarak delta dari pembagi) dicari jarak terkecilnya.
6. Dilakukan berulang kali secara rekursif hingga mendapat jarak terkecil dari himpunan titik tersebut.

### Requirement
- [Python3](https://www.python.org/downloads/) 
- matplotlib
- Library time, platform, random, math (standard library, sehingga seharusnya sudah disertakan saat meng-install python)

### Cara Clone Program
Agar program dapat dijalankan pada mesin Anda, clone repository program dengan cara

```sh
git clone https://github.com/rayhanp1402/Tucil2_13521112
```

### Cara Run Program
Jalankan main.py. Apabila menggunakan command-line, masuk ke folder root repository dan jalankan perintah berikut

```sh
cd Tucil2_13521112/src

python main.py
```
### Penggunaan Program
Saat run program, pertama kali akan ditampilkan main menu. Dari situ, pengguna memiliki pilihan untuk keluar dari program
atau "solve", yaitu mencari solusi untuk permainan Kartu 24.

Apabila pengguna memilih "solve", akan ditampilkan pilihan apakah ingin memilih empat kartu secara manual atau mengacaknya.
Untuk pemilihan kartu secara manual, input dapat berupa angka 2-10, 1 atau A, 11 atau J, 12 atau Q, dan 13 atau K

Selanjutnya akan ditampilkan jumlah solusi, solusi-solusinya, serta waktu eksekusi program dimana pengguna memiliki pilihan
untuk menyimpan hasil solusi tersebut pada sebuah file yang dapat dinamai oleh pengguna tersebut. File penyimpanan solusi
disimpan pada folder test.

Kemudian program akan kembali ke main menu.

Untuk input yang tidak sesuai, program akan mengulang hingga input benar.

### Contoh Penggunaan Program
1. Main menu

![Menu](https://cdn.discordapp.com/attachments/865154167169351730/1067554603052318730/show1.jpg)

<br>

2. Solve

![Solve](https://cdn.discordapp.com/attachments/865154167169351730/1067554602595127446/show2.jpg)

<br>

3. Simpan ke file

![Save](https://cdn.discordapp.com/attachments/865154167169351730/1067554602091814912/show3.jpg)

<br>

4. Exit

![Exit](https://cdn.discordapp.com/attachments/865154167169351730/1067554601722724463/show4.jpg)

## Dibuat oleh
Nama : Rayhan Hanif Maulana Pradana

NIM : 13521112