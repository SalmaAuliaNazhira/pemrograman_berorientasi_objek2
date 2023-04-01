# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

class Lecture:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __mul__(self, teachingtime):
        print("Teach for", teachingtime.hours, "hours")
        return self.salary * teachingtime.hours

class TeachingTime:
    def __init__(self, name, hours) :
        self.name = name
        self.hours = hours

emp = Lecture("Salma Aulia", 10)
teachingtime = TeachingTime("Salma", 35)
print("salary is: $", emp*teachingtime)