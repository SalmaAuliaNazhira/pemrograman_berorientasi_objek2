class Kubus:
    def __init__(self, s):
        self.s = s
    def luas(self):
        return 6 * (self.s ** 2)
kubusA = Kubus(23)
print(f"Luas Permukaan Kubus: {kubusA.luas()}")
