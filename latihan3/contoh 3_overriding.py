# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

# Implementasi Polymorphism Dinamis pada Abstract Class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Starting car...")

class Motorcycle(Vehicle):
    def start(self):
        print("Starting motorcycle...")

class Bus(Vehicle):
    def start(self):
        print("Starting bus...")
vehicles = [Car(), Motorcycle(), Bus()]

for vehicle in vehicles:
        vehicle.start()
