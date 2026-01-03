def input_nilai():
    data = input("Masukkan nilai tugas: ")
    nilai = list(map(float, data.split()))
    return nilai


def hitung_rata_rata(nilai):
    total = 0
    for n in nilai:
        total += n
    return total / len(nilai)


def cek_kelulusan(rata_rata, standar):
    if rata_rata >= standar:
        return "LULUS"
    else:
        return "TIDAK LULUS"
