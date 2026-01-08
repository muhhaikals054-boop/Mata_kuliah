# =========================
# BAGIAN 1
# konversi nilai ke label
# =========================
def nilai_ke_label(nilai):
    if nilai >= 85:
        return "a"
    elif nilai >= 80:
        return "a-"
    elif nilai >= 75:
        return "b+"
    elif nilai >= 70:
        return "b"
    elif nilai >= 65:
        return "b-"
    elif nilai >= 60:
        return "c+"
    elif nilai >= 55:
        return "c"
    elif nilai >= 50:
        return "d"
    else:
        return "e"


# =========================
# BAGIAN 2
# konversi label ke bobot
# =========================
def label_ke_bobot(label):
    if label == "a":
        return 4
    elif label == "a-":
        return 3.75
    elif label == "b+":
        return 3.5
    elif label == "b":
        return 3
    elif label == "b-":
        return 2.75
    elif label == "c+":
        return 2.5
    elif label == "c":
        return 2
    elif label == "d":
        return 1
    elif label == "e":
        return 0


# =========================
# BAGIAN 3
# hitung total sks
# =========================
def hitung_total_sks(sks_list):
    return sum(sks_list)


# =========================
# BAGIAN 4
# hitung total nilai
# =========================
def hitung_total_nilai(sks_list, bobot_list):
    total = 0
    for i in range(len(sks_list)):
        total += sks_list[i] * bobot_list[i]
    return total


# =========================
# BAGIAN 5
# hitung IPS
# =========================
def hitung_ips(total_nilai, total_sks):
    if total_sks == 0:
        return 0
    return total_nilai / total_sks