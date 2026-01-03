def input_nilai():
    data = input("Masukkan beberapa nilai (pisahkan dengan spasi): ")
    angka = list(map(int, data.split()))
    return angka


def nilai_terbesar_terkecil(angka):
    terbesar = max(angka)
    terkecil = min(angka)
    return terbesar, terkecil
