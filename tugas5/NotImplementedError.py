# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

try:
    salary = int(input("Enter salary: "))
    print("So cool you earn %d amount." % salary)
except NotImplementedError:
    print("Hey, that wasn't a number!")

# another example
class BaseClass:
    def some_method(self):
        raise NotImplementedError("This method is not implemented")

class DerivedClass(BaseClass):
    pass

try:
    obj = DerivedClass()
    obj.some_method()
except NotImplementedError as e:
    print("NotImplementedError:", e)
