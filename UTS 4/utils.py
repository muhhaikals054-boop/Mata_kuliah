import math

def persegi(s):
    return 4 * s, s * s

def persegi_panjang(p, l):
    return 2 * (p + l), p * l

def segitiga(a, t, s):
    return a + t + s, 0.5 * a * t

def jajar_genjang(a, t, s):
    return 2 * (a + s), a * t

def layang_layang(d1, d2, s1, s2):
    return 2 * (s1 + s2), 0.5 * d1 * d2

def belah_ketupat(d1, d2, s):
    return 4 * s, 0.5 * d1 * d2

def trapesium(a, b, c, d, t):
    return a + b + c + d, 0.5 * (a + b) * t

def lingkaran(r):
    return 2 * math.pi * r, math.pi * r * r

def pentagon(s):
    keliling = 5 * s
    luas = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * s * s
    return keliling, luas

def hexagon(s):
    keliling = 6 * s
    luas = (3 * math.sqrt(3) / 2) * s * s
    return keliling, luas
