# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

# Implementasi Polymorphism Dinamis dalam Duck Typing

class Kucing:
    def bersuara(self):
        print("Meow")
        
class Anjing:
    def bersuara(self):
        print("Guk guk")
def cetak_suara(objek):
    objek.bersuara()
kucing = Kucing()
ajing = Anjing()
cetak_suara(kucing) 
cetak_suara(ajing) 