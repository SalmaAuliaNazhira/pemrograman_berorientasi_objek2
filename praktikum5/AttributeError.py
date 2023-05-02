# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

class Python():
    def __init__(self):
            self.a = "Python"

obj = Python()
try:
    print(obj.a)
    print(obj.b)
except AttributeError:
    print("There is no such attribute")