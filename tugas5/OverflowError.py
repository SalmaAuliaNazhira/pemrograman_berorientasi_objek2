# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

import math

try:
    print("The exponential value is")
    print(math.exp(1000))
    
except OverflowError as oe:
    print("After overflow", oe)