# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

class Penulis:
    def __init__(self, nama):
        self.nama = nama
class Buku:
    def __init__(self, judul):
        self.judul = judul
class Perpustakaan:
    def __init__(self, penulis, buku):
        self.penulis = penulis
        self.buku = buku
penulis1 = Penulis("Salma Aulia Nazhira")
penulis2 = Penulis("Morgan Housel")
penulis3 = Penulis("Robert Cialdini")
buku = Buku("The Psychology of Money")
perpustakaan = Perpustakaan([penulis1, penulis2, penulis3], buku)
print(perpustakaan.penulis[1].nama) 