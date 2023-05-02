# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

try:
    with open("salma.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("File Not Found!")
