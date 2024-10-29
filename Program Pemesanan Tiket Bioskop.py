harga_reguler = 50000
harga_vip = 100000

tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").lower()
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

if tipe_tiket == "reguler" or tipe_tiket == "vip":
    harga_tiket = harga_reguler if tipe_tiket == "reguler" else harga_vip

    if member == "ya":
        harga_tiket *= 0.8

    harga_tiket = int(harga_tiket)

    print(f"Total harga yang harus dibayar: Rp{harga_tiket}")
else:
    print("Tipe tiket tidak valid!")
