def parse_number(number_str):
    # Ganti koma menjadi titik agar bisa diproses float
    return float(number_str.replace(",", "."))


def format_decimal(number, decimal_places):
    # Format angka sesuai jumlah desimal
    formatted = f"{number:.{decimal_places}f}"
    # Kembalikan titik menjadi koma
    return formatted.replace(".", ",")