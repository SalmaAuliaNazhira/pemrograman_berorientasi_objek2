# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit
    def to_celcius(self):
        return 5/9 * (self.fahrenheit - 32)
    def to_reamur(self):
       return 4/9 * (self.fahrenheit - 32)
    def to_kelvin(self):
        return 5/9 * (self.fahrenheit - 32) + 273
    
FahrenheitA = Fahrenheit(int(input("Masukkan Nilai Fahrenheit : ")))

print(f"Konversi dari Fahrenheit ke Celcius adalah {FahrenheitA.to_celcius()}", "derajat Celcius")
print(f"Konversi dari Fahrenheit ke Reamur adalah {FahrenheitA.to_reamur()}", "derajat Reamur")
print(f"Konversi dari Fahrenheit ke Kelvin adalah {FahrenheitA.to_kelvin()}", "derajat Kelvin")
