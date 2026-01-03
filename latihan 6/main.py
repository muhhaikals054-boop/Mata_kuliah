from utils import parse_list, total_harga, hitung_pajak, format_rupiah

data_input = input("Masukkan harga barang (pisahkan spasi): ")
data = parse_list(data_input)

total = total_harga(data)
pajak = hitung_pajak(total)
total_bayar = total + pajak

print("Total harga        : Rp", format_rupiah(total))
print("Pajak 10%          : Rp", format_rupiah(pajak))
print("Total yang dibayar : Rp", format_rupiah(total_bayar))
