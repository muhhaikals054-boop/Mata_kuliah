def input_nilai_mahasiswa(nomor):
    data = input(f"Masukkan nilai mahasiswa ke-{nomor}: ")
    nilai = list(map(float, data.split()))
    return nilai


def hitung_rata_rata(nilai_list):
    if len(nilai_list) == 0:
        return 0
    return sum(nilai_list) / len(nilai_list)
