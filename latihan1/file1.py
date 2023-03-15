class Handphone:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Handphone {self.merk} berwarna {self.warna}")

HandphoneA = Handphone("Samsung", "Biru")
HandphoneA.info()