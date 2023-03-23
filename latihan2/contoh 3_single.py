# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang berjalan di jalan raya.")
class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Sepeda motor ini sedang belok di tikungan.")
motorA = SepedaMotor("Sepeda Motor", "Yamaha", "Hitam", 170)
motorA.berkendara() 
motorA.belok() 