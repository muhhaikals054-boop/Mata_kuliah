from utils import *

while True:
    print("\n=== PROGRAM 10 BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Layang-layang")
    print("6. Belah Ketupat")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Pentagon")
    print("10. Hexagon")
    print("0. Keluar")

    pilih = input("Pilih bangun datar: ")

    if pilih == "0":
        print("Program selesai.")
        break

    elif pilih == "1":
        s = float(input("Masukkan sisi: "))
        k, l = persegi(s)

    elif pilih == "2":
        p = float(input("Masukkan panjang: "))
        lbr = float(input("Masukkan lebar: "))
        k, l = persegi_panjang(p, lbr)

    elif pilih == "3":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        s = float(input("Masukkan sisi miring: "))
        k, l = segitiga(a, t, s)

    elif pilih == "4":
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        s = float(input("Masukkan sisi miring: "))
        k, l = jajar_genjang(a, t, s)

    elif pilih == "5":
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        s1 = float(input("Sisi 1: "))
        s2 = float(input("Sisi 2: "))
        k, l = layang_layang(d1, d2, s1, s2)

    elif pilih == "6":
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        s = float(input("Sisi: "))
        k, l = belah_ketupat(d1, d2, s)

    elif pilih == "7":
        a = float(input("Sisi atas: "))
        b = float(input("Sisi bawah: "))
        c = float(input("Sisi kiri: "))
        d = float(input("Sisi kanan: "))
        t = float(input("Tinggi: "))
        k, l = trapesium(a, b, c, d, t)

    elif pilih == "8":
        r = float(input("Jari-jari: "))
        k, l = lingkaran(r)

    elif pilih == "9":
        s = float(input("Masukkan sisi: "))
        k, l = pentagon(s)

    elif pilih == "10":
        s = float(input("Masukkan sisi: "))
        k, l = hexagon(s)

    else:
        print("Pilihan tidak valid!")
        continue

    print("\nKeliling =", round(k, 2))
    print("Luas     =", round(l, 2))

    input("\nTekan ENTER untuk memilih bangun datar lagi...")
