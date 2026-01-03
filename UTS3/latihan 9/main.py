from utils import input_nilai_mahasiswa, hitung_rata_rata

jumlah = int(input("Masukkan jumlah mahasiswa: "))

print("\n--- INPUT NILAI MAHASISWA ---")
for i in range(1, jumlah + 1):
    nilai = input_nilai_mahasiswa(i)
    rata_rata = hitung_rata_rata(nilai)

    print(f"Rata-rata nilai mahasiswa ke-{i}: {rata_rata:.2f}\n")
