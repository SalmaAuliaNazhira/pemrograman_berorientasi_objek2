# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

# Implementasi Polymorphism Dinamis pada Abstract Class
from abc import ABC, abstractmethod
class Flower(ABC):
    @abstractmethod
    def color(self):
        pass

class Rose(Flower):
    def color(self):
        print("Rose range in color from white to yellow to pink to dark crimson")

class Lotus(Flower):
    def color(self):
        print("Lotus colors is including white, pink, and blue")

class Lily(Flower):
    def color(self):
        print("Lily colors is every color of the rainbow")
flowers = [Rose(), Lotus(), Lily()]

for flower in flowers:
        flower.color()
