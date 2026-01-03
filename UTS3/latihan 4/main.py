import utils

harga_barang = utils.input_harga()
total = utils.hitung_total(harga_barang)
diskon = utils.hitung_diskon(total)
total_setelah_diskon = total - diskon

print("\n--- STRUK PEMBAYARAN ---")
print("Total Pembayaran           :", total)
print("Diskon                  :", diskon)
print("Total Pembayaran Setelah Diskon    :", total_setelah_diskon)
