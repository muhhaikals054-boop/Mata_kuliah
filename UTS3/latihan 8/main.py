import utils

jumlah_konsumen = int(input("Masukkan jumlah konsumen: "))

print("\n--- INPUT BARANG KONSUMEN ---")

for i in range(1, jumlah_konsumen + 1):
    harga_barang = utils.input_harga_konsumen(i)
    total_bayar = utils.hitung_total(harga_barang)

    print(f"Total pembayaran konsumen {i}: {total_bayar}\n")
