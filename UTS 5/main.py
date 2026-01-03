from utils import *

while True:
    print("\n=== MENU BANGUN RUANG ===")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Limas Segiempat")
    print("5. Tabung")
    print("6. Kerucut")
    print("7. Bola")
    print("8. Limas Segitiga")
    print("9. Prisma Segiempat")
    print("10. Limas Belah Ketupat")
    print("0. Keluar")

    pilih = input("Pilih bangun ruang: ")

    if pilih == "1":
        s = float(input("Sisi: "))
        v, l = kubus(s)
        print("Volume:", v)
        print("Luas Permukaan:", l)

    elif pilih == "2":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        v, lp = balok(p, l, t)
        print("Volume:", v)
        print("Luas Permukaan:", lp)

    elif pilih == "3":
        a = float(input("Alas: "))
        ta = float(input("Tinggi alas: "))
        t = float(input("Tinggi prisma: "))
        print("Volume:", prisma_segitiga(a, ta, t))

    elif pilih == "4":
        s = float(input("Sisi alas: "))
        t = float(input("Tinggi: "))
        print("Volume:", limas_segiempat(s, t))

    elif pilih == "5":
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        v, l = tabung(r, t)
        print("Volume:", v)
        print("Luas Permukaan:", l)

    elif pilih == "6":
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        v, l = kerucut(r, t)
        print("Volume:", v)
        print("Luas Permukaan:", l)

    elif pilih == "7":
        r = float(input("Jari-jari: "))
        v, l = bola(r)
        print("Volume:", v)
        print("Luas Permukaan:", l)

    elif pilih == "8":
        a = float(input("Luas alas: "))
        t = float(input("Tinggi: "))
        print("Volume:", limas_segitiga(a, t))

    elif pilih == "9":
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        print("Volume:", prisma_segiempat(p, l, t))

    elif pilih == "10":
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        t = float(input("Tinggi: "))
        print("Volume:", limas_belah_ketupat(d1, d2, t))

    elif pilih == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")

    input("\nTekan ENTER untuk kembali ke menu...")
