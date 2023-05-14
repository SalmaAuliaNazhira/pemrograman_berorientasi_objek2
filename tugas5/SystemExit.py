# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

print("Program that uses SystemExit as Exception instead of BaseException.")
try:
    raise SystemExit
    
except SystemExit:
    print("Specifying SystemError exception in this block works.")

# another example

import sys

try:
    
    sys.exit("Terminating the program")
except SystemExit as e:
    print("SystemExit:", e)
    
    print("Performing cleanup tasks...")
    
    
