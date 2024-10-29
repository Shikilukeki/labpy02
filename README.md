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
