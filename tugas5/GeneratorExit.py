# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C


# GeneratorExit
def generator_function():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator is being closed")

my_generator = generator_function()
next(my_generator)
my_generator.close()
