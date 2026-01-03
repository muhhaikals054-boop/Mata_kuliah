def input_harga_konsumen(nomor):
    data = input(f"Masukkan harga barang konsumen {nomor} : ")
    harga = list(map(int, data.split()))
    return harga


def hitung_total(harga):
    total = 0
    for h in harga:
        total += h
    return total
