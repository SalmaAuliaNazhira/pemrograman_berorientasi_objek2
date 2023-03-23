# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "bergerak")
class Serigala(Hewan):
    def __init__(self, nama, umur, warna_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = warna_bulu
    def bersuara(self):
        print("Auuuuuuu!")
SerigalaA = Serigala("Max", 2, "Abu-abu")
SerigalaA.bergerak() 
SerigalaA.bersuara()