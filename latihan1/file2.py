class Anggota:
    def __init__(self, nama, nohp):
        self.nama = nama
        self.nohp = nohp
    def info(self):
        print(f"Nama: {self.nama}\nNO HP: {self.nohp}")
AnggotaB = Anggota("Sylvya", "08234671583")
AnggotaB.info()