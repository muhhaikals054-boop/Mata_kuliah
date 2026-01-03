import utils

harga_barang = utils.input_harga()
total_bayar = utils.hitung_total(harga_barang)

print("Total pembayaran:", total_bayar)
