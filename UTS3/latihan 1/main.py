from utils import input_nilai, nilai_terbesar_terkecil

nilai = input_nilai()

if nilai:
    terbesar, terkecil = nilai_terbesar_terkecil(nilai)
    print("Nilai terbesar :", terbesar)
    print("Nilai terkecil :", terkecil)
else:
    print("Tidak ada nilai yang dimasukkan")
