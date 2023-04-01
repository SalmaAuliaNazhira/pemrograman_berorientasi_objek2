# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

class Bentley:
    def fuel_type(self):
        print("Fuel type of Bentley is Petrol")
    def max_speed(self):
        print("and Max Speed is 562")

class BMW:
    def fuel_type(self):
        print("Fuel type of BMW is Diesel")
    def max_speed(self):
        print("and Max Speed is 240")

bentley = Bentley()
bmw = BMW()

def cetak_suara(object):
    object.fuel_type()
    object.max_speed()

cetak_suara(bentley) 
cetak_suara(bmw) 




