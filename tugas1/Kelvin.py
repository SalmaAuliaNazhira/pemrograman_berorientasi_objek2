# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin
    def to_fahrenheit(self):
        return 9/5 * (self.kelvin - 273) + 32
    def to_celcius(self):
        return self.kelvin - 273
    def to_reamur(self):
        return 4/5 * (self.kelvin - 273)
    
KelvinA = Kelvin(int(input("Masukkan Nilai Kelvin : ")))

print(f"Konversi dari Kelvin ke Fahrenheit adalah {KelvinA.to_fahrenheit()}", "derajat Fahrenheit")
print(f"Konversi dari Kelvin ke Celcius adalah {KelvinA.to_celcius()}", "derajat Celcius")
print(f"Konversi dari Kelvin ke Reamur adalah {KelvinA.to_reamur()}", "derajat Reamur")
