# Nama : Salma Aulia Nazhira
# NIM : 210511132
# Kelas : R3/C

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("The animal speaks")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print("The cat meowly")

class Persia(Cat):
    def __init__(self, name, breed, origin):
        super().__init__(name, breed)
        self.origin = origin
    def speak(self):
        print("The Persia growls")
