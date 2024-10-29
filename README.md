# labpy02

Tugas Laporan Praktikum 2

Nama : Rifqi Maulana

NIM : 312410529

Mata Kuliah : Bahasa Pemograman

# Kasus 1 : Program Pemesanan Tiket Bioskop

FlowChart :

![gambar](https://github.com/Shikilukeki/Foto/blob/main/FlowchartBioskop.png?raw=true
)

Penjelasan :

program ini menggunakan if, else, dan operator ternary

```python
harga_reguler = 50000
harga_vip = 100000
```

Inisialisasi dengan menetapkan variabel untuk harga tiket reguler dan VIP

```python
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()
```

Meminta User menginputkan pilihan tipe tiket dan menanyakan apakah User memiliki Kartu Member

```python
if tipe_tiket == "reguler" or tipe_tiket == "vip":
    harga_tiket = harga_reguler if tipe_tiket == "reguler" else harga_vip
```

Jika tipe tiket yang dimasukan adalah reguler maka User akan dikenakan biaya harga tiket reguler, sebaliknya, jika tipe tiket yang dipilih User adalah VIP maka User akan dikenakan biaya harga tiket VIP

```python
if member == "ya":
  harga_tiket *= 0.8
```

Jika user memiliki kartu member maka user akan mendapat potongan harga sebesar 20%

```python
print(f"Total harga yang harus dibayar: Rp{harga_tiket}")
else:
    print("Tipe tiket tidak valid!")
```

Jika semua sudah benar harga yang harus dibayarkan akan keluar, sebaliknya jika ada kesalahan, tipe tiket menjadi tidak valid

Contoh hasil eksekusi program : 

![gambar](https://github.com/Shikilukeki/Foto/blob/main/pemesanan%20tiket%20bioskop.png?raw=true)

# Kasus 2 : Program Kalkulator Sederhana

Flowchart : 

![Gambar](https://github.com/Shikilukeki/Foto/blob/main/Flowchart%20aritmatika%20sederhana.png?raw=true)

Program ini menggunakan if elif else untuk menentukan operasi aritmatika.

```python
angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))
```

User akan diminta menginputkan bilangan pertama, operator aritmatika, dan bilangan kedua untuk di jumlahkan

```python
if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
        hasil = None
else:
    print("Operator tidak valid!")
    hasil = None

```

Penggunaan if, elif (else if), dan else untuk menentukan operator aritmatika yang akan digunakan untuk penjumlahan angka pertama dan angka kedua, serta peringatan eror karna akan menghasilkan nilai tak terhingga (inf)

```python
if hasil is not None:

    if hasil.is_integer():
        print(f"Hasil: {int(hasil)}")
    else:
        print(f"Hasil: {hasil}")
```
Jika angka yang dimasukan bukan 0, maka akan ada decision apakah hasil dari penjumlahan itu decimal atau tidak, jika hasilnya bilangan bulat, makan output penjumlahan akan menjadi interger, sebaliknya, jika hasil penjumlahan adalah bilangan pecahan atau desimal, maka output hasil akan menjadi float

Contoh hasil eksekusi program :

![Gambar](https://github.com/Shikilukeki/Foto/blob/main/Aritmatika%20sederhana.png?raw=true)
