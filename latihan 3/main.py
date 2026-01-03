import utils

nilai_tugas = utils.input_nilai()
standar_kelulusan = float(input("Masukkan standar kelulusan: "))

rata_rata = utils.hitung_rata_rata(nilai_tugas)
keterangan = utils.cek_kelulusan(rata_rata, standar_kelulusan)

print("\n--- HASIL ---")
print("Nilai rata-rata :", rata_rata)
print("Keterangan      :", keterangan)
