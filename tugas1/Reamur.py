# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Reamur:
    def __init__(self, reamur):
        self.reamur = reamur
    def to_fahrenheit(self):
        return (self.reamur * 9/4) + 32
    def to_celcius(self):
       return self.reamur * 5/4
    def to_kelvin(self):
        return (self.reamur * 5/4) + 273
    
ReamurA = Reamur(int(input("Masukkan Nilai Reamur : ")))

print(f"Konversi dari Reamur ke Fahrenheit adalah {ReamurA.to_fahrenheit()}", "derajat Fahrenheit")
print(f"Konversi dari Reamur ke Celcius adalah {ReamurA.to_celcius()}", "derajat Celcius")
print(f"Konversi dari Reamur ke Kelvin adalah {ReamurA.to_kelvin()}", "derajat Kelvin")
