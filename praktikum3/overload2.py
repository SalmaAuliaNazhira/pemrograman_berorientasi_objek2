# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age

H1 = Human("Salma", 20)
H2 = Human("Alya", 17)

print(H1 < H2)
print(H1 > H2)
