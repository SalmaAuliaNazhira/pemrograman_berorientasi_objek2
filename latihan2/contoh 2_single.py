# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")
class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")
dosenA = Dosen("Aulia", 30, "89101112")
dosenA.berbicara() 
dosenA.mengajar()