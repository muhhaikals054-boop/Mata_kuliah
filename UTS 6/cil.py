def input_sks(jumlah):
    sks = []
    print("\n--------- input SKS ---------")
    for i in range(jumlah):
        sks.append(int(input(f"SKS {i+1}: ")))
    return sks


def input_nilai(jumlah):
    nilai = []
    print("\n--------- input Nilai Mahasiswa ---------")
    for i in range(jumlah):
        nilai.append(int(input(f"Nilai {i+1}: ")))
    return nilai