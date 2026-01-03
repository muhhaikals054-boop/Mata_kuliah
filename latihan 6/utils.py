def parse_list(data_input: str):
    """
    Mengubah input string menjadi list angka (int)
    Contoh: "10000 20000 30000" -> [10000, 20000, 30000]
    """
    return list(map(int, data_input.split()))


def total_harga(data: list):
    """
    Menghitung total harga dari list angka
    """
    return sum(data)


def hitung_pajak(total: int):
    """
    Menghitung pajak 10%
    """
    return int(total * 0.10)


def format_rupiah(angka: int):
    """
    Memformat angka ke format rupiah
    Contoh: 15000 -> 15.000
    """
    return f"{angka:,}".replace(",", ".")
