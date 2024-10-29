angka1 = float(input("Masukkan angka pertama: "))
operator = input("Masukkan operator (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

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

if hasil is not None:

    if hasil.is_integer():
        print(f"Hasil: {int(hasil)}")
    else:
        print(f"Hasil: {hasil}")
