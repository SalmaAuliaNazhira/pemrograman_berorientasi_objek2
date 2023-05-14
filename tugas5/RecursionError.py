# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

import math
if __name__ == '__main__':
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1) 
    try:
        print("The factorial of 1000 is: {}".format(factorial(2000)))
    except RecursionError as re:
        print("Unable to calculate factorial. Number is too big.")
        
# another example of RecursionError
def recursive_function():
    recursive_function()

try:
    recursive_function()
except RecursionError as e:
    print("RecursionError:", e)



































