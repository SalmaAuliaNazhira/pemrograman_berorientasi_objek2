# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

def my_generator():
    try: 
        for i in range(5):
            print('Yielding', i)
            yield i
    except GeneratorExit:
        print('Exiting early')
    
g = my_generator()
print (g.next())
g.close