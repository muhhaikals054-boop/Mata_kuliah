def input_harga():
    data = input("Masukkan harga barang: ")
    harga = list(map(int, data.split()))
    return harga


def hitung_total(harga):
    total = 0
    for h in harga:
        total += h
    return total


def hitung_diskon(total):
    if total >= 100000:
        return total * 0.1   # diskon 10%
    else:
        return 0
