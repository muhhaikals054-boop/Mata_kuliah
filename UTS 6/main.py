from logika import *

while True:
    print("\nMENU")
    print("1. Konversi Nilai ke Label")
    print("2. Konversi Label ke Bobot")
    print("3. Hitung Total SKS")
    print("4. Hitung Total Nilai")
    print("5. Hitung IPS")
    print("6. Exit")

    pilihan = input("Pilihan: ")

    # MENU 1
    if pilihan == "1":
        nilai = float(input("Nilai Mahasiswa: "))
        print("Label:", nilai_ke_label(nilai))

    # MENU 2
    elif pilihan == "2":
        label = input("Label: ")
        print("Bobot:", label_ke_bobot(label))

    # MENU 3
    elif pilihan == "3":
        jumlah = int(input("Jumlah Data: "))
        sks_list = []

        for i in range(jumlah):
            sks_list.append(int(input(f"SKS {i+1}: ")))

        print("Total SKS:", hitung_total_sks(sks_list))

    # MENU 4
    elif pilihan == "4":
        jumlah = int(input("Jumlah Data: "))
        sks_list = []
        bobot_list = []

        print("\n--- input SKS ---")
        for i in range(jumlah):
            sks_list.append(int(input(f"SKS {i+1}: ")))

        print("\n--- input Nilai Mahasiswa ---")
        for i in range(jumlah):
            nilai = float(input(f"Nilai {i+1}: "))
            label = nilai_ke_label(nilai)
            bobot = label_ke_bobot(label)
            bobot_list.append(bobot)

        if len(sks_list) != len(bobot_list):
            print("Jumlah bobot dan SKS tidak sama")
        else:
            total_nilai = hitung_total_nilai(sks_list, bobot_list)
            print("Total Nilai:", total_nilai)

    # MENU 5
    elif pilihan == "5":
        jumlah = int(input("Jumlah Data: "))
        sks_list = []
        bobot_list = []

        print("\n--- input SKS ---")
        for i in range(jumlah):
            sks_list.append(int(input(f"SKS {i+1}: ")))

        print("\n--- input Nilai Mahasiswa ---")
        for i in range(jumlah):
            nilai = float(input(f"Nilai {i+1}: "))
            label = nilai_ke_label(nilai)
            bobot = label_ke_bobot(label)
            bobot_list.append(bobot)

        total_sks = hitung_total_sks(sks_list)
        total_nilai = hitung_total_nilai(sks_list, bobot_list)
        ips = hitung_ips(total_nilai, total_sks)

        print("IPS:", round(ips, 2))

    # EXIT
    elif pilihan == "6":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")