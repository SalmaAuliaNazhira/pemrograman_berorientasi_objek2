# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

try :
    print("hello")
except SyntaxError as e:
    print("Invalid Syntax")
except :
    print("Invalid Syntax")

try:
    eval("hello =")
except SyntaxError:
    print("Invalid Syntax")