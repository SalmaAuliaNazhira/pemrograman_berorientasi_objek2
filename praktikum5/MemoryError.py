# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

try:  
    l=[]  
    for i in range(1000000):  
        l.append('a')  
except MemoryError:  
    print("Memory limit is exceeded by the code")  
