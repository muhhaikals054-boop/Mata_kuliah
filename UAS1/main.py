import os
from utils import nilai_ke_label, hitung_ip

biodata = {}
sks_list = []
nilai_list = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("------------Menu Utama------------")
    print("1. Biodata")
    print("2. Input SKS")
    print("3. Input Nilai")
    print("4. Lihat Nilai")
    print("5. Lihat IP")
    print("6. Keluar")

while True:
    clear()
    menu()
    pilihan = input("Pilihan: ")

    # ================= BIODATA =================
    if pilihan == "1":
        print("------------Biodata Mahasiswa------------")
        mode = input("1. Lihat Biodata\n2. Input Biodata\nPilih: ")
        if mode == "1":
            if not biodata:
                print("Biodata belum diinput.")
            else:
                print(f"Nama: {biodata['nama']}")
                print(f"NIM : {biodata['nim']}")
        elif mode == "2":
            biodata['nama'] = input("Nama: ")
            biodata['nim'] = input("NIM : ")

    # ================= SKS =================
    elif pilihan == "2":
        print("------------Input SKS------------")
        try:
            sks_input = input("SKS (pisahkan dengan spasi): ")
            sks_list = list(map(int, sks_input.split()))
            print("SKS berhasil disimpan.")
        except:
            print("Input SKS harus angka!")

    # ================= NILAI =================
    elif pilihan == "3":
        print("------------Input Nilai------------")
        mode = input("1. Angka\n2. Huruf\nPilih: ")
        nilai_list.clear()

        if mode == "1":
            try:
                nilai_input = input("Nilai angka (pisahkan spasi): ")
                angka_list = list(map(int, nilai_input.split()))
                nilai_list = [nilai_ke_label(n) for n in angka_list]
            except:
                print("Nilai harus berupa angka!")
        elif mode == "2":
            nilai_input = input("Nilai huruf (A, B+, dst): ")
            nilai_list = nilai_input.upper().split()

    # ================= LIHAT NILAI =================
    elif pilihan == "4":
        print("------------Nilai Mahasiswa------------")
        if not nilai_list:
            print("Data nilai belum diinput.")
        else:
            print(f"Nama : {biodata.get('nama', '-')}")
            print(f"NIM  : {biodata.get('nim', '-')}")
            print(f"Nilai: {nilai_list}")

    # ================= HITUNG IP =================
    elif pilihan == "5":
        if not nilai_list or not sks_list:
            print("Nilai atau SKS belum diinput.")
        elif len(nilai_list) != len(sks_list):
            print("Jumlah nilai dan SKS tidak sama!")
        else:
            ip = hitung_ip(nilai_list, sks_list)
            print(f"IP Anda: {ip}")

    # ================= KELUAR =================
    elif pilihan == "6":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk kembali ke menu...")