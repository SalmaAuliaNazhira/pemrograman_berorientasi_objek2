class Kereta:
        def __init__(self, stasiun, tujuan):
            self.stasiun = stasiun
            self.tujuan = tujuan
        def info(self):
            print(f"Stasiun: {self.stasiun}\nTujuan: {self.tujuan}")
KeretaA = Kereta("Kejaksan", "Cirebon - Bandung")
KeretaA.info()