import math

# 1. Kubus
def kubus(sisi):
    volume = sisi ** 3
    luas = 6 * sisi ** 2
    return volume, luas


# 2. Balok
def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    return volume, luas


# 3. Prisma Segitiga
def prisma_segitiga(alas, tinggi_alas, tinggi_prisma):
    volume = (alas * tinggi_alas / 2) * tinggi_prisma
    return volume


# 4. Limas Segiempat
def limas_segiempat(sisi, tinggi):
    volume = (1/3) * sisi * sisi * tinggi
    return volume


# 5. Tabung
def tabung(jari, tinggi):
    volume = math.pi * jari ** 2 * tinggi
    luas = 2 * math.pi * jari * (jari + tinggi)
    return volume, luas


# 6. Kerucut
def kerucut(jari, tinggi):
    s = math.sqrt(jari**2 + tinggi**2)
    volume = (1/3) * math.pi * jari ** 2 * tinggi
    luas = math.pi * jari * (jari + s)
    return volume, luas


# 7. Bola
def bola(jari):
    volume = (4/3) * math.pi * jari ** 3
    luas = 4 * math.pi * jari ** 2
    return volume, luas


# 8. Limas Segitiga
def limas_segitiga(luas_alas, tinggi):
    volume = (1/3) * luas_alas * tinggi
    return volume


# 9. Prisma Segiempat
def prisma_segiempat(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume


# 10. Limas Belah Ketupat
def limas_belah_ketupat(d1, d2, tinggi):
    luas_alas = 0.5 * d1 * d2
    volume = (1/3) * luas_alas * tinggi
    return volume
