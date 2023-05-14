# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

my_list = [1, 2, 3]
my_iterator = iter(my_list)

while True:
    try:
        # Get the next item from the iterator
        item = next(my_iterator)
        print(item)
    except StopIteration:
        # Stop the loop when StopIteration is raised
        break
