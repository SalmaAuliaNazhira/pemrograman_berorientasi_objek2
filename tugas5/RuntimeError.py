# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

# RuntimeError
def raise_runtime_error():
    raise RuntimeError("This is a runtime error")

try:
    raise_runtime_error()
except RuntimeError as e:
    print("RuntimeError:", e)
